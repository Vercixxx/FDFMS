from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import AssetUser
from users.models import GeneralUser

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetUser
        fields = ['email', 
                  'first_name', 
                  'id', 
                  'is_active', 
                  'last_name', 
                  'user_role', 
                  'username', 
                  'phone' ,
                  'residence_country', 
                  'residence_city', 
                  'residence_state', 
                  'residence_street', 
                  'residence_home_number', 
                  'residence_apartament_number', 
                  'residence_zip_code']


class AddAssetUserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)
    
    class Meta:
        model = AssetUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True,
                         'validators': [validate_password]},
            'username': {'validators': [UniqueValidator(queryset=GeneralUser.objects.all(), message='This username is already in use.')]},
            'email': {'validators': [UniqueValidator(queryset=GeneralUser.objects.all(), message='This email address is already in use.')]}
        }


    def save(self):
        request_data = self.initial_data 
        account_data = {
            'user_role': 'Asset',
            'email': self.validated_data.get('email', None),
            'username': self.validated_data.get('username', None),
            'first_name': self.validated_data.get('first_name', None),
            'last_name': self.validated_data.get('last_name', None),
            'phone': self.validated_data.get('phone', None),
            'residence_country': request_data.get('residence_country', None),
            'residence_city': request_data.get('residence_city', None),
            'residence_state': request_data.get('residence_state', None),
            'residence_street': request_data.get('residence_street', None),
            'residence_home_number': request_data.get('residence_home_number', None),
            'residence_apartament_number': request_data.get('residence_apartament_number', None),
            'residence_zip_code': request_data.get('residence_zip_code', None),
            'registered_country': request_data.get('registered_country', None),
            'registered_city': request_data.get('registered_city', None),
            'registered_state': request_data.get('registered_state', None),
            'registered_street': request_data.get('registered_street', None),
            'registered_home_number': request_data.get('registered_home_number', None),
            'registered_apartament_number': request_data.get('registered_apartament_number', None),
            'registered_zip_code': request_data.get('registered_zip_code', None),
            'correspondence_country': request_data.get('correspondence_country', None),
            'correspondence_city': request_data.get('correspondence_city', None),
            'correspondence_state': request_data.get('correspondence_state', None),
            'correspondence_street': request_data.get('correspondence_street', None),
            'correspondence_home_number': request_data.get('correspondence_home_number', None),
            'correspondence_apartament_number': request_data.get('correspondence_apartament_number', None),
            'correspondence_zip_code': request_data.get('correspondence_zip_code', None),
            'bank_account_number': request_data.get('bank_account_number', None),
            'pesel_nip': request_data.get('pesel_nip', None),
            'tax_office_name': request_data.get('tax_office_name', None),
            'tax_office_address': request_data.get('tax_office_address', None),
            'nfz': request_data.get('nfz', None),
        }
        
        account = AssetUser(**account_data)
    
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        
        account.set_password(password)
        account.save()
        return account
