from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import AssetUser
from users.models import GeneralUser


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
        account = AssetUser(
            user_role = 'Asset',
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
