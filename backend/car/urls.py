from django.urls import path, include
from . import views


urlpatterns = [
    # path('api/cars/', include(car_router.urls)),
    
    # Get Cars
    path('api/car/getall/', views.GetCars.as_view(), name="get-cars"),
    
    # Creating car
    path('api/car/create/', views.AddCar.as_view(), name="add-cars"),
    
    # Delete car
    path('api/car/delete/<int:vin>/', views.DeleteCar.as_view(), name="delete-car"),
    
    # Get car info
    path('api/car/get/<int:vin>/', views.GetCar.as_view(), name="get-car"),
    
    # Edit car
    path('api/car/edit/<int:vin>/', views.EditCar.as_view(), name="edit-car")
]