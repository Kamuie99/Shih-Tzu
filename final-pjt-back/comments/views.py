from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import ReviewSerializer, ReviewListSerializer
from .models import Review
from movies.models import Movie
from accounts.models import User

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        reviews = reviews.ordered_by('-id')
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def review_detail(request, movie_id):
    user = request.user
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        review_data = request.data.copy()
        review_data['movie'] = movie_id
        review_data['username'] = user.username
        serializer = ReviewSerializer(data=review_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        reviews = Review.objects.filter(movie=movie)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        review = get_object_or_404(Review, movie=movie, user=user)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def review_delete(request, comment_id):
    review = get_object_or_404(Review, id=comment_id)
    if request.user == review.user:  # Only the author can delete
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
