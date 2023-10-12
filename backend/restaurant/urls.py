from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"get-restaurants", views.GetRestaurants, basename='get-restaurants')


urlpatterns = [
    # Creating restaurant
    path('api/restaurant/create/', views.CreateRestaurant.as_view(), name="create-restaurant"),
    
    # Deliting restaurant
    path('api/restaurant/delete/<str:name>/', views.DeleteRestaurant.as_view(), name='delete-restaurant'),
    
    # Get restaurants
    path('api/restaurants/', include(router.urls)),
    
    # Get list of possible cities
    path('api/restaurants/unique_cities/', views.GetPossibleCities.as_view(), name='unique-cities'),
]

    