from django.shortcuts import render

from django.http import JsonResponse

from .models import Restaurant

# Serializers
from .serializers import CreateRestaurantSerializer, GetAllRestaurants

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