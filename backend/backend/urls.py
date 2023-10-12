from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('car.urls')),
    path('', include('clients_dept.urls')),
    path('', include('restaurant.urls')),
    
]
