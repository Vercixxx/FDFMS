from django.urls import path

from . import views

urlpatterns = [
    path('get-users/<str:role>/<str:active>/<str:search>/', views.get_users),
    path('add-user/', views.add_user),
    path('remove-user/<str:username>/<str:user_role>/', views.remove_user),
    path('log-in/', views.log_in),
    path('log-out/', views.log_out),
    path('get-token/', views.get_token),
    path('user/', views.get_user_data),
]