
# Auth
from django.contrib.auth import authenticate, get_user_model, login, logout
# Password Auth
from django.contrib.auth import password_validation
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.contrib.auth.password_validation import get_password_validators

from .models import GeneralUser
from .serializers import GeneralUserSerializer, GeneralUserRegistrationSerializer
from django.http import JsonResponse


def is_password_valid(password):
    password_validators = get_password_validators({})
    password_errors = []

    for validator in password_validators:
        try:
            validator.validate(password)
        except ValidationError as e:
            password_errors.extend(e.messages)
    
    return password_errors

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
            login(request, general_user)
        
            return Response({'message': 'Logged in successfully', 'role' : general_user.user_role, 'username': general_user.username}, status=status.HTTP_200_OK)
        
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

        
    else:
        return Response({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


# CHANGE TO POST IN PRODUCTION=========================================== 
@api_view(['GET'])
def generalLogOut(request):
    if request.method == 'GET':
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
