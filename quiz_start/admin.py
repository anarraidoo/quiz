# from django.contrib import admin
#
# # Register your models here.
# from django.contrib import admin
# from .models import *
#
#
# # Register your models here.
#
# class AnswerAdmin(admin.StackedInline):
#     model = Answer
#     extra = 3  # Number of inline forms to display by default
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [AnswerAdmin]
#     readonly_fields = ('uid',)
#     # fields = ('uid', 'question')
#     # list_display = ['pk', 'question']
#
#
# # admin.site.register(PersonalityTrait, PersonalityTraitAdmin)
# # admin.site.register(Types)
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer)

from django.contrib import admin
from .models import *


class AnswerAdmin(admin.StackedInline):
    model = Answer
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]
    # list_display = ('uid', 'question')


# admin.site.register(Types)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
