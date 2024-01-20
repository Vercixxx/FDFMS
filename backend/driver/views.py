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

# DB
from django.db.models import Q


class GetRestaurants(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        driver = Driver.objects.get(username=username)
        restaurants = Restaurant.objects.filter(drivers=driver)
        result = {}


        for restaurant in restaurants:
            fleets = Fleet.objects.filter(restaurant=restaurant)
            result[restaurant.name] = [car.license_plate for fleet in fleets for car in fleet.cars.all()]

        return JsonResponse(result, safe=False)
