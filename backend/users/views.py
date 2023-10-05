
# Auth
from django.contrib.auth import authenticate, get_user_model

# Password 
import secrets
import string


from django.http import JsonResponse


from .serializers import GeneralUserSerializer, GeneralUserRegistrationSerializer
from owner.serializers import AddOwnerSerializer
from rest_manager.serializers import AddManagerSerializer, RestManagerSerializer, GetRestManager, UpdateRestManager
from asset_dept.serializers import AddAssetUserSerializer, AssetSerializer, GetAssetUser, UpdateAssetUser
from clients_dept.serializers import AddClientsUserSerializer, GetClientsUser, UpdateClientsUser
from hr_dept.serializers import AddHRUserSerializer, HRUserSerializer, GetHRUser, UpdateHRUser
from payroll_dept.serializers import AddPayrollUserSerializer, PayrollUser, GetPayrollUser, UpdatePayrollUser
from driver.serializers import AddDriverSerializer, DriverSerializer, GetDriver, UpdateDriverUser
from administrator.serializers import AddAdministratorSerializer, AdministratorSerializer, GetAdministrator, UpdateAdministrator

# Rest API
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView

# JWT
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings

# Models
from .models import GeneralUser
from owner.models import Owner
from rest_manager.models import RestManager
from asset_dept.models import AssetUser
from clients_dept.models import ClientsUser
from hr_dept.models import HRUser
from payroll_dept.models import PayrollUser
from driver.models import Driver
from administrator.models import Administrator


class GlobalDictionaries:
    dicts = {
        'UserModels': {
            'Owner': Owner,
            'Manager': RestManager,
            'Asset': AssetUser,
            'Clients': ClientsUser,
            'HR': HRUser,
            'Payroll': PayrollUser,
            'Driver': Driver,
            'Administrator': Administrator,
        },
        
        'AddUserSerializers': {
            'Owner' : AddOwnerSerializer,
            'Manager' : AddManagerSerializer,
            'Asset' : AddAssetUserSerializer,
            'Clients' : AddClientsUserSerializer,
            'HR' : AddHRUserSerializer,
            'Payroll' : AddPayrollUserSerializer,
            'Driver' : AddDriverSerializer,
            'Administrator' : AddAdministratorSerializer,
        },
        
        'UserSerializers': {
            'Manager' : RestManagerSerializer,
            'Asset' : AssetSerializer,
            'Clients' : AddClientsUserSerializer,
            'HR' : HRUserSerializer,
            'Payroll' : AddPayrollUserSerializer,
            'Driver' : DriverSerializer,
            'Administrator' : AdministratorSerializer,
        },
        
        'GetUserSerializers': {
            'Manager': GetRestManager,
            'Asset': GetAssetUser,
            'Clients': GetClientsUser,
            'HR': GetHRUser,
            'Payroll': GetPayrollUser,
            'Driver': GetDriver,
            'Administrator': GetAdministrator,
        },
        
        'UpdateUserSerializers': {
            'Asset': UpdateAssetUser,
            'Manager': UpdateRestManager,
        }
    }
        
    @staticmethod
    def get_serializer(name, key):
        dictionary = GlobalDictionaries.dicts.get(name)
        if dictionary:
            return dictionary.get(key)
            
      
  

class GUViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    # query
    filter_backends = (filters.SearchFilter, )
    search_fields = ('username', 'email')


    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        
        # Choosing correct serializer
        role = self.request.query_params.get('role')

        serializer_class = GlobalDictionaries.get_serializer('UserSerializers', role)
        self.serializer_class = serializer_class if serializer_class else GeneralUserSerializer
        
        
        status = self.request.query_params.get('status')
        self.queryset = self.serializer_class.Meta.model.objects.all()
        
        # Filtering by status
        if status == 'True':
            self.queryset = self.queryset.filter(is_active=True)
        elif status == 'False':
            self.queryset = self.queryset.filter(is_active=False)

        
        
    
    def get_users(self, request):
        serializer = GeneralUserSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    
class DeleteUser(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = GeneralUser.objects.all()
    serializer_class = GeneralUserSerializer
    lookup_field = 'username'
  
    
class UserAuth(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
 
        general_user = authenticate(username=username, password=password)
        
        if general_user is not None:

            user_role = general_user.user_role

            user_model = GlobalDictionaries.get_serializer('UserModels', user_role)
            logged_user = user_model.objects.get(id=general_user.id)
            
            serializer_class = GlobalDictionaries.get_serializer('UserSerializers', user_role)

            serializer = serializer_class(logged_user)
            user_data = serializer.data
            
            jwt = self.get_tokens_for_user(logged_user)
            

            return JsonResponse({'message': 'Logged in successfully', 'user_role':logged_user.user_role, 'data':user_data , 'jwt':jwt})
        
        else:
            return JsonResponse({'error': 'Invalid username or password'})

    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class AddUser(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user_role = request.data.get('user_role')
        
        # Password generating
        generated_password = self.generate_password()
        request.data['password'] = generated_password
        request.data['password2'] = generated_password

        serializer_class = GlobalDictionaries.get_serializer('AddUserSerializers', user_role) 

        serializer = serializer_class(data=request.data)
        data = {}
        

        
        if serializer.is_valid():
            account = serializer.save()
            data['message'] = 'Succesfully registered a new User'
            data['username'] = account.username
            
            # user_model = account.__class__
            # user = user_model.objects.get(username=account.username)
            
            print("Created ", account.username, " with password: ", generated_password)
            
        
        else:
            data = serializer.errors
            
        return JsonResponse(data)
    
    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(8))
        return password
    

class getUser(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, username, user_role):


        user_model = GlobalDictionaries.get_serializer('UserModels', user_role)
        user = user_model.objects.get(username = username)
        
        
        user_serializer = GlobalDictionaries.get_serializer('GetUserSerializers', user_role)
        serializer_instance  = user_serializer(user)
        output = serializer_instance.data
        return JsonResponse(output, status=200, safe=False)

    
class UpdateUser(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, username, user_role):
        data = request.data
        

        user_model = GlobalDictionaries.get_serializer('UserModels', user_role)
        user = user_model.objects.get(username = username)
    
        
        serializer_class = GlobalDictionaries.get_serializer('UpdateUserSerializers', user_role)
        serializer = serializer_class(user, data=data)
        
        if serializer.is_valid():
            serializer.update(user, data)  
            return JsonResponse({'message' : 'success'},status=200)
        
        else:
            return JsonResponse(serializer.errors, status=400)
            

class ChangeUserState(APIView):
    def put(self, request, username):
        user = GeneralUser.objects.get(username = username)
        user.is_active = not user.is_active
        user.save()
        return JsonResponse({'message' : 'Changed successfully'}, status=200)
    
    
    
class GetAllCountries(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(safe, request):
        countries = [choice[0] for choice in GeneralUser.COUNTRY_CHOICES]
        return JsonResponse(countries, safe=False)
    
class GetCities(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(safe, request, selected_country):
        if(selected_country == "Poland"):
            countries = [choice[0] for choice in GeneralUser.POLAND_STATE_CHOICES]
            
        return JsonResponse(countries, safe=False)