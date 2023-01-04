from rest_framework.viewsets import ModelViewSet
from .models import Quiz, Question, Answer, QuizUser
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, QuizUserSerializer


class QuizModelViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionModelViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerModelViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuizUserModelViewSet(ModelViewSet):
    queryset = QuizUser.objects.all()
    serializer_class = QuizUserSerializer
