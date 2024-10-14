from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Count
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from .models import Movie, Genre
from .serializer import MovieListSerializer, GenreListSerializer, UserSerializer
import numpy as np
from numpy import dot
from numpy.linalg import norm
import pandas as pd
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from datetime import datetime
import os
import random
import openai
import re

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreListSerializer(genres, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

def box_office(request):
    movies = Movie.objects.filter(box_office=True, coming_soon=False)
    serializer = MovieListSerializer(movies, many=True)
    movies = serializer.data
    movies = [movie for movie in movies if movie['poster_path']]
    sorted_movies = sorted(movies, key=lambda x: x['popularity'], reverse=True)
    return JsonResponse(sorted_movies, safe=False, json_dumps_params={'ensure_ascii': False})

def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))

data_cache = {
    "df": None,
    "tfidf_matrix": None,
    "cos_sim_matrix": None,
    "indices": None
}

def preprocess_stopwords(stopwords):
    return [word.strip().lower() for word in stopwords]

def initalize_data_cache():
    global data_cache

    if data_cache["df"] is None:
        conn = sqlite3.connect('db.sqlite3')
        query = '''
                SELECT 
                    id,
                    title,
                    overview,
                    poster_path,
                    vote_avg,
                    released_date,
                    backdrop_path
                FROM 
                    movies_movie
                '''
        df = pd.read_sql_query(query, conn)
        conn.close()

        stopwords_path = os.path.join(os.path.dirname(__file__), 'stopwords.txt')

        with open(stopwords_path, 'r', encoding='utf-8') as file:
            korean_stopwords = file.read().splitlines()

        korean_stopwords = preprocess_stopwords(korean_stopwords)

        tfidf = TfidfVectorizer(stop_words=korean_stopwords)
        tfidf_matrix = tfidf.fit_transform(df['overview'])

        cos_sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
        indices = pd.Series(df.index, index=df['id']).drop_duplicates()

        data_cache["df"] = df
        data_cache["tfidf_matrix"] = tfidf_matrix
        data_cache["cos_sim_matrix"] = cos_sim_matrix
        data_cache["indices"] = indices
    
def get_recommendations(id, cos_sim=cos_sim):
    initalize_data_cache()

    df = data_cache["df"]
    cos_sim = data_cache["cos_sim_matrix"]
    indices = data_cache["indices"]

    idx = indices[id]

    sim_scores = list(enumerate(cos_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:13]

    movies_indices = [i[0] for i in sim_scores]

    recommendations = df[['id', 'title', 'overview', 'poster_path', 'backdrop_path', 'vote_avg', 'released_date']].iloc[movies_indices]

    return recommendations

def similar(request, movie_id):
    recommend_movies = get_recommendations(movie_id)
    recommendations_list = recommend_movies.to_dict(orient='records')
    return JsonResponse(recommendations_list, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def shihtzu(request):
    preferences = request.GET

    if preferences.get('where') == 'Theater':
        movies = Movie.objects.filter(now_playing=True)
    else:
        movies = Movie.objects.filter(now_playing=False)

    if preferences.get('time') == 'now':
        time = datetime.now()
        target_time = int(time.strftime("%H")) + 1
    elif preferences.get('time') == '13:00':
        target_time = 13
    else:
        target_time = 21
    
    recommended_genres = []
    
    if preferences.get('isWeekend') == 'true':
        movies = movies.filter(runtime__gte=90)
    else:
        movies = movies.filter(runtime__lt=90)

    if target_time // 6 == 0:
        recommended_genres.extend([27, 28, 9648, 878])
    elif target_time // 6 == 1:
        recommended_genres.extend([99, 18, 36, 10751])
    elif target_time // 6 == 2:
        recommended_genres.extend([35, 16, 12, 14])
    else:
        recommended_genres.extend([53, 80, 18, 10749])

    if preferences.get('withWho') == 'Alone':
        recommended_genres.extend([27, 9648, 878, 99])
    elif preferences.get('withWho') == 'Friend':
        recommended_genres.extend([35, 28, 53, 12])
    elif preferences.get('withWho') == 'Family':
        recommended_genres.extend([18, 10751, 16, 12])
    elif preferences.get('withWho') == 'Couple':
        recommended_genres.extend([10749, 35, 18, 10402])
    else:
        movies = movies.filter(genres__pk__in=[16, 10751]).distinct().order_by('-popularity')[:50]
        movies = random.sample(list(movies), min(len(movies), 30))
        serializer = MovieListSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    genre_counts = {genre: recommended_genres.count(genre) for genre in set(recommended_genres)}

    for movie in movies:
        genre_ids = movie.genres.values_list('pk', flat=True)
        popularity_boost = sum([400 if genre_counts[genre] == 1 else 1200 for genre in genre_ids if genre in genre_counts])
        movie.popularity += popularity_boost

    movies = movies.distinct().order_by('-popularity')[:50]
    movies = random.sample(list(movies), min(len(movies), 30))

    serializer = MovieListSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def AIRecommend(request):
    preferences = request.GET
    where = preferences.get('where')
    time = preferences.get('time')
    
    if where == 'Theater':
        movies = Movie.objects.filter(now_playing=True)
    else:
        movies = Movie.objects.filter(now_playing=False)

    if time == 'now':
        time = datetime.now().strftime("%H:%M")
    elif time == '13:00':
        time = '13:00'
    else:
        time = '21:00'

    withWho = preferences.get('withWho')
    openai.api_key = settings.OPENAI_API_KEY
    messages = [
        {
            "role": "user",
            "content": """
            '다음은 전체 영화 장르 목록입니다:
            {"id": 28, "name": "action"},
            {"id": 12, "name": "adventure"},
            {"id": 16, "name": "animation"},
            {"id": 35, "name": "comedy"},
            {"id": 80, "name": "crime"},
            {"id": 99, "name": "documentary"},
            {"id": 18, "name": "drama"},
            {"id": 10751, "name": "family"},
            {"id": 14, "name": "fantasy"},
            {"id": 36, "name": "history"},
            {"id": 27, "name": "horror"},
            {"id": 10402, "name": "music"},
            {"id": 9648, "name": "mystery"},
            {"id": 10749, "name": "romance"},
            {"id": 878, "name": "SF"},
            {"id": 10770, "name": "TV movie"},
            {"id": 53, "name": "thriller"},
            {"id": 10752, "name": "war"},
            {"id": 37, "name": "western"}            
            다음 상황에 따라 어울리는 영화 장르를 이유와 함께 추천해주세요: [Where, with whom, at what time]
            단, 추천하는 장르의 id를 반드시 문장에 맨 앞에 리스트 형태로 포함시켜주세요
            """
        }
    ]
    situations = [{"role": "user", "content": f'[{where}, {withWho}, {time}]'}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages+situations
    )
    assistant_reply = response['choices'][0]['message']['content']
    genre_ids = re.findall(r'\b\d+\b', assistant_reply)
    genre_ids = [int(id) for id in genre_ids]

    movies = Movie.objects.filter(genres__pk__in=genre_ids).distinct().order_by('-popularity')[:50]
    
    # 영화 리스트에서 랜덤 샘플링
    movies = random.sample(list(movies), min(len(movies), 30))
    
    # 응답 데이터 직렬화
    serializer = MovieListSerializer(movies, many=True)
    return JsonResponse({
        'assistant_reply': assistant_reply,
        'movies': serializer.data
    }, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def ranking(request):
    users = User.objects.annotate(follower_count=Count('followers')).order_by('-follower_count').distinct()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user = request.user
    if request.method == 'POST':
        if user.liked_movies.filter(id=movie_id).exists():
            user.liked_movies.remove(movie)
            liked = False
        else:
            user.liked_movies.add(movie)
            liked = True

        return JsonResponse({'liked': liked, 'count': movie.liked_users.count()})
    
    elif request.method == 'GET':
        liked = user.liked_movies.filter(id=movie_id).exists()
        return JsonResponse({'liked': liked})

