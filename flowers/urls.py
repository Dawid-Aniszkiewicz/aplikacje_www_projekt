from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='flowers-welcome'),
    path('about/', views.about_view, name='flowers-about'),
]