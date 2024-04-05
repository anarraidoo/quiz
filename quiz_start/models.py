from django.db import models

# Create your models here.
import uuid
import random


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Question(BaseModel):
    question = models.CharField(max_length=100)

    # trait_A_score = models.IntegerField(default=0)
    # trait_B_score = models.IntegerField(default=0)
    # trait_C_score = models.IntegerField(default=0)

    def __str__(self):
        return self.question


class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    trait_A_score = models.IntegerField(default=0)
    trait_B_score = models.IntegerField(default=0)
    trait_C_score = models.IntegerField(default=0)

    def __str__(self):
        return self.answer
