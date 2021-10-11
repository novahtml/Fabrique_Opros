from rest_framework import serializers
from . import models


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ('id', 'text', 'question')


class AnswerTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AnswerText
        fields = ('id', 'text')


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Survey
        fields = ('__all__')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ('text', 'type', 'survey')




# class QuestionSerializer(serializers.ModelSerializer):
#     answer = AnswerSerializer(many=True, allow_null=True)
#     class Meta:
#         model = models.Question
#         fields = ('id', 'text', 'type', 'answer', 'answer_text', 'survey')
#
#     def create(self, validated_data):
#         answers = validated_data.pop('answer')
#
#         new_question = models.Survey.objects.create(**validated_data)
#         for i in answers:
#             QuestionSerializer.objects.create(**i, quest=new_question)
#         return new_question
#
#     def validate_type(self, value):
#         if value < 0 or value > 2:
#             raise serializers.ValidationError('Тип вопроса допускается в пределах от 0 до 2')
#         return value
#
#
# class SurveySerializer(serializers.ModelSerializer):
#     question = QuestionSerializer(many=True, allow_null=True)
#     class Meta:
#         model = models.Survey
#         fields = ('id', 'Name', 'date_start', 'date_end', 'description', 'question')
#
#
#     def create(self, validated_data):
#         questions = validated_data.pop('question')
#         new_survey = models.Survey.objects.create(**validated_data)
#         for i in questions:
#             QuestionSerializer.objects.create(**i, survey=new_survey)
#         return new_survey




