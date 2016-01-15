from django.shortcuts import render, redirect
from Tutorial2.models import Question
from django.utils import timezone


def view_questions(request): #1
    questions = Question.objects.all() #2
    return render(request, 'questions.html', {'questions': questions}) #3

def add_question(request): #1
    new_question_text = request.POST['question_text'] #2
    Question.objects.create(question_text=new_question_text, pub_date=timezone.now()) #3
    return redirect('/questions') #4