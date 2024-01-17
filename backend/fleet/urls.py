from django.urls import path, include
from . import views

urlpatterns = [
    # Add Fleet
    path('api/fleet/add/', views.AddFleet.as_view()),
    
    # Get Fleets
    path('api/fleets/get/', views.GetFleets.as_view()),
    
    # Get Fleet
    path('api/fleet/get/', views.GetFleet.as_view()),
    
    # Update Fleet
    path('api/fleet/update/<int:id>/', views.UpdateFleet.as_view()),
    
    # Delete Fleet
    path('api/fleet/delete/<int:id>/', views.DeleteFleet.as_view()),
    
]