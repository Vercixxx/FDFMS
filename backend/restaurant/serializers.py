from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Restaurant, Brands
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






# Brand serializers
class CreateBrandSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Brands
        fields = '__all__'
        
    def save(self):
        request_data = self.initial_data
        brand_data = {
            'name': self.validated_data.get('name', None),
            'phone': self.validated_data.get('phone', None),
            'country': request_data.get('country', None),
            'city': request_data.get('city', None),
            'state': request_data.get('state', None),
            'street': request_data.get('street', None),
            'home': request_data.get('home', None),
            'apartament': request_data.get('apartament', None),
            'zip': request_data.get('zip', None),

        }
        
        brand = Brands(**brand_data)
        brand.save()
        return brand
    
    
    


#Get brands
class GetBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'
# Brand serializers