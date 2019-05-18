from rest_framework.viewsets import ModelViewSet
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
        subject = self.request.query_params.get('subject',None)
        if subject is not None:
            subject_qs = qs.filter(subject=subject)
            return subject_qs.order_by("?")[:1]



