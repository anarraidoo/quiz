# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import *

import random


def quiz(request):
    # context = {'gfg': request.GET.get('gfg')}
    return render(request, 'home.html')


def start(request):
    return render(request, 'quiz.html')


def get_quiz(request):
    try:
        question_objs = Question.objects.all()

        # if request.GET.get('gfg'):
        # question_objs = question_objs.filter(gfg__gfg_name__icontains=request.GET.get('gfg'))

        question_objs = list(question_objs)
        data = []
        random.shuffle(question_objs)

        for question_obj in question_objs:
            data.append({
                "uid": question_obj.uid,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answer": question_obj.get_answers(),
            })

        payload = {'status': True, 'data': data}

        return JsonResponse(payload)  # Return JsonResponse

    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")

