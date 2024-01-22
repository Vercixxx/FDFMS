from django.http import JsonResponse

# Pagination
from rest_framework.pagination import PageNumberPagination

# Serializers
# from .serializers import
from restaurant.serializers import RestaurantNameIdSerializer

# Models
from restaurant.models import Restaurant
from driver.models import Driver 
from .models import RestManager

# Rest
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

class GetRestaurants(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = request.query_params.get('username')
        user = RestManager.objects.get(username=username)
        
        restaurants = Restaurant.objects.filter(managers=user)
        serialized = RestaurantNameIdSerializer(restaurants, many=True)
        return JsonResponse(serialized.data, safe=False)