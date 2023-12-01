from django.urls import path, include
from . import views

urlpatterns = [ 
    # Get posts
    path('api/posts/get/<str:target>/', views.GetPosts.as_view(), name="get-posts"),
    
    # Create post
    path('api/posts/create/<str:target>', views.CreatePost.as_view(), name="create-post"),
    
    # Delete post
    path('api/posts/delete/<int:id>', views.DeletePost.as_view(), name="delete-post"),
    
]