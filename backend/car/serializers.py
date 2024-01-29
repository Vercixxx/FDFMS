from rest_framework import serializers

from .models import Car, CarDailyReports, CarDamage

class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = '__all__'
        
        
class CarVinLicensePlateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = ('vin', 'license_plate')
        
class CarDailyReportsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CarDailyReports
        fields = '__all__'
        

class CarDamageSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = CarDamage
            fields = '__all__'
            

