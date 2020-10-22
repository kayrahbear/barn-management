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
    first_name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=15, null=True, blank=True)
    contact_num = models.CharField(max_length=15, null=True, blank=True)
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

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            self.save(update_fields=["password"])

        if raw_password is None:
            return False

        hasher = get_hasher("default")
        must_update = False
        if self.password.find('$') > 0:
            hasher = identify_hasher(self.password)
            must_update = True

        is_correct = hasher.verify(raw_password, self.password)
        if is_correct and must_update:
            self.set_password(raw_password)
            self.save(update_fields=["password"])

        return is_correct


class Group(models.Model):
    group_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    group_type = models.CharField(
        max_length=8,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.group_id}"

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"


class GroupMember(models.Model):
    member_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "GroupMember"
        verbose_name_plural = "GroupMembers"


class Trainer(models.Model):
    trainer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Trainer"
        verbose_name_plural = "Trainers"


class Horse(models.Model):
    horse_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stall_identifier = models.CharField(max_length=10, null=True, blank=True)
    horse_img = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)
    short_name = models.CharField(
        max_length=15,
    )
    show_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )
    breed = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )
    birth_year = models.CharField(
        max_length=4,
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    sex = models.CharField(
        max_length=8,
        null=True,
        blank=True,
    )
    lesson_horse = models.BooleanField(default=True)
    show_horse = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Horse"
        verbose_name_plural = "Horses"

    def __str__(self):
        return f"{self.short_name} | {self.breed} {self.sex}"


class Lesson(models.Model):
    lesson_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    horse_id = models.ForeignKey(Horse, on_delete=models.CASCADE)
    rider_id = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    lesson_time = models.DateTimeField()
    requested_date = models.DateTimeField()
    approved = models.BooleanField(default=False)
    lesson_length = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"


class Turnout(models.Model):
    turnout_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    horse_id = models.ForeignKey(Horse, on_delete=models.CASCADE)
    turnout_time = models.CharField(
        max_length=2,
        null=True,
        blank=True,
    )
    weekday = models.CharField(
        max_length=8,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Turnout"
        verbose_name_plural = "Turnouts"


class SuppsMeds(models.Model):
    supp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    horse_id = models.ForeignKey(Horse, on_delete=models.CASCADE)
    supp_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    supp_time = models.CharField(
        max_length=8,
        null=True,
        blank=True,
    )
    amount = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Supplement/Medication"
        verbose_name_plural = "Supplements/Medications"

    def __str__(self):
        return f"{self.supp_name} | {self.horse_id} {self.supp_time}"


class Feed(models.Model):
    feed_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    horse_id = models.ForeignKey(Horse, on_delete=models.CASCADE)
    grain = models.CharField(
        max_length=8,
        null=True,
        blank=True,
    )
    secondary_grain = models.CharField(
        max_length=8,
        null=True,
        blank=True,
    )
    grain_amount = models.FloatField(null=True, blank=True)
    second_grain_amount = models.FloatField(null=True, blank=True)
    hay = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    secondary_hay = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    hay_amount = models.FloatField(null=True, blank=True)
    second_hay_amount = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "Feed"
        verbose_name_plural = "Feeds"

    def __str__(self):
        return f"{self.horse_id}"
