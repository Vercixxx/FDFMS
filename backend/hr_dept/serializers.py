from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import HRUser
from users.models import GeneralUser

class HRUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRUser
        fields = ['email', 'first_name', 'id', 'is_active', 'last_name', 'test_field', 'user_role', 'username', 'test_field']
        
class AddHRUserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)
    
    class Meta:
        model = HRUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True,
                         'validators': [validate_password]},
            'username': {'validators': [UniqueValidator(queryset=GeneralUser.objects.all(), message='This username is already in use.')]},
            'email': {'validators': [UniqueValidator(queryset=GeneralUser.objects.all(), message='This email address is already in use.')]}
        }


    def save(self):
        account = HRUser(
            user_role = 'HR',
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            test_field = self.validated_data['test_field'],  #Temporary 
        )
    
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        
        
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        
        account.set_password(password)
        account.save()
        return account

