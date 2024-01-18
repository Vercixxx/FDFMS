from rest_framework import serializers

from .models import Restaurant, Brands
from rest_manager.models import RestManager


class GetAllRestaurants(serializers.ModelSerializer):

    managers = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = '__all__'

    def get_managers(self, obj):
        return [manager.username for manager in obj.managers.all()]

    def get_brand(self, obj):
        return obj.brand.name




# Brand serializers
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'
        
     
# Restaurant serializers   
class RestaurantInfoSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'city', 'brand_name', 'phone', 'country', 'state', 'street', 'home', 'apartament', 'zip', 'managers', 'drivers']
        
    def get_brand_name(self, obj):
        return obj.brand.name
    
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
        
class RestaurantNameIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']