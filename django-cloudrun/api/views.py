# *coding: utf-8*
from backoffice.models import User, Horse, Lesson
from api.serializers import UserSerializer, HorseSerializer, LessonSerializer
from rest_framework import generics


class UserListView(generics.ListAPIView):
    """
            get:
                Search or get users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HorseListView(generics.ListAPIView):
    """
            get:
                Search or get users
    """
    queryset = Horse.objects.all()
    serializer_class = HorseSerializer

class LessonListView(generics.ListAPIView):
    """
            get:
                Search or get users
    """
    queryset = Horse.objects.all()
    serializer_class = LessonSerializer