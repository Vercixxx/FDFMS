from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Car

class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = '__all__'
        
        
        
class CreateCarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = [
            'vin',
            'brand',
            'model',
            'year_of_prod',
            'color',
            'mileage',
            'engine_cap',
            'engine_pow',
            'transmission',
            'policy_number',
            'is_oc',
            'is_ac',
            'phone_policy_contact',
        ]
        extra_kwargs = {
            'vin' : {'validators' : [UniqueValidator(queryset=Car.objects.all(), message='This vin number is already in use.')]}
        }
        
    def save(self):
        request_data = self.initial_data 
        form_data = {
            'vin': self.validated_data.get('vin', None),
            'brand': self.validated_data.get('brand', None),
            'model': self.validated_data.get('model', None),
            'year_of_prod': self.validated_data.get('year_of_prod', None),
            'color': self.validated_data.get('color', None),
            'mileage': request_data.get('mileage', None),
            'engine_cap': request_data.get('engine_cap', None),
            'engine_pow': request_data.get('engine_pow', None),
            'transmission': request_data.get('transmission', None),
            'policy_number': request_data.get('policy_number', None),
            'is_oc': request_data.get('is_oc', None),
            'is_ac': request_data.get('is_ac', None),
            'phone_policy_contact': request_data.get('phone_policy_contact', None),
        }
        
        car_obj = Car(**form_data)
    

        car_obj.save()
        return car_obj