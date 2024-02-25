from django.shortcuts import render,redirect
from main.models import *

def main(request):
    return render(request,'dashboard/index.html')


def create_quiz(request):
    if request.method=='POST':
        owner=request.user
        name=request.POST['name']
        if owner and name:
            Quiz.objects.create(
                owner=owner,
                name=name
            )
        
        redirect('quiz_list')

    return render(request, 'dashboard/quiz/create.html' )


def quiz_list(request):   
    quizzes = Quiz.objects.all()
    context = {
        'quizzes': quizzes
    }
    return render(request, 'dashboard/quiz/list.html', context)

