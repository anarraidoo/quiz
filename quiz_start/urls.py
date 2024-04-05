from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz, name='home'),
    path('quiz', views.start, name='quiz'),
    path('api/get-quiz/', views.get_quiz, name='get_quiz'),
    path('submit-quiz/', views.submit_quiz, name='submit_quiz'),
]
