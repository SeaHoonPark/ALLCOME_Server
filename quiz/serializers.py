from .models import Quiz
from rest_framework.serializers import ModelSerializer


class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

