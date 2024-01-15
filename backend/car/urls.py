from django.urls import path, include
from . import views

# Rest
from rest_framework.routers import DefaultRouter

car_router = DefaultRouter()
car_router.register(r"get-cars", views.CarsViewSet, basename='get-cars')




urlpatterns = [
    path('api/cars/', include(car_router.urls)),
    
    # Creating car
    path('api/car/create/', views.AddCar.as_view(), name="add-cars"),
    
    # Delete car
    path('api/car/delete/<int:vin>', views.DeleteCar.as_view(), name="delete-cars"),
    
    # Get car info
    path('api/car/get/<int:vin>/', views.GetCar.as_view(), name="get-car"),
    
    # Edit car
    path('api/car/edit/<int:vin>/', views.EditCar.as_view(), name="edit-car")
]