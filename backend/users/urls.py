from django.urls import path

from . import views

urlpatterns = [
    path('get-users/', views.getUsers),
    path('create-user/', views.createUser),
    path('gu-log-in/', views.generalLogIn),
    path('gu-log-out/', views.generalLogOut),
    path('get-token/', views.get_token),
]