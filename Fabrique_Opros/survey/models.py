from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    Name = models.CharField(max_length=150, db_index=True)
    DateStart = models.DateField(null=False)
    DateEnd = models.DateField(null=True, blank=True)
    Description = models.CharField(max_length=4000)
    DateCreate = models.DateTimeField(auto_now_add=True, null=True, blank=True)


TypeQuestion = (
    (0, 'Ответ текстом'),
    (1, 'Ответ с выбором одного варианта'),
    (2, 'Ответ с выбором нескольких вариантов')
)


class Question(models.Model):
    Text = models.CharField(max_length=200)
    Type = models.SmallIntegerField(choices=TypeQuestion)
    Survey = models.ForeignKey(Survey, on_delete=models.CASCADE)


class Answer(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Text = models.CharField(max_length=200)


class UserAnswer(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class AnswerText(models.Model):
    UserAnswer = models.ForeignKey(UserAnswer, on_delete=models.CASCADE)
    Text = models.CharField(max_length=200)
