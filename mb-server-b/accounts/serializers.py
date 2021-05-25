from rest_framework import serializers
from django.contrib.auth import get_user_model

from community.serializers import *
from community.models import *

User = get_user_model()

class UserCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password' )
        extra_kwargs = {'password': {'write_only': True}}

class UserSerializer(serializers.ModelSerializer):
    community_set = CommunitySerializer(many=True)
    movies = MovieSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'community_set', 'movies')