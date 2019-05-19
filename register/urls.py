from django.urls import path
from .views import UserViewSet, WrongViewSet, BookmarkViewSet, WrongDelete, WrongDetail, BookmarkDelete

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
wrong_list = WrongViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
wrong_pr_detail = WrongDetail.as_view({
    'get': 'list',
})
bookmark_list = BookmarkViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns = [
    path('user_list', user_list),
    path('wrong', wrong_list),
    path('wrong/<int:pk>', WrongDelete.as_view()),
    path('detail', wrong_pr_detail),
    path('bookmark', bookmark_list),
    path('bookmark/<int:pk>', BookmarkDelete.as_view()),

]
