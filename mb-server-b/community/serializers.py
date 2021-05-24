from rest_framework import serializers
from .models import Community, Movie

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = (
            'user', 'vote_users', 'title', 'movie_title_1', 'movie_title_2',
            # 'created_at', 'updated_at',
        )


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields ='__all__'
            # 'title', 'overview', 'poster_path',
            # 'created_at', 'updated_at',
        