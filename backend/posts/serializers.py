from rest_framework import serializers
from .models import Posts
from users.models import GeneralUser

class getPostsSerializer(serializers.ModelSerializer):
    posted_date = serializers.DateTimeField(format='%Y-%m-%d')
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ['id', 'posted_date', 'author_username', 'title', 'content']

    def get_author_username(self, obj):
        user_id = obj.author.id
        try:
            user = GeneralUser.objects.get(id=user_id)
            return user.username
        except GeneralUser.DoesNotExist:
            return None
        
        

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['author', 'title', 'content']
    
    def create(self, validated_data):
        post = Posts.objects.create(**validated_data)
        return post