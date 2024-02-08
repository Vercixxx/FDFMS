from django.urls import path, include
from . import views



urlpatterns = [
    path('api/drivers/get/restaurants/<str:username>/', views.GetRestaurants.as_view(), name='get_restaurants'),
    
    # Get Drivers
    path('api/drivers/get/all/', views.GetDrivers.as_view(), name='get_drivers'),
    
    # Get Drivers usernames
    path('api/drivers/get/usernames/', views.GetDriversUsernames.as_view(), name='get_drivers_usernames'),
    
    # Daily report
    path('api/drivers/daily_report/add/', views.AddDailyReport.as_view(), name='add_daily_report'),
    
    # Genre report
    path('api/drivers/generate_report/<str:username>/', views.GenerateReport.as_view(), name='generate_report'),
    
    
    # WageTariff
    
    # Create WageTariff
    path('api/drivers/wage_tariff/create/', views.CreateWageTariff.as_view(), name='create_wage_tariff'),
    
    # Get WageTariffs
    path('api/drivers/wage_tariff/get/all/', views.GetWageTariffs.as_view(), name='get_wage_tariffs'),
    
    # Edit WageTariff
    path('api/drivers/wage_tariff/edit/<int:pk>/', views.EditWageTariff.as_view(), name='edit_wage_tariff'),
    
]