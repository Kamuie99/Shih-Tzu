from django.urls import path
from . import views

urlpatterns = [
    path('reviews/<int:movie_id>', views.review_detail),
    path('reviews/delete/<int:comment_id>', views.review_delete),
]
