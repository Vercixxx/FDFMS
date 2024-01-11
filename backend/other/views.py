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

        output = []
        if country:
            states = State.objects.filter(country__name=country)
            serialized = StateSerializer(states, many=True)
            output = serialized.data

        else:
            states = State.objects.all().order_by('name')
            serialized = StateSerializer(states, many=True)
            output = serialized.data

        return JsonResponse(output, safe=False, status=200)


class AddCountry(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        name = self.request.data['name'].strip()

        if name:
            if Country.objects.filter(name=name).exists():
                return JsonResponse({'error': 'Country already exists'}, safe=False, status=400)
            country = Country.objects.create(name=name)
            return JsonResponse({'message': 'Ok'}, status=201)

        return JsonResponse({'error': 'Country name is required'}, safe=False, status=400)

class DeleteCountry(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, name):
        name = name.strip()

        if name:
            country = Country.objects.get(name=name)
            country.delete()
            return JsonResponse({'message': 'Ok'}, status=201)
        
        return JsonResponse({'error': 'Country name is required'}, safe=False, status=400)
    
class EditCountry(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, name):
        name = name.strip()

        if name:
            country = Country.objects.get(name=name)
            country.name = self.request.data['name'].strip()
            country.save()
            return JsonResponse({'message': 'Ok'}, status=200)
        else:
            return JsonResponse({'error': 'Country name is required'}, safe=False, status=400)