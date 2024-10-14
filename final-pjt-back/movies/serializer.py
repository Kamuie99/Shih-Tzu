from rest_framework import serializers
from .models import Movie, Genre
from accounts.models import User

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    liked_movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'nickname', 'liked_movies', 'following', 'followers']