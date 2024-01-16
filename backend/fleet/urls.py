from django.urls import path, include
from . import views

urlpatterns = [
    # Add Fleet
    path('add/', views.AddFleet.as_view()),
    
    # Get Fleets
    path('get/', views.GetFleets.as_view()),
    
    # Get Fleet
    path('get/<int:pk>/', views.GetFleet.as_view()),
    
    # Update Fleet
    path('update/<int:pk>/', views.UpdateFleet.as_view()),
    
    # Delete Fleet
    path('delete/<int:pk>/', views.DeleteFleet.as_view()),
    
]