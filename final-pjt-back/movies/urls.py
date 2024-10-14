from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.movie_list, name='movie_list'),
    path('genre-list/', views.genre_list, name='genre_list'),
    path('box_office/', views.box_office, name='box_office'),
    path('similar/<int:movie_id>', views.similar, name='similar'),
    path('shihtzu/', views.shihtzu, name='shihtzu'),
    path('AI/', views.AIRecommend, name='AIRecommend'),
    path('like/<int:movie_id>', views.like_movie, name='like_movie'),
    path('ranking/', views.ranking, name='ranking'),
]
