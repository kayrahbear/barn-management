from django.db import models
from django.core.files import File
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from .UserManager import UserManager
from django.contrib.auth.hashers import get_hasher, identify_hasher
import uuid


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_img = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)
    email = models.EmailField(
        unique=True,
    )
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    facebookId = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    android = models.BooleanField(default=False)
    ios = models.BooleanField(default=False)
    acceptPush = models.BooleanField(default=False)
    pushToken = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(("active"), default=True)
    is_staff = models.BooleanField(("staff"), default=False)
    valid = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Horse(models.Model):
    horse_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    horse_img = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)
    short_name = models.CharField(
        max_length=100,
    )
    show_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    breed = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    birth_year = models.CharField(
        max_length=4,
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sex = models.CharField(
        max_length=4,
        null=True,
        blank=True,
    )
    lesson_horse = models.BooleanField(default=True)
    show_horse = models.BooleanField(default=True)
    stall_number = models.IntegerField(blank=True)

    class Meta:
        verbose_name = "Horse"
        verbose_name_plural = "Horses"


class Lesson(models.Model):
    lesson_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    horse_id = models.ForeignKey(Horse, on_delete=models.CASCADE)
    rider_id = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_time = models.DateTimeField()
    requested_date = models.DateTimeField()
    approved = models.BooleanField(default=False)
    lesson_length = models.FloatField(null=True)

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
