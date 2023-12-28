
# Auth
from django.contrib.auth import authenticate

# Password
import secrets
import string


from django.http import JsonResponse
from django.shortcuts import get_object_or_404


from .serializers import GeneralUserSerializer, GetAllUsernamesSerializer, CreateAddressesSerializer, GetAddressesSerializer
from rest_manager.serializers import AddManagerSerializer, RestManagerSerializer, GetRestManager, UpdateRestManager
from asset_dept.serializers import AddAssetUserSerializer, AssetSerializer, GetAssetUser, UpdateAssetUser
from clients_dept.serializers import AddClientsUserSerializer, ClientsSerializer, GetClientsUser, UpdateClientsUser
from hr_dept.serializers import AddHRUserSerializer, HRUserSerializer, GetHRUser, UpdateHRUser
from payroll_dept.serializers import AddPayrollUserSerializer, PayrollSerializer, PayrollUser, GetPayrollUser, UpdatePayrollUser
from driver.serializers import AddDriverSerializer, DriverSerializer, GetDriver, UpdateDriverUser
from administrator.serializers import AddAdministratorSerializer, AdministratorSerializer, GetAdministrator, UpdateAdministrator

# Rest API
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView

# JWT
from rest_framework_simplejwt.tokens import RefreshToken

# Models
from .models import GeneralUser
from rest_manager.models import RestManager
from asset_dept.models import AssetUser
from clients_dept.models import ClientsUser
from hr_dept.models import HRUser
from payroll_dept.models import PayrollUser
from driver.models import Driver
from administrator.models import Administrator
from other.models import State, Country

# DB
from django.db.models import F
from django.db.models import Q

# Pagination
from rest_framework.pagination import PageNumberPagination


class GlobalDictionaries:
    dicts = {
        'UserModels': {
            'All': GeneralUser,
            'Manager': RestManager,
            'Asset': AssetUser,
            'Clients': ClientsUser,
            'HR': HRUser,
            'Payroll': PayrollUser,
            'Driver': Driver,
            'Administrator': Administrator,
        },

        'AddUserSerializers': {
            'Manager': AddManagerSerializer,
            'Asset': AddAssetUserSerializer,
            'Clients': AddClientsUserSerializer,
            'HR': AddHRUserSerializer,
            'Payroll': AddPayrollUserSerializer,
            'Driver': AddDriverSerializer,
            'Administrator': AddAdministratorSerializer,
        },

        'UserSerializers': {
            'Manager': RestManagerSerializer,
            'Asset': AssetSerializer,
            'Clients': ClientsSerializer,
            'HR': HRUserSerializer,
            'Payroll': PayrollSerializer,
            'Driver': DriverSerializer,
            'Administrator': AdministratorSerializer,
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
            'Manager': UpdateRestManager,
            'Asset': UpdateAssetUser,
            'Clients': UpdateClientsUser,
            'HR': UpdateHRUser,
            'Payroll': UpdatePayrollUser,
            'Driver': UpdateDriverUser,
            'Administrator': UpdateAdministrator,
        }
    }

    @staticmethod
    def get_serializer(name, key):
        dictionary = GlobalDictionaries.dicts.get(name)
        if dictionary:
            return dictionary.get(key)


class UsersPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 100

    def get_page_size(self, request):
        page_size = super().get_page_size(request)
        if page_size is None or page_size == 0:
            return self.max_page_size
        return page_size


class GetGeneralUsers(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = UsersPagination
    

    def get_queryset(self):
        # Choosing correct serializer
        role = self.request.query_params.get('role')
        serializer_class = GlobalDictionaries.get_serializer(
            'UserSerializers', role)
        serializer_class = serializer_class or GeneralUserSerializer

        queryset = serializer_class.Meta.model.objects.all()

        # Filtering by status
        status = self.request.query_params.get('status')

        if status == 'True':
            queryset = queryset.filter(is_active=True)
        elif status == 'False':
            queryset = queryset.filter(is_active=False)
            
        # Additional filtering using Q
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(Q(username__icontains=search_query) | Q(email__icontains=search_query))

            

        # Sort by date
        queryset = queryset.order_by(F('date_joined').desc(nulls_last=True))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Pagination
        paginator = UsersPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = GeneralUserSerializer(result_page, many=True)

        response_data = {
            'posts_amount': paginator.page.paginator.count,
            'total_pages': paginator.page.paginator.num_pages,
            'current_page': paginator.page.number,
            'results': serializer.data,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'total_results': queryset.count(),
        }
        return JsonResponse(response_data, status=200)


class GetUsernames(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        desired_role = self.request.query_params.get('role', '').strip()
        search_query = self.request.query_params.get('search', '').strip()

        user_model = GlobalDictionaries.get_serializer(
            'UserModels', desired_role)

        users = user_model.objects.all()

        if search_query:
            users = users.filter(Q(username__icontains=search_query))

        serializer = GetAllUsernamesSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)


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

            user_model = GlobalDictionaries.get_serializer(
                'UserModels', user_role)
            logged_user = user_model.objects.get(username=general_user.pk)

            serializer_class = GlobalDictionaries.get_serializer(
                'UserSerializers', user_role)

            serializer = serializer_class(logged_user)
            user_data = serializer.data

            jwt = self.get_tokens_for_user(logged_user)

            return JsonResponse({'message': 'Logged in successfully', 'user_role': logged_user.user_role, 'data': user_data, 'jwt': jwt})

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
        data = request.data
        
        user_role = data['user_role']

        # Password generating
        generated_password = self.generate_password()
        data['password'] = generated_password
        data['password2'] = generated_password

        serializer_class = GlobalDictionaries.get_serializer(
            'AddUserSerializers', user_role)

        serializer = serializer_class(data=data)
        
        

        # correspondence_state_name = request.data.pop('correspondence_state')
        # registered_state_name = request.data.pop('registered_state')
        # residence_state_name = request.data.pop('residence_state')

        # correspondence_state = get_object_or_404(State, name=correspondence_state_name, country__name=request.data['correspondence_country'])
        # registered_state = get_object_or_404(State, name=registered_state_name, country__name=request.data['registered_country'])
        # residence_state = get_object_or_404(State, name=residence_state_name, country__name=request.data['residence_country'])

        # request.data['correspondence_state'] = correspondence_state
        # request.data['registered_state'] = registered_state
        # request.data['residence_state'] = residence_state

        # correspondence_country_name = request.data.pop('correspondence_country')
        # registered_country_name = request.data.pop('registered_country')
        # residence_country_name = request.data.pop('residence_country')

        # correspondence_country = get_object_or_404(Country, name=correspondence_country_name)
        # registered_country = get_object_or_404(Country, name=registered_country_name)
        # residence_country = get_object_or_404(Country, name=residence_country_name)

        # request.data['correspondence_country'] = correspondence_country
        # request.data['registered_country'] = registered_country
        # request.data['residence_country'] = residence_country
        

        
        response_data = {}

        if serializer.is_valid():
            account = serializer.save()
            
        else:
            response_data = serializer.errors
            return JsonResponse(response_data, status=400)
        
            
        # Address
        residence_state_name = data['residence_state']
        registered_state_name = data['registered_state']
        correspondence_state_name = data['correspondence_state']

        residence_state = State.objects.get(name=residence_state_name)
        registered_state = State.objects.get(name=registered_state_name)
        correspondence_state = State.objects.get(name=correspondence_state_name)

        data['residence_state'] = residence_state.id
        data['registered_state'] = registered_state.id
        data['correspondence_state'] = correspondence_state.id
        
        addres_serializer = CreateAddressesSerializer(data=data)
        # Address 
            
        if addres_serializer.is_valid():
            addres_serializer.save()
            
            response_data['message'] = f'Succesfully registered {account.username}'
            print("Created ", account.username,
                  " with password: ", generated_password)
            
        else:
            response_data = addres_serializer.errors
            return JsonResponse(response_data, status=400)
            
        return JsonResponse(response_data, status=201)

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(8))
        return password


class getUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username, user_role):

        user_model = GlobalDictionaries.get_serializer('UserModels', user_role)
        user = user_model.objects.get(username=username)

        user_serializer = GlobalDictionaries.get_serializer(
            'GetUserSerializers', user_role)
        serializer_instance = user_serializer(user)
        
        
        output = serializer_instance.data
        return JsonResponse(output, status=200, safe=False)


class UpdateUser(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, username, user_role):
        data = request.data

        try:
            user_model = GlobalDictionaries.get_serializer(
                'UserModels', user_role)
            user = user_model.objects.get(username=username)

            fields_to_check = ['username', 'email']
            conflicting_fields = []

            for field_name in fields_to_check:
                if field_name in data:
                    field_value = data[field_name]
                    exclude_conditions = {field_name: field_value}
                    if GeneralUser.objects.exclude(username=username).filter(**exclude_conditions).exists():
                        conflicting_fields.append(field_name)

            if conflicting_fields:
                error_message = f'The following fields are already taken: {", ".join(conflicting_fields)}. Please try another.'
                return JsonResponse({'error': error_message}, status=400)

            user_model = GlobalDictionaries.get_serializer(
                'UserModels', user_role)
            user = user_model.objects.get(username=username)

            serializer_class = GlobalDictionaries.get_serializer(
                'UpdateUserSerializers', user_role)
            serializer = serializer_class(user, data=data)

            if serializer.is_valid():
                serializer.update(user, data)
                return JsonResponse({'message': 'Successfully updated'}, status=200)

            else:
                return JsonResponse(serializer.errors, status=400)

        except GeneralUser.DoesNotExist:
            return JsonResponse({'error': 'Brand does not exist.'}, status=404)


class ChangeUserState(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, username):
        user = GeneralUser.objects.get(username=username)
        user.is_active = not user.is_active
        user.save()
        return JsonResponse({'message': 'Changed successfully'}, status=200)

