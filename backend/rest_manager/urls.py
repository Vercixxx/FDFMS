from django.urls import path

from . import views

urlpatterns = [
    # Get restaurants
    path('api/rest_manager/get_restaurants/', views.GetRestaurants.as_view()),
]