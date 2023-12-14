from django.urls import path, include
from . import views

urlpatterns = [ 
    path('api/messages/get/', views.GetMessages.as_view(), name="get-messages"),

]