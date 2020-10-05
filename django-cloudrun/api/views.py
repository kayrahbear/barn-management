# *coding: utf-8*
from django.contrib.auth.models import Group
from backoffice.models import *
from api.serializers import *
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("email", "password")


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("group_name",)


class GroupMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        "email",
        "group_name",
    )


class TrainerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("email",)


class HorseViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]
    queryset = Horse.objects.all()
    serializer_class = HorseSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("short_name", "show_name", "lesson_horse")


class LessonViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        "horse_id",
        "rider_id",
        "trainer_id",
        "lesson_time",
        "approved",
    )
