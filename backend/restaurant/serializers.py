from rest_framework import serializers

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
            'brand',
            'country',
            'city',
            'state',
            'street',
            'home',
            'apartament',
            'zip',
            'managers',
        ]

    def create(self, validated_data):
        managers_data = validated_data.pop('managers', [])

        restaurant = Restaurant.objects.create(**validated_data)
        restaurant.managers.set(managers_data)
        return restaurant


class UpdateRestaurantSerializer(serializers.ModelSerializer):
    managers = serializers.SlugRelatedField(
        many=True,
        queryset=RestManager.objects.all(),
        slug_field='username',
        required=False,
    )

    class Meta:
        model = Restaurant
        fields = [
            'name',
            'phone',
            'brand',
            'country',
            'city',
            'state',
            'street',
            'home',
            'apartament',
            'zip',
            'managers',
        ]

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.street = validated_data.get('street', instance.street)
        instance.home = validated_data.get('home', instance.home)
        instance.apartament = validated_data.get('apartament', instance.apartament)
        instance.zip = validated_data.get('zip', instance.zip)

        instance.brand = Brands.objects.get(pk=validated_data.get('brand'))
                
        managers_data = validated_data.pop('managers', [])

        
        new_manager_ids = [RestManager.objects.get(username=manager_data).id for manager_data in managers_data]
        instance.managers.set(new_manager_ids)

        instance.save()
        return instance



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
class RestaurantSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'city', 'brand_name', 'phone', 'country', 'state', 'street', 'home', 'apartament', 'zip', 'managers']
        
    def get_brand_name(self, obj):
        return obj.brand.name