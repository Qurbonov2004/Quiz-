from django.urls import path
from main.views import main,create_quiz,quiz_list


urlpatterns=[
    path('',main, name='main'),
    path('create/',create_quiz, name='create_quiz'),
    path('list/',quiz_list, name='quiz_list')
]