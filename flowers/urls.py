from django.urls import path
from . import views

app_name = 'flowers'

urlpatterns = [
    path('', views.flower_list, name='flower-list'),
    path('kwiat/<slug:slug>/', views.flower_detail, name='flower-detail'),
    path('about/', views.about_view, name='flowers-about'),
]