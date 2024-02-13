from django.http import JsonResponse


# Serializers
from .serializers import BrandSerializer, RestaurantSerializer, RestaurantInfoSerializer, RestaurantNameIdSerializer

# Rest
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import DestroyAPIView

# Models
from .models import Restaurant, Brands

# DB
from django.db.models import Q


# Pagination
class LocalPaginator(PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 100

    def get_page_size(self, request):
        page_size = super().get_page_size(request)
        if page_size is None or page_size == 0:
            return self.max_page_size
        return page_size
# Pagination


class CreateRestaurant(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        brand = Brands.objects.get(name=data['brand'])
        data['brand'] = brand.id

        # Check for unique
        fields_to_check = ['name']

        errors = [
            f'Given {field} is already taken. Please try another.'
            for field in fields_to_check
            if Restaurant.objects.filter(**{field: data.get(field, None)}).exists()
        ]

        if errors:
            return JsonResponse({'error': ' '.join(errors)}, status=400)
        # Check for unique

        serializer = RestaurantSerializer(data=data)

        if serializer.is_valid():
            restaurant = serializer.save()
            return JsonResponse({'message': f'Succesfully created {restaurant.name}'}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)


class UpdateRestaurant(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, name):
        data = request.data

        brand_name = data['brand']
        brand = Brands.objects.get(name=brand_name)
        data['brand'] = brand.pk

        try:

            # Check for unique
            fields_to_check = ['name']

            errors = [
                f'Given {field} is already taken. Please try another.'
                for field in fields_to_check
                if Restaurant.objects.filter(**{field: data.get(field, None)}).exists() > 1
            ]

            if errors:
                return JsonResponse({'error': ' '.join(errors)}, status=400)
            # Check for unique

            restaurant = Restaurant.objects.get(name=name)

            serializer = RestaurantSerializer(restaurant, data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': f'Succesfully edited {restaurant.name}'}, status=200)

            else:
                return JsonResponse(serializer.errors, status=400)

        except Restaurant.DoesNotExist:
            return JsonResponse({'error': 'Restaurant does not exist.'}, status=404)


class GetRestaurants(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            restaurant = Restaurant.objects.get(id=id)
            serializer = RestaurantInfoSerializer(restaurant)

            return JsonResponse(serializer.data, status=200, safe=False)

        else:
            limit = self.request.query_params.get('limit', '').strip()
            query = self.request.query_params.get('search', '').strip()

            queryset = Restaurant.objects.all()

            if query:
                queryset = queryset.filter(Q(name__icontains=query)) | (
                    Q(city__icontains=query) | Q(brand__name__icontains=query))

            paginator = LocalPaginator()
            response_page = paginator.paginate_queryset(queryset, request)

            serialized_data = [RestaurantInfoSerializer(
                restaurant).data for restaurant in response_page]

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


class GetRestaurantsNameId(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = self.request.query_params.get('search', '').strip()


        if query:
            queryset = queryset.filter(Q(name__icontains=query)) | (
                Q(id__icontains=query))
            
        else:
            queryset = Restaurant.objects.all()
            

        serializer = RestaurantNameIdSerializer(queryset, many=True)

        return JsonResponse(serializer.data, status=200, safe=False)


class DeleteRestaurant(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'id'


# Brand
class CreateBrand(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        # Check for unique
        fields_to_check = ['name']

        errors = [
            f'Given {field} is already taken. Please try another.'
            for field in fields_to_check
            if Brands.objects.filter(**{field: data.get(field, None)}).exists()
        ]

        if errors:
            return JsonResponse({'error': ' '.join(errors)}, status=400)
        # Check for unique

        serializer = BrandSerializer(data=data)

        if serializer.is_valid():
            brand = serializer.save()
            return JsonResponse({'message': f'Succesfully created {brand.name}'}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)


class GetBrands(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            brand = Brands.objects.get(id=id)
            serializer = BrandSerializer(brand)

            return JsonResponse(serializer.data, status=200, safe=False)

        else:
            limit = self.request.query_params.get('limit', '').strip()
            query = self.request.query_params.get('search', '').strip()

            queryset = Brands.objects.all()

            if query:
                queryset = queryset.filter(name__icontains=query)

            paginator = LocalPaginator()
            response_page = paginator.paginate_queryset(queryset, request)

            serialized_data = [BrandSerializer(
                brand).data for brand in response_page]

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


# Deletion
class DeleteBrands(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'id'
# Deletion


# Updating brand
class UpdateBrand(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, brandID):
        data = request.data

        try:

            # Check for unique
            fields_to_check = ['name']

            errors = [
                f'Given {field} is already taken. Please try another.'
                for field in fields_to_check
                if Brands.objects.filter(**{field: data.get(field, None)}).exists() > 1
            ]

            if errors:
                return JsonResponse({'error': ' '.join(errors)}, status=400)
            # Check for unique

            brand = Brands.objects.get(id=brandID)

            serializer = BrandSerializer(brand, data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'Success'}, status=200)

            else:
                return JsonResponse(serializer.errors, status=400)

        except Brands.DoesNotExist:
            return JsonResponse({'error': 'Brand does not exist.'}, status=404)
# Updating brand
