from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from api.views import *

router = DefaultRouter()
router.register(r'', UserViewSet)
router.register(r'', GroupViewSet)
router.register(r'', GroupMemberViewSet)
router.register(r'', TrainerViewSet)
router.register(r'', HorseViewSet)
router.register(r'', LessonViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
