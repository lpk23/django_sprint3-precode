from django.urls import path
from . import views

app_name = 'pages'  # namespace для приложения pages

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
