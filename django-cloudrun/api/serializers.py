from backoffice.models import User, Horse, Lesson
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class HorseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horse
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
