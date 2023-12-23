from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import GeneralUser


class GeneralUserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = GeneralUser
        fields = ['username', 'email' , 'user_role', 'is_active', 'date_joined']
        
class GeneralUserRegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)
    
    class Meta:
        model = GeneralUser
        fields = ['username', 
                  'password', 
                  'password2', 
                  'email' , 
                  'phone' , 
                  'country' , 
                  'city' , 
                  'state' , 
                  'street' , 
                  'home_number' , 
                  'apartament_number' , 
                  'zip_code' ]
        extra_kwargs = {
            'password': {'write_only': True,
                         'validators': [validate_password]},
            'username': {'validators': [UniqueValidator(queryset=GeneralUser.objects.all(), message='This username is already in use.')]},
            'email': {'validators': [UniqueValidator(queryset=GeneralUser.objects.all(), message='This email address is already in use.')]}
        }


    def save(self):
        account = GeneralUser(
            user_role = self.validated_data['user_role'],
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            phone = self.validated_data['phone'],
            country = self.validated_data['country'],
            city = self.validated_data['city'],
            state = self.validated_data['state'],
            street = self.validated_data['street'],
            home_number = self.validated_data['home_number'],
            apartament_number = self.validated_data['apartament_number'],
            zip_code = self.validated_data['zip_code'],
        )
    
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        
        account.set_password(password)
        account.save()
        return account

class GetAllUsernamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralUser
        fields = ['username']
        