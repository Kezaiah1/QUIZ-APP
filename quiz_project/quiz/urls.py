from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_quiz, name='create_quiz'),
    path('add_questions/<int:quiz_id>/', views.add_questions, name='add_questions'),
    path('add_answers/<int:question_id>/', views.add_answers, name='add_answers'),
    path('take/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
]    