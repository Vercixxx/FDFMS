from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Country, State
from .serializers import *


class GetCountries(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        countries = Country.objects.all().order_by('name')
        serialized = CountrySerializer(countries, many=True)
        return JsonResponse(serialized.data, safe=False, status=200)
    
    
class GetStates(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        country = self.request.query_params.get('country', '').strip()
        states = State.objects.filter(country__name=country)
        serialized = StateSerializer(states, many=True)
        return JsonResponse(serialized.data, safe=False, status=200)
    
    
