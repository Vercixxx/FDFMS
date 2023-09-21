from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Restaurant
from rest_manager.models import RestManager

class CreateRestaurantSerializer(serializers.ModelSerializer):
    
    managers = serializers.SlugRelatedField(
    many=True,
    queryset=RestManager.objects.all(),
    slug_field='username',
    )
    class Meta:
        model = Restaurant
        fields = [
                  'name', 
                  'phone', 
                  'country', 
                  'city', 
                  'state', 
                  'street', 
                  'home_number', 
                  'apartament_number', 
                  'zip_code', 
                  'managers', 
                  ]
        extra_kwargs = {
            'name': {'validators': [UniqueValidator(queryset=Restaurant.objects.all(), message='This name is already in use.')]}
        }
        
    def create(self, validated_data):
        managers_data = validated_data.pop('managers', [])
        
        restaurant = Restaurant.objects.create(**validated_data)
        restaurant.managers.set(managers_data)
        return restaurant
    
    
class GetAllRestaurants(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


