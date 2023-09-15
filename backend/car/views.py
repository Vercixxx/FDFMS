from django.shortcuts import render
from django.http import JsonResponse

from .serializers import CarSerializer, CreateCarSerializer

from .models import Car

from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView



class CarView(APIView):
    def post(self, request):
        serializer = CreateCarSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message' : 'Success'})
        else:
            return JsonResponse(serializer.errors)
        
    def get(self, request):
        serializer = CarSerializer
        return JsonResponse(serializer)
    

class DeleteCar(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'vin'
    

    # print(lookup_field)
    
class CarsViewSet(viewsets.ModelViewSet):
    # query
    filter_backends = (filters.SearchFilter, )
    search_fields = ('brand', 'model')


    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        
        self.serializer_class = CarSerializer

        self.queryset = self.serializer_class.Meta.model.objects.all()