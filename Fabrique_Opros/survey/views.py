from django.shortcuts import render
from rest_framework import viewsets, permissions
from . import models
from . import serializers


from django.contrib.auth import authenticate
from rest_framework.response import Response

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = models.Survey.objects.all()
    serializer_class = serializers.SurveySerializer
    permission_classes = [permissions.IsAdminUser]
