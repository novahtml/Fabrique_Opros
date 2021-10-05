from rest_framework import serializers
from . import models


class SurveySerializer(models.Model):
    class Meta:
        model = models.Survey
        fields = ('IdVisNumber', 'IdDoc', 'NameDoc')

