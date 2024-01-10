from django.urls import path, include
from . import views


urlpatterns = [
    # Countries
    
    # Add Country
    path('api/countries/add/', views.AddCountry.as_view(), name="add-country"),
    
    # Delete Country
    path('api/countries/delete/<str:name>/', views.DeleteCountry.as_view(), name="delete-country"),
    
    # Edit Country
    path('api/countries/edit/<str:name>/', views.EditCountry.as_view(), name="edit-country"),
    
    # GetCountries
    path('api/countries/get/', views.GetCountries.as_view(), name="get-countries"),
    
    
    # Countries
    
    # GetStates
    path('api/states/get/', views.GetStates.as_view(), name="get-states"),
    
]