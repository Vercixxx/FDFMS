
# Auth
from django.contrib.auth import authenticate, get_user_model, login, logout

# Password Auth
from django.shortcuts import get_object_or_404, render


from django.http import JsonResponse


from .serializers import GeneralUserSerializer, GeneralUserRegistrationSerializer
from owner.serializers import AddOwnerSerializer
from rest_manager.serializers import AddManagerSerializer
from asset_dept.serializers import AddAssetUserSerializer, AssetSerializer
from clients_dept.serializers import AddClientsUserSerializer
from hr_dept.serializers import AddHRUserSerializer, HRUserSerializer
from payroll_dept.serializers import AddPayrollUserSerializer
from driver.serializers import AddDriverSerializer, DriverSerializer
from administrator.serializers import AddAdministratorSerializer

# Rest API
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView

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
from django.db.models import Q


class GUViewSet(viewsets.ModelViewSet):
    # query
    filter_backends = (filters.SearchFilter, )
    search_fields = ('username', 'email')


    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        
        # Choosing correct serializer
        role = self.request.query_params.get('role')
        
        available_serializers = {
            'HR': HRUserSerializer,
            'Driver': DriverSerializer,
            'Asset': AssetSerializer,
        }
        
        serializer_class = available_serializers.get(role, GeneralUserSerializer)
        
        self.serializer_class = serializer_class
        
        
        status = self.request.query_params.get('status')
        self.queryset = serializer_class.Meta.model.objects.all()
        
        # Filtering by status
        if status == 'True':
            self.queryset = self.queryset.filter(is_active=True)
        elif status == 'False':
            self.queryset = self.queryset.filter(is_active=False)

        
        
    
    def get_users(self, request):
        serializer = GeneralUserSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    
    # authentication_classes = [SessionAuthentication, TokenAuthentication]

class DeleteUser(DestroyAPIView):
    queryset = GeneralUser.objects.all()
    serializer_class = GeneralUserSerializer
    lookup_field = 'username'

class GeneralUser(APIView):

    pass    

        
class UserAuth(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
 
        general_user = authenticate(username=username, password=password)
        
        if general_user is not None:

            user_role = general_user.user_role

            user_role_to_model = {
                'Owner': Owner,
                'Manager': RestManager,
                'Asset': AssetUser,
                'Clients': ClientsUser,
                'HR': HRUser,
                'Payroll': PayrollUser,
                'Driver': Driver,
                'Administrator': Administrator,
            }

            if user_role in user_role_to_model:
                using_model = user_role_to_model[user_role]
                logged_user = using_model.objects.get(id=general_user.id)

                login(request, logged_user)
                token, created = Token.objects.get_or_create(user=general_user)
                
                
                avalible_serializers = {
                    'Owner': AddOwnerSerializer,
                    'Manager': AddManagerSerializer,
                    'Asset': AssetSerializer,
                    'Clients': AddClientsUserSerializer,
                    'HR': HRUserSerializer,
                    'Payroll': AddPayrollUserSerializer,
                    'Driver': AddDriverSerializer,
                    'Administrator': AddAdministratorSerializer,
                }
                
                if user_role in avalible_serializers:
                    choosen_seralizer = avalible_serializers[user_role]
                else:
                    return JsonResponse({'error': 'Unsupported user model'})


                serializer = choosen_seralizer(logged_user)
                user_data = serializer.data
                        
                
                return JsonResponse({'message': 'Logged in successfully', 'user_role':logged_user.user_role, 'token':token.key, 'data':user_data })
        
        else:
            return JsonResponse({'error': 'Invalid username or password'})

    
    def delete(self, request):
        token_dict = request.data
        token = token_dict.get('token')
        
        request.session.flush()
        logout(request)
        return JsonResponse({'message': 'Logged out successfully'})

class AddUser(APIView):
    def post(self, request):
        user_role = request.data.get('user_role')

        serializers = {
            'Owner' : AddOwnerSerializer,
            'Manager' : AddManagerSerializer,
            'Asset' : AddAssetUserSerializer,
            'Clients' : AddClientsUserSerializer,
            'HR' : AddHRUserSerializer,
            'Payroll' : AddPayrollUserSerializer,
            'Driver' : AddDriverSerializer,
            'Administrator' : AddAdministratorSerializer,
        }
        
        selected_serializer = serializers[user_role]
        serializer = selected_serializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['message'] = 'Succesfully registered a new User'
            data['username'] = account.username
            
            user_model = account.__class__
            user = user_model.objects.get(username=account.username)
            
            token = Token.objects.create(user=user)
        
        else:
            data = serializer.errors
            
        return JsonResponse(data)

