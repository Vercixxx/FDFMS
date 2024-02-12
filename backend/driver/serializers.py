from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Driver, DailyWork, WageTariff
from users.models import GeneralUser

from users.serializers import GetAddressesSerializer


class GetDriver(serializers.ModelSerializer):
    wage_tariff = serializers.StringRelatedField()
    class Meta:
        model = Driver
        fields = ['email',
                  'username',
                  'first_name',
                  'last_name',
                  'is_active',
                  'user_role',
                  'phone',
                  'bank_account_number',
                  'pesel_nip',
                  'tax_office_name',
                  'tax_office_address',
                  'nfz',
                  'license_number',
                  'ln_release_date',
                  'ln_expire_date',
                  'ln_published_by',
                  'ln_code',
                  'wage_tariff',
                  ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        addresses_serializer = GetAddressesSerializer()
        for field_name, _ in addresses_serializer.fields.items():
            source_field = f'addresses.{field_name}'
            self.fields[field_name] = serializers.CharField(
                source=source_field)


class DriverSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d')
    wage_tariff = serializers.StringRelatedField()

    class Meta:
        model = Driver
        fields = ['email',
                  'first_name',
                  'is_active',
                  'last_name',
                  'user_role',
                  'username',
                  'phone',
                  'date_joined',
                  'wage_tariff',
                  ]


class RestaurantDriversSerliazer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(read_only=True)
    date_joined = serializers.DateTimeField(format='%Y-%m-%d')
    wage_tariff = serializers.StringRelatedField()

    class Meta:
        model = Driver
        fields = ['email',
                  'first_name',
                  'is_active',
                  'last_name',
                  'user_role',
                  'username',
                  'phone',
                  'date_joined',
                  'restaurant_name',
                  'wage_tariff',
                  ]

class DriverUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['username', 'first_name', 'last_name']


class AddDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class UpdateDriverUser(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'phone',
            'bank_account_number',
            'pesel_nip',
            'tax_office_name',
            'tax_office_address',
            'nfz',
            'license_number',
            'ln_release_date',
            'ln_expire_date',
            'ln_published_by',
            'ln_code',
            'wage_tariff',
        ]


class DailyDriverReportSerializer(serializers.ModelSerializer):
    start_work = serializers.TimeField(format='%H:%M')
    end_work = serializers.TimeField(format='%H:%M')
    working_time = serializers.TimeField(format='%H:%M')

    class Meta:
        model = DailyWork
        fields = ['id','driver', 'date', 'orders', 'start_work', 'end_work', 'working_time', 'orders_per_hour']
        

class WageTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = WageTariff
        fields = '__all__'
        
class WageTariffGetIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = WageTariff
        fields = ['id']