from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import PayrollUser

from users.models import GeneralUser

class GetPayrollUser(serializers.ModelSerializer):
    class Meta:
        model = PayrollUser
        fields = ['email', 
                  'username', 
                  'first_name', 
                  'last_name', 
                  'is_active', 
                  'user_role', 
                  'phone',
                  'residence_country', 
                  'residence_city', 
                  'residence_state', 
                  'residence_street', 
                  'residence_home_number', 
                  'residence_apartament_number', 
                  'residence_zip_code',
                  'registered_country', 
                  'registered_city', 
                  'registered_state', 
                  'registered_street', 
                  'registered_home_number', 
                  'registered_apartament_number', 
                  'registered_zip_code',
                  'correspondence_country', 
                  'correspondence_city', 
                  'correspondence_state', 
                  'correspondence_street', 
                  'correspondence_home_number', 
                  'correspondence_apartament_number', 
                  'correspondence_zip_code',
                  'bank_account_number',
                  'pesel_nip',
                  'tax_office_name',
                  'tax_office_address',
                  'nfz',
                  ]
        
        
class PayrollUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollUser
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
class AddPayrollUserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)
    
    class Meta:
        model = PayrollUser
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
            'user_role': 'Payroll',
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
        
        account = PayrollUser(**account_data)
    
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        
        account.set_password(password)
        account.save()
        return account


class UpdatePayrollUser(serializers.Serializer):
    class Meta:
        model = PayrollUser
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'phone',
            'residence_country',
            'residence_city',
            'residence_state',
            'residence_street',
            'residence_home_number',
            'residence_apartament_number',
            'residence_zip_code',
            'registered_country',
            'registered_city',
            'registered_state',
            'registered_street',
            'registered_home_number',
            'registered_apartament_number',
            'registered_zip_code',
            'correspondence_country',
            'correspondence_city',
            'correspondence_state',
            'correspondence_street',
            'correspondence_home_number',
            'correspondence_apartament_number',
            'correspondence_zip_code',
            'bank_account_number',
            'pesel_nip',
            'tax_office_name',
            'tax_office_address',
            'nfz',
        ]
        extra_kwargs = {
            'username' : {'validators' : [UniqueValidator(queryset=GeneralUser.objects.all(), message='This username is already in use.')]}
        }
        
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.residence_country = validated_data.get('residence_country', instance.residence_country)
        instance.residence_city = validated_data.get('residence_city', instance.residence_city)
        instance.residence_state = validated_data.get('residence_state', instance.residence_state)
        instance.residence_street = validated_data.get('residence_street', instance.residence_street)
        instance.residence_home_number = validated_data.get('residence_home_number', instance.residence_home_number)
        instance.residence_apartament_number = validated_data.get('residence_apartament_number', instance.residence_apartament_number)
        instance.residence_zip_code = validated_data.get('residence_zip_code', instance.residence_zip_code)
        instance.registered_country = validated_data.get('registered_country', instance.registered_country)
        instance.registered_city = validated_data.get('registered_city', instance.registered_city)
        instance.registered_state = validated_data.get('registered_state', instance.registered_state)
        instance.registered_street = validated_data.get('registered_street', instance.registered_street)
        instance.registered_home_number = validated_data.get('registered_home_number', instance.registered_home_number)
        instance.registered_apartament_number = validated_data.get('registered_apartament_number', instance.registered_apartament_number)
        instance.registered_zip_code = validated_data.get('registered_zip_code', instance.registered_zip_code)
        instance.correspondence_country = validated_data.get('correspondence_country', instance.correspondence_country)
        instance.correspondence_city = validated_data.get('correspondence_city', instance.correspondence_city)
        instance.correspondence_state = validated_data.get('correspondence_state', instance.correspondence_state)
        instance.correspondence_street = validated_data.get('correspondence_street', instance.correspondence_street)
        instance.correspondence_home_number = validated_data.get('correspondence_home_number', instance.correspondence_home_number)
        instance.correspondence_apartament_number = validated_data.get('correspondence_apartament_number', instance.correspondence_apartament_number)
        instance.correspondence_zip_code = validated_data.get('correspondence_zip_code', instance.correspondence_zip_code)
        instance.bank_account_number = validated_data.get('bank_account_number', instance.bank_account_number)
        instance.pesel_nip = validated_data.get('pesel_nip', instance.pesel_nip)
        instance.tax_office_name = validated_data.get('tax_office_name', instance.tax_office_name)
        instance.tax_office_address = validated_data.get('tax_office_address', instance.tax_office_address)
        instance.nfz = validated_data.get('nfz', instance.nfz)
        instance.save()
        return instance