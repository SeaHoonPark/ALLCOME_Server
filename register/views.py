from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import User, Wrong, Bookmark
from quiz.models import Quiz
from quiz.serializers import QuizSerializer
from .serializers import UserSerializer, WrongSerializer, BookmarkSerializer
from rest_framework.response import Response


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        email = self.request.query_params.get('email', None)
        if email is not None:
            email_qs = qs.filter(email=email)
            return email_qs


class WrongViewSet(ModelViewSet):
    queryset = Wrong.objects.all()
    serializer_class = WrongSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        email = self.request.query_params.get('email', None)
        if email is not None:
            email_qs = qs.filter(email=email)
            return email_qs

    def perform_create(self, serializer):
        qs = super().get_queryset()
        email = self.request.data['email']
        pr_id = self.request.data['pr_id']
        email_qs = qs.filter(email=email, pr_id=pr_id)
        print(email_qs)
        if email_qs:
            return Response(status=300)
        else:
            serializer.save()


class WrongDetail(ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        pr_id = self.request.query_params.get('pr_id', None)
        if pr_id is not None:
            pr_id_qs = qs.filter(pr_id=pr_id)
            return pr_id_qs


class BookmarkViewSet(ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        email = self.request.query_params.get('email', None)
        if email is not None:
            email_qs = qs.filter(email=email)
            return email_qs

    def perform_create(self, serializer):
        qs = super().get_queryset()
        email = self.request.data['email']
        pr_id = self.request.data['pr_id']
        email_qs = qs.filter(email=email, pr_id=pr_id)
        if email_qs:
            return Response(status=300)
        else:
            serializer.save()
