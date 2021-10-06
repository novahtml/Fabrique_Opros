from rest_framework import serializers
from . import models


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Survey
        fields = ('id', 'Name', 'DateStart', 'DateEnd', 'Description')

