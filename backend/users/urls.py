from django.urls import path, include
from . import views

# Rest
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"get-gu", views.GUViewSet)




urlpatterns = [
    path('api/', include(router.urls)),
    path('api/gu/', views.GeneralUser.as_view(), name="gu"),
    
    # Logging
    path('api/auth/', views.UserAuth.as_view(), name="auth"),
    
    
    path('get-users/<str:role>/<str:active>/<str:search>/', views.get_users),
    path('add-user/', views.add_user),
    # path('remove-user/<str:username>/<str:user_role>/', views.remove_user),
    path('get-token/', views.get_token),

]