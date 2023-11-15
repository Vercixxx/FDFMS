from django.urls import path, include
from . import views

urlpatterns = [ 
    # Get posts
    path('api/posts/get/', views.getPosts.as_view(), name="get-posts"),
    
    # Create posts
    path('api/posts/create/<str:target>', views.CreatePost.as_view(), name="create-post"),
]