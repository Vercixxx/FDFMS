from rest_framework import serializers

from .models import Car, CarDailyReports

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
