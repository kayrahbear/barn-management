from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from api.views import (
    UserViewSet,
    GroupViewSet,
    GroupMemberViewSet,
    TrainerViewSet,
    HorseViewSet,
    LessonViewSet,
    TurnoutViewSet,
    SuppsMedsViewSet,
    FeedViewSet
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"groupmembers", GroupMemberViewSet)
router.register(r"trainers", TrainerViewSet)
router.register(r"horses", HorseViewSet)
router.register(r"lessons", LessonViewSet)
router.register(r"turnouts", TurnoutViewSet)
router.register(r"supplements", SuppsMedsViewSet)
router.register(r"feeds", FeedViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
