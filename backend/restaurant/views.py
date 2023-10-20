from django.shortcuts import render

from django.http import JsonResponse

from .models import Restaurant, Brands

# Serializers
from .serializers import CreateRestaurantSerializer, GetAllRestaurants, CreateBrandSerializer, GetBrandSerializer

# Rest
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import viewsets, filters
from rest_framework.generics import DestroyAPIView




class CreateRestaurant(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        
        
        
        serializer = CreateRestaurantSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message' : 'Success'},status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
        
        
class GetRestaurants(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    # query
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name',)

    serializer_class = GetAllRestaurants

    def get_queryset(self):
        city = self.request.GET.get('city')
        queryset = Restaurant.objects.all()
        
        if city in city != 'all':
            queryset = queryset.filter(city=city)
        
        
        return queryset
    
class GetPossibleCities(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        unique_cities = Restaurant.objects.values('city').distinct()
        list = [city['city'] for city in unique_cities]
        return JsonResponse(list, status=200, safe=False)      

class DeleteRestaurant(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class = GetAllRestaurants
    lookup_field = 'name'
    
    
    
    
# Brand
class CreateBrand(APIView):
    
    """ This class is made for creating new brand instansce in database. 
    It also checks for unique values, to ensure every instansce has unique primary key.

    Returns:
        JSON : message of status of operation 
    """
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        
        # Check for unique 
        fields_to_check = ['name']

        for field_name in fields_to_check:
            if field_name in data:
                field_value = data[field_name]

                duplicate_exists = Brands.objects.filter(**{field_name: field_value}).exists()
                if duplicate_exists:
                    return JsonResponse({'error': f'Given {field_name} is already taken. Please try another.'}, status=400) 
        
        serializer = CreateBrandSerializer(data=data)
        
        if serializer.is_valid():
            brand = serializer.save()
            return JsonResponse({'message' : f'Succesfully created {brand.name}'},status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
        
        
        


class GetBrands(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id=None):

        if id:
            brand = Brands.objects.get(id=id)
            serializer = GetBrandSerializer(brand)
        
        else:
            all_brands = Brands.objects.all()
            serializer = GetBrandSerializer(all_brands, many=True)
            
        return JsonResponse(serializer.data, status=200, safe=False)

# Brand