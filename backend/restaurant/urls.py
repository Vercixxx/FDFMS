from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # Creating restaurant
    path('api/restaurant/create/', views.CreateRestaurant.as_view(), name="create-restaurant"),
    
    # Updating restaurant
    path('api/restaurant/update/<str:name>/', views.UpdateRestaurant.as_view(), name="update-restaurant"),
    
    # Deliting restaurant
    path('api/restaurant/delete/<int:id>/', views.DeleteRestaurant.as_view(), name='delete-restaurant'),
    
    # Get restaurants
    path('api/restaurants/get/<str:city>/', views.GetRestaurants.as_view(), name='get-restaurants'),
    
    # Get restaurant
    path('api/restaurant/get/<int:id>/', views.GetRestaurant.as_view(), name='get-restaurant'),
    
    # Get list of possible cities
    path('api/restaurants/unique_cities/', views.GetPossibleCities.as_view(), name='unique-cities'),
    
    
    # Brands Brands Brands
    
    # Creating Brand
    path('api/brands/create/', views.CreateBrand.as_view(), name="create-brand"),
    
    # Getting all brands
    path('api/brands/get-all/', views.GetBrands.as_view(), name='get-all-brands'),
    
    # Getting brand info
    path('api/brands/get-info/<int:id>/', views.GetBrands.as_view(), name='get-existing-brands'),
    
    # Deleting brand
    path('api/brands/delete/<int:id>/', views.DeleteBrands.as_view(), name='delete-brand'),
    
    # Updating Brand
    path('api/brands/update/<int:brandID>/', views.UpdateBrand.as_view(), name='update-brand')
]

    