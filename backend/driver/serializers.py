from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Driver
from users.models import GeneralUser

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 
                  'username', 
                  'first_name', 
                  'last_name', 
                  'email', 
                  'is_active', 
                  'phone_number', 
                  'country', 
                  'city', 
                  'state', 
                  'user_role', 
                  'zip_code',
                  'license_number',]
        
class AddDriverSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)
    
    class Meta:
        model = Driver
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True,
                         'validators': [validate_password]},
            'username': {'validators': [UniqueValidator(queryset=GeneralUser.objects.all(), message='This username is already in use.')]},
            'email': {'validators': [UniqueValidator(queryset=GeneralUser.objects.all(), message='This email address is already in use.')]}
        }

        
    # My validations
    phone_number = serializers.CharField(
        max_length=20,
    )
    country = serializers.CharField(
        max_length=100,
    )
    city = serializers.CharField(
        max_length=100,
    )
    state = serializers.CharField(
        max_length=100,
    )
    street = serializers.CharField(
        max_length=200,
    )
    home_number = serializers.CharField(
        max_length=10,
    )
    apartament_number = serializers.CharField(
        max_length=10,
    )
    zip_code = serializers.CharField(
        max_length=10,
    )
    license_number = serializers.CharField(
        max_length=50,
    )


    def save(self):
        account = Driver(
            user_role = 'Driver',
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            phone_number = self.validated_data['phone_number'],
            country = self.validated_data['country'],
            city = self.validated_data['city'],
            state = self.validated_data['state'],
            street = self.validated_data['street'],
            home_number = self.validated_data['home_number'],
            apartament_number = self.validated_data['apartament_number'],
            zip_code = self.validated_data['zip_code'],
            license_number = self.validated_data['license_number'], 
        )
    
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        
        account.set_password(password)
        account.save()
        return account
