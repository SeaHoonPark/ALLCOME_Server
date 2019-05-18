from django.urls import path
from .views import UserViewSet, WrongViewSet, BookmarkViewSet,WrongDetail

user_list = UserViewSet.as_view({
    'get': 'list',
})
wrong_list = WrongViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
wrong_detail = WrongViewSet.as_view({
    'delete': 'destroy'
})
wrong_pr_detail = WrongDetail.as_view({
    'get': 'list',
})
bookmark_list = BookmarkViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
bookmark_detail = BookmarkViewSet.as_view({
    'delete': 'destroy'
})

urlpatterns = [
    path('user_list', user_list),
    path('wrong', wrong_list),
    path('wrong/<int:pk>', wrong_detail),
    path('detail', wrong_pr_detail),
    path('bookmark', bookmark_list),
    path('bookmark/<int:pk>', bookmark_detail),

]
