# from django.db import models
#
# # Create your models here.
# import uuid
# import random
#
#
# class BaseModel(models.Model):
#     uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)
#
#     class Meta:
#         abstract = True
#
# # CATEGORY
# # class Types(BaseModel):
# #     gfg_name = models.CharField(max_length=100)
# #
# #     def __str__(self) -> str:
# #         return self.gfg_name
#
#
# class PersonalityTrait(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class Question(BaseModel):
#     # gfg = models.ForeignKey(Types, related_name='gfg', on_delete=models.CASCADE)
#     question = models.CharField(max_length=100)
#     trait = models.ForeignKey(PersonalityTrait, on_delete=models.CASCADE, related_name='questions')
#     marks = models.IntegerField(default=5)
#
#     def __str__(self) -> str:
#         return self.question
#
#     # def get_answers(self):
#     #     answer_objs = list(Answer.objects.filter(question=self))
#     #     data = []
#     #     random.shuffle(answer_objs)
#     #
#     #     for answer_obj in answer_objs:
#     #         data.append({
#     #             'answer': answer_obj.answer,
#     #             'is_correct': answer_obj.is_correct
#     #         })
#     #     return data
#
#
# class Answer(BaseModel):
#     question = models.ForeignKey(Question, related_name='question_answer', on_delete=models.CASCADE)
#     answer = models.CharField(max_length=100)
#     # is_correct = models.BooleanField(default=False)
#     score = models.IntegerField(default=0)  # Score associated with selecting this answer
#
#     def __str__(self) -> str:
#         return self.answer