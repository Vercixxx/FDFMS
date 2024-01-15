from django.http import JsonResponse

from .serializers import CarSerializer

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

        errors = [
            f'Given {field} is already taken. Please try another.'
            for field in fields_to_check
            if Car.objects.filter(**{field: data.get(field, None)}).exists()
        ]

        if errors:
            return JsonResponse({'error': ' '.join(errors)}, status=400)
        # Check for unique 

        serializer = CarSerializer(data=data)

        if serializer.is_valid():
            car = serializer.save()
            return JsonResponse({'message' : f'Successfully created car vin - {car.vin}'}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

    

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
        
class GetCar(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, vin):
        car = Car.objects.get(vin=vin)
        serializer = CarSerializer(car)

        return JsonResponse(serializer.data, status=200)
        
        
class EditCar(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, vin):
        data = request.data

        try:
            car = Car.objects.get(vin = vin)
            serializer = CarSerializer(car, data=data)
            
            if serializer.is_valid():
                serializer.save()  
                return JsonResponse({'message' : 'Success'},status=200)
            
            else:
                return JsonResponse(serializer.errors, status=400)
            
        except Car.DoesNotExist:
            return JsonResponse({'error': 'Car does not exist.'}, status=404)
