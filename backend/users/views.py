
# Auth
from django.contrib.auth import authenticate, get_user_model, login, logout

# Password Auth
from django.shortcuts import get_object_or_404, render


from django.http import JsonResponse
from django.core import serializers


from .serializers import GeneralUserSerializer, GeneralUserRegistrationSerializer
from owner.serializers import AddOwnerSerializer
from rest_manager.serializers import AddManagerSerializer
from asset_dept.serializers import AddAssetUserSerializer
from clients_dept.serializers import AddClientsUserSerializer
from hr_dept.serializers import AddHRUserSerializer, HRUserSerializer
from payroll_dept.serializers import AddPayrollUserSerializer
from driver.serializers import AddDriverSerializer
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


# CBV

class GUViewSet(viewsets.ModelViewSet):
    serializer_class = GeneralUserSerializer
    queryset = GeneralUser.objects.all()
    
    # query
    filter_backends = (filters.SearchFilter, )
    search_fields = ('username', 'email')

    
    def get_gu(self, request):
        serializer = GeneralUserSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    
    def destroy(self, request, *args, **kwargs):
        username = request.data.get('username')
        user_role = request.data.get('user_role')
        print(username,user_role)
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
        
        user_model = user_role_to_model[user_role]
        
        try:
            user  = get_object_or_404(user_model, username=username)
            user.delete()
            return JsonResponse({'message': 'User successfully deleted'})
        except HRUser.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'})
        except Exception as e:
            return JsonResponse({'error' : str(e)})
    
    
    

class GeneralUser(APIView):
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """
            Returns user data from GeneralUser class
            
            * Requires token authentication
        """

        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        token = authorization_header.split(' ')[1] if authorization_header.startswith('Token ') else None
        
        user_model = request.GET.get('user_role')

        
        user_role_to_serializer = {
            'Owner': AddOwnerSerializer,
            'Manager': AddManagerSerializer,
            'Asset': AddAssetUserSerializer,
            'Clients': AddClientsUserSerializer,
            'HR': HRUserSerializer,
            'Payroll': AddPayrollUserSerializer,
            'Driver': AddDriverSerializer,
            'Administrator': AddAdministratorSerializer,
        }
        
        if user_model in user_role_to_serializer:
            serializer_class = user_role_to_serializer[user_model]
            user_class = serializer_class.Meta.model
        else:
            return JsonResponse({'error': 'Unsupported user model'})

        user = user_class.objects.get(auth_token=token)
            

        serializer = serializer_class(user)
        user_data = serializer.data


        return JsonResponse(user_data)
        
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
                return JsonResponse({'message': 'Logged in successfully', 'user_role':logged_user.user_role, 'token':token.key })
        
        else:
            return JsonResponse({'error': 'Invalid username or password'})

    
    def delete(self, request):
        token_dict = request.data
        token = token_dict.get('token')
        
        request.session.flush()
        logout(request)
        return JsonResponse({'message': 'Logged out successfully'})

# CBV





@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_users(request, role, active, search):
    queryset  = GeneralUser.objects.all()
    
    if role and role.lower() != 'all':
            queryset = queryset.filter(user_role=role)

    if active and active.lower() != 'all':
        if active.lower() == 'true':
            queryset = queryset.filter(is_active=True)
        elif active.lower() == 'false':
            queryset = queryset.filter(is_active=False)

    users = queryset.all()
    users_serialized = GeneralUserSerializer(users, many=True)

    if search != 'all':
        search_results = [user for user in users_serialized.data if any(search_term in str(user.values()) for search_term in [search])]
        return Response(search_results)
    else:
        return Response(users_serialized.data)

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def add_user(request):
    """
    Method to register new general user
    """
    if request.method == 'POST':
        
        user_role = request.data.get('user_role')
        
        serializers = {
            'Owner' : AddOwnerSerializer,
            'Manager' : AddManagerSerializer,
            'Asset' : AddAssetUserSerializer,
            'Clients' : AddClientsUserSerializer,
            'HR' : AddHRUserSerializer,
            'Payroll' : AddPayrollUserSerializer,
            'Driver' : AddOwnerSerializer,
            'Administrator' : AddAdministratorSerializer,
        }
        
        sz = serializers[user_role]
        serializer = sz(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['message'] = 'Succesfully registered a new User'
            data['username'] = account.username
            
            user = GeneralUser.objects.get(username=request.data['username'])
            token = Token.objects.create(user=user)
            # data['token'] = token.key
        
        else:
            data = serializer.errors
            print(data)
            
        return JsonResponse(data)

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def remove_user(request, username, user_role):
    
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
    
    user_model = user_role_to_model[user_role]
    
    try:
        user  = get_object_or_404(user_model, username=username)
        user.delete()
        return JsonResponse({'message': 'User successfully deleted'})
    except HRUser.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'})
    except Exception as e:
        return JsonResponse({'error' : str(e)})


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_token(request):
    return JsonResponse({'passed_for': request.user.username})
