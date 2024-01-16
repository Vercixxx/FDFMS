from django.http import JsonResponse

# Rest
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import DestroyAPIView

# DB
from django.db.models import Q

# Models
from .models import Fleet

# Serializers
from .serializers import FleetSerializer


# Add Fleet
class AddFleet(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        data = request.data
        
        serializer = FleetSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Fleet added successfully'}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
# Add Fleet

        
# Fleet Paginator
class FleetPaginator(PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 100

    def get_page_size(self, request):
        page_size = super().get_page_size(request)
        if page_size is None or page_size == 0:
            return self.max_page_size
        return page_size
# Fleet Paginator


# Get Fleets
class GetFleets(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        limit = self.request.query_params.get('limit', '').strip()
        query = self.request.query_params.get('search', '').strip()
        
        queryset = Fleet.objects.all()
        
        if query:
            queryset = queryset.filter(Q(restaurant__name__icontains=query) | Q(cars__name__icontains=query))
            
            
        paginator = FleetPaginator()
        response_page = paginator.paginate_queryset(queryset, request)
        
        serialized_data = [FleetSerializer(fleet).data for fleet in response_page]
            
        response_data = {
            'posts_amount': paginator.page.paginator.count,
            'total_pages': paginator.page.paginator.num_pages,
            'current_page': paginator.page.number,
            'results': serialized_data,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'total_results': queryset.count(),
        }
        return JsonResponse(response_data, status=200)
# Get Fleets

# Get Fleet
class GetFleet(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id):
        try:
            fleet = Fleet.objects.get(id=id)
        except Fleet.DoesNotExist:
            return JsonResponse({'message': 'Fleet not found'}, status=404)
        
        serializer = FleetSerializer(fleet)
        
        return JsonResponse(serializer.data, status=200)
# Get Fleet
    
    
# Update Fleet
class UpdateFleet(APIView):
    permission_classes = (IsAuthenticated,)
    
    def put(self, request, id):
        try:
            fleet = Fleet.objects.get(id=id)
        except Fleet.DoesNotExist:
            return JsonResponse({'message': 'Fleet not found'}, status=404)
        
        data = request.data
        
        serializer = FleetSerializer(fleet, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Fleet updated successfully'}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
# Update Fleet

# Delete Fleet
class DeleteFleet(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer
    lookup_field = 'id'
# Delete Fleet
