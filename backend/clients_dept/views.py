from rest_framework.response import Response

from django.http import JsonResponse

# Rest
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


# Models
from rest_manager.models import RestManager

# Serializers
from rest_manager.serializers import GetAllManagersUsername

class DisablePagination(PageNumberPagination):
    page_size = None

class GetUsernames(APIView):

    def get(self, request, format=None):
        search_param = request.query_params.get('search', '')
        users = RestManager.objects.filter(username__icontains=search_param)
        serializer = GetAllManagersUsername(users, many=True)

        return Response(serializer.data)