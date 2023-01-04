from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Question(models.Model):
    title = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='q_q')

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='q_a')

    def __str__(self):
        return self.title


class QuizUser(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

