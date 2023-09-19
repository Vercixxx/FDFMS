from django.shortcuts import render
from django.http import JsonResponse

from .serializers import CarSerializer, CreateCarSerializer, UpdateCarSerializer

from .models import Car

from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated



class CarView(APIView):
    permission_classes = [IsAuthenticated]
    
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
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'vin'
    

    
class CarsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # query
    filter_backends = (filters.SearchFilter, )
    search_fields = ('brand', 'model')


    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        
        self.serializer_class = CarSerializer

        self.queryset = self.serializer_class.Meta.model.objects.all()
        
class getCar(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        car = Car.objects.get(id=id)
        serializer = CarSerializer(car)
        return JsonResponse(serializer.data, status=200)
        
        
        
class saveCar(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, id):
        data = request.data
        car = Car.objects.get(id = id)
        serializer = UpdateCarSerializer(car, data=data)
        
        if serializer.is_valid():
            serializer.update(car, data)  
            return JsonResponse({'message' : 'success'},status=200)
        
        else:
            return JsonResponse(serializer.errors, status=400)
