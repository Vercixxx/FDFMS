from django.urls import path, include
from . import views

# Rest
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"get-gu", views.GUViewSet, basename='get-gu')




urlpatterns = [
    path('api/', include(router.urls)),
    
    # Creating account
    path('api/create/', views.AddUser.as_view(), name="add-user"),
    
    # Deliting account
    path('api/users/delete/<str:username>/', views.DeleteUser.as_view(), name='delete_user'),
    
    # Modify user
    path('api/users/update/<str:username>/<str:user_role>/', views.UpdateUser.as_view(), name='update-user'),
    
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    
    # Logging
    path('api/v1/login/', views.UserAuth.as_view(), name='login'),
    
    # Get User data
    path('api/users/get/<str:username>/<str:user_role>/', views.getUser.as_view(), name="get-user"),
    
    # Save User data
    path('api/users/save/<str:username>/<str:user_role>/', views.UpdateUser.as_view(), name="save-user")
    
    



]