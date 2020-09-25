from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from api.views import UserListView, HorseListView, LessonListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='users_list'),
    path('horses/', HorseListView.as_view(), name='horses_list'),
    path('lessons/', LessonListView.as_view(), name='lessons_list'),
    path('', include(router.urls))
]