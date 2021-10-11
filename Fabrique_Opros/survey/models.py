from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    date_start = models.DateField(null=False)
    date_end = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=4000)
    date_create = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


TypeQuestion = (
    (0, 'Ответ текстом'),
    (1, 'Ответ с выбором одного варианта'),
    (2, 'Ответ с выбором нескольких вариантов')
)


class Question(models.Model):
    text = models.CharField(max_length=200)
    type = models.SmallIntegerField(choices=TypeQuestion)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class AnswerText(models.Model):
    user_answer = models.ForeignKey(UserAnswer, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


