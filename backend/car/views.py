from django.http import JsonResponse

from .serializers import CarSerializer

from .models import Car

from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

# DB
from django.db.models import F
from django.db.models import Q

# Pagination
from rest_framework.pagination import PageNumberPagination


class AddCar(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        # Check for unique
        fields_to_check = ['vin']

        errors = [
            f'Given {field} is already taken. Please try another.'
            for field in fields_to_check
            if Car.objects.filter(**{field: data.get(field, None)}).exists()
        ]

        if errors:
            return JsonResponse({'error': ' '.join(errors)}, status=400)
        # Check for unique

        serializer = CarSerializer(data=data)

        if serializer.is_valid():
            car = serializer.save()
            return JsonResponse({'message': f'Successfully created car vin - {car.vin}'}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)


class DeleteCar(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'vin'





class CarsPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 100

    def get_page_size(self, request):
        page_size = super().get_page_size(request)
        if page_size is None or page_size == 0:
            return self.max_page_size
        return page_size

class GetCars(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CarsPagination


    def get(self, request):
        limit = self.request.query_params.get('limit', '').strip()
        query = self.request.query_params.get('search', '').strip()
        

        serializer_class = CarSerializer
        queryset = Car.objects.all()
        
        if query:
            queryset = queryset.filter(
                Q(brand__icontains=query) | Q(model__icontains=query) | Q(vin__icontains=query)
            )
            
        paginator = CarsPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        
        serialized_data = []
        
        for car in result_page:
            car_data = serializer_class(car).data
            serialized_data.append(car_data)
            
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



class GetCar(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, vin):
        car = Car.objects.get(vin=vin)
        serializer = CarSerializer(car)

        return JsonResponse(serializer.data, status=200)


class EditCar(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, vin):
        data = request.data

        try:
            car = Car.objects.get(vin=vin)
            serializer = CarSerializer(car, data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'Success'}, status=200)

            else:
                return JsonResponse(serializer.errors, status=400)

        except Car.DoesNotExist:
            return JsonResponse({'error': 'Car does not exist.'}, status=404)
