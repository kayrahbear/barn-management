# *coding: utf-8*
from backoffice.models import User, Horse, Lesson
from api.serializers import UserSerializer, HorseSerializer, LessonSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class UserCreateOrView(generics.ListCreateAPIView):
    """
        create:
            add users
        get:
            Search or get users
            You can search using:
                :param email
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('email', 'first_name')

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
            get:
                get a specific user
            delete:
                Remove an existing user.
            patch:
                Update one or more fields on an existing user.
            put:
                Update a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HorseCreateOrView(generics.ListCreateAPIView):
    """
            create:
                add horses
            get:
                Search or get horses
                You can search using:
                    :param short_name
                    :param show_name
                    :param lesson_horse
    """
    queryset = Horse.objects.all()
    serializer_class = HorseSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('short_name', 'show_name', 'lesson_horse')

class LessonCreateOrView(generics.ListCreateAPIView):
    """
            create:
                add lessons
            get:
                Search or get lessons
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer