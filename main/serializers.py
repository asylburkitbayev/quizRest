from rest_framework import serializers
from .models import Quiz, Question, Answer, QuizUser


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'title', 'correct', 'question']


class QuestionSerializer(serializers.ModelSerializer):
    q_a = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'quiz', 'q_a']


class QuizSerializer(serializers.ModelSerializer):
    q_q = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'q_q']


class QuizUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizUser
        fields = ['id', 'quiz', 'question', 'answer', 'user']
