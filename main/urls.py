from rest_framework.routers import DefaultRouter
from .views import QuizModelViewSet, QuestionModelViewSet, AnswerModelViewSet, QuizUserModelViewSet

routers = DefaultRouter()

routers.register('quiz', QuizModelViewSet)
routers.register('question', QuestionModelViewSet)
routers.register('answer', AnswerModelViewSet)
routers.register('quizuser', QuizUserModelViewSet)

urlpatterns = routers.urls
