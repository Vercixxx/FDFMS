from django.shortcuts import render

from django.http import JsonResponse

from .models import Restaurant, Brands

# Serializers
from .serializers import CreateRestaurantSerializer, GetAllRestaurants, CreateBrandSerializer, GetBrandSerializer, UpdateBrandSerializer

# Rest
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import viewsets, filters
from rest_framework.generics import DestroyAPIView




class CreateRestaurant(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
            
        # Check for unique 
        fields_to_check = ['name']

        for field_name in fields_to_check:
            if field_name in data:
                field_value = data[field_name]

                duplicate_exists = Restaurant.objects.filter(**{field_name: field_value}).exists()
                if duplicate_exists:
                    return JsonResponse({'error': f'Given {field_name} is already taken. Please try another.'}, status=400) 
        
        serializer = CreateRestaurantSerializer(data=data)
        
        if serializer.is_valid():
            brand = serializer.save()
            return JsonResponse({'message' : f'Succesfully created {brand.name}'},status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
        
        
class GetRestaurants(APIView):
    permission_classes = [IsAuthenticated]
    
    
    def get(self, request, city, id=None):
        print(id)
        if id:
            restaurant = Restaurant.objects.get(id=id)
            serializer = GetAllRestaurants(restaurant)
        
        else:
            if city == "All":
                all_restaurants = Restaurant.objects.all()
            else:
                all_restaurants = Restaurant.objects.filter(city=city)
            serializer = GetAllRestaurants(all_restaurants, many=True)
            
        return JsonResponse(serializer.data, status=200, safe=False)
    
    
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
    
    



# Deletion
class DeleteBrands(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Brands.objects.all()
    lookup_field = 'id'
# Deletion





# Updating brand
class UpdateBrand(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, brandID):
        data = request.data

        try:
            brand = Brands.objects.get(id=brandID)

            fields_to_check = ['name']

            for field_name in fields_to_check:
                if field_name in data:
                    field_value = data[field_name]

                    if field_value != getattr(brand, field_name) and Brands.objects.exclude(id=brandID).filter(**{field_name: field_value}).exists():
                        return JsonResponse({'error': f'Given {field_name} is already taken. Please try another.'}, status=400) 
        
        
            serializer = UpdateBrandSerializer(brand, data=data)
            
            if serializer.is_valid():
                serializer.update(brand, data)  
                return JsonResponse({'message' : 'Success'},status=200)
            
            else:
                return JsonResponse(serializer.errors, status=400)
            
        except Brands.DoesNotExist:
            return JsonResponse({'error': 'Brand does not exist.'}, status=404)
# Updating brand
# Brand