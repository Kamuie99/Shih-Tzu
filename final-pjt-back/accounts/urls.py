from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>', views.profile, name='profile'),
    path('follow/check/<str:username>', views.check_followed, name='check_followed'),
    path('follow/<str:username>', views.follow, name='follow'),
    path('update/', views.update, name='update'),
    path('delete/<str:username>/', views.delete, name='delete'),
    path('change-password/', views.change_password, name='change_password'),
]
