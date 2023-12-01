from rest_framework import serializers

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
    
    
class UpdateCarSerializer(serializers.Serializer):
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

    def update(self, instance, validated_data):
        instance.vin = validated_data.get('vin', instance.vin)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.model = validated_data.get('model', instance.model)
        instance.year_of_prod = validated_data.get('year_of_prod', instance.year_of_prod)
        instance.color = validated_data.get('color', instance.color)
        instance.mileage = validated_data.get('mileage', instance.mileage)
        instance.engine_cap = validated_data.get('engine_cap', instance.engine_cap)
        instance.engine_pow = validated_data.get('engine_pow', instance.engine_pow)
        instance.transmission = validated_data.get('transmission', instance.transmission)
        instance.policy_number = validated_data.get('policy_number', instance.policy_number)
        instance.is_oc = validated_data.get('is_oc', instance.is_oc)
        instance.is_ac = validated_data.get('is_ac', instance.is_ac)
        instance.phone_policy_contact = validated_data.get('phone_policy_contact', instance.phone_policy_contact)

        instance.save()
        return instance







