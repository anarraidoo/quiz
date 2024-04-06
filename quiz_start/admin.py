from django.contrib import admin
from .models import *


class AnswerAdmin(admin.StackedInline):
    model = Answer
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
