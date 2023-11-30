from django.http import JsonResponse

# Pagination
from rest_framework.pagination import PageNumberPagination

# Serializers
from .serializers import GetPostsSerializer, CreatePostSerializer, CreateDriverPostSerializer, GetDriverPostsSerializer

# Models
from .models import Posts, DriverPosts

# Rest
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

class CustomPostsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class GetPosts(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPostsPagination
    
    def get(self, request, target):
        if target == "Users":
            posts = Posts.objects.all().order_by('-posted_date')
            paginator = CustomPostsPagination()
            result_page = paginator.paginate_queryset(posts, request)
            serializer = GetPostsSerializer(result_page, many=True)
            
        else:
            posts = DriverPosts.objects.all().order_by('-posted_date')
            paginator = CustomPostsPagination()
            result_page = paginator.paginate_queryset(posts, request)
            serializer = GetDriverPostsSerializer(result_page, many=True)
        
        response_data = {
            'posts_amount': paginator.page.paginator.count,
            'total_pages': paginator.page.paginator.num_pages,
            'results': serializer.data,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
        }

        return JsonResponse(response_data, status=200)
    
    
class CreatePost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, target):
        data = request.data
        
        if target == "Users":
            serializer = CreatePostSerializer(data=data)
        else:
            serializer = CreateDriverPostSerializer(data=data)
            
        if serializer.is_valid():
            serializer.save()

            return JsonResponse({'message': 'Post created successfully'}, status=201)
        else:
            return JsonResponse({'errors': serializer.errors}, status=400)  
        
        
class DeletePost(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Posts.objects.all()
    serializer_class = GetPostsSerializer
    lookup_field = 'id'