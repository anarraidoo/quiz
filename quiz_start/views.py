# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import *

import random


def quiz(request):
    return render(request, 'home.html')


def start(request):
    return render(request, 'quiz.html')


def get_quiz(request):
    try:
        questions = Question.objects.all()
        questions = list(questions)
        random.shuffle(questions)

        data = []
        for question in questions:
            answers = [
                {'uid': answer.uid, 'answer': answer.answer} for answer in question.answers.all()
            ]
            data.append({
                'uid': question.uid,
                'question': question.question,
                'answers': answers,
            })

        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")


def calculate_personality_traits(selected_answers):
    trait_A_score = sum(answer.trait_A_score for answer in selected_answers)
    trait_B_score = sum(answer.trait_B_score for answer in selected_answers)
    trait_C_score = sum(answer.trait_C_score for answer in selected_answers)
    # Determine resulting personality trait based on scores
    if trait_A_score >= trait_B_score and trait_A_score >= trait_C_score:
        return 'A'
    elif trait_B_score >= trait_A_score and trait_B_score >= trait_C_score:
        return 'B'
    else:
        return 'C'


@ensure_csrf_cookie
def submit_quiz(request):
    if request.method == 'POST':
        selected_answers = request.POST.getlist('answers[]')
        try:
            selected_answers = Answer.objects.filter(uid__in=selected_answers)
            personality_trait = calculate_personality_traits(selected_answers)
            return JsonResponse({'status': True, 'personality_trait': personality_trait})
        except Answer.DoesNotExist:
            return JsonResponse({'status': False, 'message': 'One or more selected answers do not exist.'}, status=400)

    return HttpResponse("Invalid method")
