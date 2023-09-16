from django.urls import path, include
from . import views

# Rest
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"get-gu", views.GUViewSet, basename='get-gu')




urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/gu/', views.GeneralUser.as_view(), name="gu"),
    
    # Logging
    
    # Creating account
    path('api/create/', views.AddUser.as_view(), name="add-user"),
    
    # Deliting account
    path('api/users/delete/<str:username>/', views.DeleteUser.as_view(), name='delete_user'),
    
    
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    
    path('api/v1/login/', views.UserAuth.as_view(), name='login'),
    



]