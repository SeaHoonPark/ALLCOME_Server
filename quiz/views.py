from rest_framework.viewsets import ModelViewSet
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Quiz
from .serializers import QuizSerializer


class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizRequestViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        subject = self.request.query_params.get('subject', None)
        if subject is not None:
            subject_qs = qs.filter(subject=subject)
            return subject_qs.order_by("?")[:1]


@api_view(['GET'])
def subject_view(request):
    data = [
        {"subject1": "Algorithme"},
        {'subject2': 'Database'},
        {'subject3': 'sofrware_engineering'},
        {'subject4': 'operation_system'},
        {'subject5': 'computer_network'},
        {'subject6': 'computer_structure'},
        {'subject7': 'data_structure'},
    ]
    return Response(data=data)
