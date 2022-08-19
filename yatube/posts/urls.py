from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Страница с группами
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
    # Главная страница
    path('', views.index, name='main'),
]
