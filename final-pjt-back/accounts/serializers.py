from rest_framework import serializers
from .models import User
from movies.models import Movie
from comments.models import Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = ['id', 'content', 'created_at', 'updated_at', 'movie']

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'nickname', 'profile_image']

class UserSerializer(serializers.ModelSerializer):
    liked_movies = MovieSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True, source='review_set')
    following = SimpleUserSerializer(many=True, read_only=True)
    followers = SimpleUserSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'liked_movies', 'reviews', 'following', 'followers', 'profile_image')

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'nickname')