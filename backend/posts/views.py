from django.http import JsonResponse

# Serializers
from .serializers import getPostsSerializer

# Models
from .models import Posts

# Rest
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated


class getPosts(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        posts = Posts.objects.all()
        serializer = getPostsSerializer(posts, many=True)
        
        return JsonResponse(serializer.data, safe=False, status=200)
