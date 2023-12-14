from django.http import JsonResponse
from django.http import HttpResponseNotFound

from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from .models import MyMessages
from users.models import GeneralUser

from .serializers import GetMessagesSerializer
from django.db import models



class GetMessages(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = self.request.query_params.get('query', '').strip()
        mail_version = self.request.query_params.get('version', '').strip()
            
        # if not query:
        #     return all_messages
        
        if mail_version == 'all':
            all_messages = MyMessages.objects.all()
            
        else:
            try:
                user = GeneralUser.objects.get(username='viktot697')
                if mail_version == 'inbox':
                    all_messages = MyMessages.objects.filter(receiver=user)
                else:
                    all_messages = MyMessages.objects.filter(sender=user)
            except GeneralUser.DoesNotExist as error:
                return JsonResponse((''), status=404, safe=False)

        
        serialized_data = GetMessagesSerializer(all_messages, many=True)

        return JsonResponse(serialized_data.data, safe=False)
