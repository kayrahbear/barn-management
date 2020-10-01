from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, GroupViewSet, GroupMemberViewSet,TrainerViewSet, HorseViewSet, LessonViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'groupmembers', GroupMemberViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'horses', HorseViewSet)
router.register(r'lessons', LessonViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
