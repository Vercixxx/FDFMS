from django.urls import path, include
from . import views


urlpatterns = [
    # GetCountries
    path('api/countries/get/', views.GetCountries.as_view(), name="get-countries"),
    
    # GetStates
    path('api/states/get/', views.GetStates.as_view(), name="get-states"),
    
]