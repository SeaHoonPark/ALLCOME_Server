from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuizRequestViewSet

router = DefaultRouter()
router.register('problem', QuizViewSet)
request_list = QuizRequestViewSet.as_view({
    'get': 'list',
})


urlpatterns = [
    path('', include(router.urls)),
    path('request', request_list),
]
