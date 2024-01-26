from django.urls import path, include
from . import views



urlpatterns = [
    path('api/drivers/get/restaurants/<str:username>/', views.GetRestaurants.as_view(), name='get_restaurants'),
    
    # Get Drivers
    path('api/drivers/get/all/', views.GetDrivers.as_view(), name='get_drivers'),
]