from django.http import JsonResponse

from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from .models import MyMessages
from users.models import GeneralUser

from .serializers import GetMessagesSerializer, CreateMessageSerializer


class GetMessages(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = self.request.query_params.get('query', '').strip()
        mail_version = self.request.query_params.get('version', '').strip()
        username = self.request.query_params.get('user', '').strip()

        try:
            user = GeneralUser.objects.get(username=username)
        
            if mail_version == 'all':
                all_messages = MyMessages.objects.filter(Q(receiver=user) | Q(sender=user))
                
            else:
                if mail_version == 'inbox':
                    all_messages = MyMessages.objects.filter(receiver=user)
                else:
                    all_messages = MyMessages.objects.filter(sender=user)
                    
        except GeneralUser.DoesNotExist as error:
            return JsonResponse((''), status=404, safe=False)
        
                    
        if query:
            all_messages = [message for message in all_messages if
                     query.lower() in message.sender.username.lower() or
                     query.lower() in message.receiver.username.lower() or
                     query.lower() in message.title.lower() or
                     query.lower() in message.content.lower()]
        
        serialized_data = GetMessagesSerializer(all_messages, many=True)

        return JsonResponse(serialized_data.data, safe=False)
    
    
    
    
class CreateMessage(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        print(data)
        
        if data.get('taget') == 'Users':
            for receiver_username in data.get('to', []):
                user_data = {
                    'content': data.get('content'),
                    'sender': data.get('from'),
                    'receiver': receiver_username,
                    'title': data.get('title'),
                }

                serializer = CreateMessageSerializer(data=user_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return JsonResponse({'errors': serializer.errors}, status=400)

            return JsonResponse({'message': 'Messages sent successfully'}, status=201)
        else:
            pass
            # serializer = CreateMessageSerializer(data=data)
        

        
        


    
# Delete 
class DeleteMessages(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    queryset = MyMessages.objects.all()
    serializer_class = GetMessagesSerializer

    def delete(self, request, *args, **kwargs):
        message_ids = request.data.get('message_ids', [])
        print(message_ids)
        if message_ids:
            messages = MyMessages.objects.filter(id__in=message_ids)
            messages.delete()
            return JsonResponse({'message': 'Messages deleted successfully.'}, status=204,)

        return super().delete(request, *args, **kwargs)

# Delete 