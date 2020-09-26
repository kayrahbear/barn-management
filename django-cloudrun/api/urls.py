from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
from api.views import UserCreateOrView, HorseCreateOrView, LessonCreateOrView

urlpatterns = [
    path("users/", UserCreateOrView.as_view(), name="users_list"),
    path("user/<uuid:pk>/", UserCreateOrView.as_view(), name="user_detail"),
    path("horses/", HorseCreateOrView.as_view(), name="horses_list"),
    path("lessons/", LessonCreateOrView.as_view(), name="lessons_list"),
    path("", include(router.urls)),
]
