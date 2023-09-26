from django.urls import path, include
from . import views

# Rest
from rest_framework.routers import DefaultRouter

car_router = DefaultRouter()
car_router.register(r"get-cars", views.CarsViewSet, basename='get-cars')




urlpatterns = [
    path('api/cars/', include(car_router.urls)),
    
    # Creating car
    path('api/car', views.CarView.as_view(), name="cars"),
    
    # Delete car
    path('api/car/delete/<str:vin>', views.DeleteCar.as_view(), name="delete-cars"),
    
    # Get car info
    path('api/car/edit/<int:id>', views.getCar.as_view(), name="edit-car"),
    # Save car info
    path('api/car/save/<int:id>', views.saveCar.as_view(), name="save-car")
]