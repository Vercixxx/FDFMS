from django.http import JsonResponse

# Rest
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import DestroyAPIView

# Models
from .models import Driver
from fleet.models import Fleet
from restaurant.models import Restaurant
from users.models import GeneralUser, Addresses

# Serializers
from .serializers import RestaurantDriversSerliazer
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
