from django.http import JsonResponse

from datetime import datetime, date

# Rest
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import DestroyAPIView

# Models
from .models import Driver, DailyWork
from fleet.models import Fleet
from restaurant.models import Restaurant
from users.models import GeneralUser, Addresses

# Serializers
from .serializers import RestaurantDriversSerliazer, DriverUsernameSerializer, DailyDriverReportSerializer
from users.serializers import ResidenceAddressSerializer


# DB
from django.db.models import Q,F


class GetRestaurants(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        driver = Driver.objects.get(username=username)
        restaurants = Restaurant.objects.filter(drivers=driver)
        result = {}

        for restaurant in restaurants:
            fleets = Fleet.objects.filter(restaurant=restaurant)
            result[restaurant.name] = [car.license_plate for fleet in fleets for car in fleet.cars.filter(active=True)]

        return JsonResponse(result, safe=False)
    
class UsersPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 100

    def get_page_size(self, request):
        page_size = super().get_page_size(request)
        if page_size is None or page_size == 0:
            return self.max_page_size
        return page_size
    
    
class GetDriversUsernames(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        restaurant = self.request.query_params.get('restaurant', '').strip()

        # Choosing correct serializer and user model
        serializer_class = DriverUsernameSerializer
        user_model = Driver

        queryset = user_model.objects.all()
        
        # Get users from selected restaurant
        restaurants = Restaurant.objects.filter(name=restaurant)
        
        drivers = Driver.objects.none()

        for restaurant in restaurants:
            drivers |= restaurant.drivers.all().order_by('date_joined')

        queryset = drivers.filter(is_active=True)

        serialized_data = serializer_class(queryset, many=True).data
        return JsonResponse(serialized_data, status=200, safe=False)

    
class GetDrivers(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = UsersPagination

    @staticmethod
    def get_addresses(username):
        try:
            user = GeneralUser.objects.get(username=username)
            address = Addresses.objects.get(username=user)
            return ResidenceAddressSerializer(instance=address).data
        except GeneralUser.DoesNotExist:
            return {'error': 'User not found'}
        except Addresses.DoesNotExist:
            return {'error': 'Address not found'}

    def get(self, request):
        limit = self.request.query_params.get('limit', '').strip()
        query = self.request.query_params.get('search', '').strip()
        status = self.request.query_params.get('status', '').strip()
        restaurant = self.request.query_params.get('restaurant', '').strip()


        # Choosing correct serializer and user model
        serializer_class = RestaurantDriversSerliazer
        user_model = Driver

        queryset = user_model.objects.all()
        
        # Get users from selected restaurant
        restaurants = Restaurant.objects.filter(name=restaurant)
        
        drivers = Driver.objects.none()

        for restaurant in restaurants:
            drivers |= restaurant.drivers.all().annotate(restaurant_name=F('restaurant__name')).order_by('date_joined')

        queryset = drivers
        
        
        # Filtering by status
        if status == 'True':
            queryset = queryset.filter(is_active=True)
        elif status == 'False':
            queryset = queryset.filter(is_active=False)

        # Additional filtering using Q
        if query:
            queryset = queryset.filter(
                Q(username__icontains=query) | Q(email__icontains=query))

        

        paginator = UsersPagination()
        result_page = paginator.paginate_queryset(queryset, request)

        serialized_data = []
        for user in result_page:
            user_data = serializer_class(user).data
            address_data = self.get_addresses(user.username)
            user_data.update(address_data)
            serialized_data.append(user_data)

        response_data = {
            'posts_amount': paginator.page.paginator.count,
            'total_pages': paginator.page.paginator.num_pages,
            'current_page': paginator.page.number,
            'results': serialized_data,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'total_results': queryset.count(),
        }
        
        return JsonResponse(response_data, status=200)




class AddDailyReport(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        
        data['start_work'] = datetime.strptime(data['start_shift'], '%H:%M').time()
        data['end_work'] = datetime.strptime(data['end_shift'], '%H:%M').time()
        
        # Working time
        working_time = datetime.combine(date.min, data['end_work']) - datetime.combine(date.min, data['start_work'])
        hours, remainder = divmod(working_time.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        data['working_time'] = '{:02}:{:02}'.format(hours, minutes)
        # Working time
        
        data['driver'] = Driver.objects.get(username=data['driver'])

        serializer = DailyDriverReportSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'ok'}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)