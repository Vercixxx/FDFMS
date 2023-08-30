from django.urls import path

from . import views

urlpatterns = [
    path('get-users/', views.get_users),
    path('add-user/', views.add_user),
    path('log-in/', views.log_in),
    path('log-out/', views.log_out),
    path('get-token/', views.get_token),
]