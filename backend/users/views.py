
# Auth
from django.contrib.auth import authenticate, get_user_model, login, logout
# Password Auth
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token



from .serializers import GeneralUserSerializer, GeneralUserRegistrationSerializer
from django.http import JsonResponse

# Models
from .models import GeneralUser
from asset_dept.models import *
from clients_dept.models import *
from hr_dept.models import *
from payroll_dept.models import *
from driver.models import Driver
from rest_manager.models import RestManager

def app_redirect(role):
    role = f'{role}'
    output_redirect = f'{role}_dashboard' 
    return output_redirect

@api_view(['GET'])
def getUsers(request):
    """
    Method to log-in user
    """
    users = GeneralUser.objects.all()
    
    users_serialized = GeneralUserSerializer(users, many=True)
    return Response(users_serialized.data)


@api_view(['POST'])
def createUser(request):
    """
    Method to register new general user
    """
    if request.method == 'POST':
        serializer = GeneralUserRegistrationSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['message'] = 'Succesfully registered a new User'
            data['username'] = account.username
            data['user_role'] = account.user_role
            
            user = GeneralUser.objects.get(username=request.data['username'])
            token = Token.objects.create(user=user)
            data['token'] = token.key
        
        else:
            data = serializer.errors
            
        return JsonResponse(data)


@api_view(['POST'])
def generalLogIn(request):
    """
    Method used to log-in user, then check his role and then redirect to specified site
    
    """

    if request.method == 'POST':

        username = request.data.get('username')
        password = request.data.get('password')
 
        general_user = authenticate(username=username, password=password)
    
        if general_user is not None:
            user_role = general_user.user_role

            user_role_to_model = {
                'Driver': Driver,
                'Manager': RestManager,
            }

            if user_role in user_role_to_model:
                using_model = user_role_to_model[user_role]
                logged_user = using_model.objects.get(id=general_user.id)
                login(request, logged_user)
            
            
            token, created = Token.objects.get_or_create(user=general_user)
            redirection = app_redirect(general_user.user_role)
            return JsonResponse({'message': 'Logged in successfully', 'user-model' : using_model, 'username': general_user.username, 'redirect_to': redirection, 'token':token.key}, status=status.HTTP_200_OK)
        
        else:
            return JsonResponse({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

        
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


# CHANGE TO POST IN PRODUCTION=========================================== 
@api_view(['GET'])
def generalLogOut(request):
    if request.method == 'GET':
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_token(request):
    return JsonResponse({'passed_for': request.user.username})





