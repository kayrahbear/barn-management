# *coding: utf-8*
from django.contrib.auth.models import Group
from backoffice.models import *
from api.serializers import *
from rest_framework import generics, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("email", "password")


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("group_name",)


class GroupMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        "email",
        "group_name",
    )


class TrainerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("email",)


class HorseViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Horse.objects.all()
    serializer_class = HorseSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("short_name", "show_name", "lesson_horse")


class LessonViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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

class TurnoutViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Turnout.objects.all()
    serializer_class = TurnoutSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        "horse_id",
        "turnout_time",
        "weekday"
    )

class SuppsMedsViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SuppsMeds.objects.all()
    serializer_class = SuppsMedsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        "horse_id",
        "supp_time",
        "supp_name"
    )

class FeedViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        "horse_id",
    )