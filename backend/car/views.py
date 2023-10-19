from django.shortcuts import render
from django.http import JsonResponse

from .serializers import CarSerializer, CreateCarSerializer, UpdateCarSerializer

from .models import Car

from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated



class AddCar(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data=request.data
        
        # Check for unique 
        fields_to_check = ['vin']

        for field_name in fields_to_check:
            if field_name in data:
                field_value = data[field_name]

                duplicate_exists = Car.objects.filter(**{field_name: field_value}).exists()
                if duplicate_exists:
                    return JsonResponse({'error': f'Given {field_name} is already taken. Please try another.'}, status=400) 
        

        serializer = CreateCarSerializer(data=data)

        if serializer.is_valid():
            car = serializer.save()
            return JsonResponse({'message' : f'Successfully created car vin - {car.vin}'}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
        
    def get(self, request):
        serializer = CarSerializer
        return JsonResponse(serializer)
    

class DeleteCar(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'
    
    
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
        
        
class EditCar(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, id):
        data = request.data

        try:
            car = Car.objects.get(id=id)

            fields_to_check = ['vin']

            for field_name in fields_to_check:
                if field_name in data:
                    field_value = data[field_name]


                    if field_value != getattr(car, field_name) and Car.objects.exclude(id=id).filter(**{field_name: field_value}).exists():
                        return JsonResponse({'error': f'Given {field_name} is already taken. Please try another.'}, status=400) 
        
        
            car = Car.objects.get(id = id)
            serializer = UpdateCarSerializer(car, data=data)
            
            if serializer.is_valid():
                serializer.update(car, data)  
                return JsonResponse({'message' : 'Success'},status=200)
            
            else:
                return JsonResponse(serializer.errors, status=400)
            
        except Car.DoesNotExist:
            return JsonResponse({'error': 'Samochód o podanym ID nie istnieje.'}, status=404)
