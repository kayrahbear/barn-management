from backoffice.models import User, Group, GroupMember, Trainer, Horse, Lesson, Turnout, SuppsMeds, Feed
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = "__all__"

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"


class HorseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horse
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

class TurnoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turnout
        fields = "__all__"

class SuppsMedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuppsMeds
        fields = "__all__"

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"