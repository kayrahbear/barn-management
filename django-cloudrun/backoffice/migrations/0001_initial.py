# Generated by Django 3.1.1 on 2020-09-29 04:04

import backoffice.UserManager
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "user_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "user_img",
                    models.ImageField(
                        blank=True, null=True, upload_to="media/%Y/%m/%d"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("first_name", models.CharField(blank=True, max_length=15, null=True)),
                ("last_name", models.CharField(blank=True, max_length=15, null=True)),
                ("facebookId", models.CharField(blank=True, max_length=100, null=True)),
                ("android", models.BooleanField(default=False)),
                ("ios", models.BooleanField(default=False)),
                ("acceptPush", models.BooleanField(default=False)),
                ("pushToken", models.CharField(blank=True, max_length=100, null=True)),
                ("is_active", models.BooleanField(default=True, verbose_name="active")),
                ("is_staff", models.BooleanField(default=False, verbose_name="staff")),
                ("valid", models.BooleanField(default=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
            managers=[
                ("objects", backoffice.UserManager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "group_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("group_name", models.CharField(blank=True, max_length=20, null=True)),
                ("group_type", models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                "verbose_name": "Group",
                "verbose_name_plural": "Groups",
            },
        ),
        migrations.CreateModel(
            name="Horse",
            fields=[
                (
                    "horse_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "stall_identifier",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "horse_img",
                    models.ImageField(
                        blank=True, null=True, upload_to="media/%Y/%m/%d"
                    ),
                ),
                ("short_name", models.CharField(max_length=15)),
                ("show_name", models.CharField(blank=True, max_length=25, null=True)),
                ("breed", models.CharField(blank=True, max_length=25, null=True)),
                ("birth_year", models.CharField(blank=True, max_length=4, null=True)),
                ("sex", models.CharField(blank=True, max_length=8, null=True)),
                ("lesson_horse", models.BooleanField(default=True)),
                ("show_horse", models.BooleanField(default=True)),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Horse",
                "verbose_name_plural": "Horses",
            },
        ),
        migrations.CreateModel(
            name="SuppsMeds",
            fields=[
                (
                    "supp_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("supp_name", models.CharField(blank=True, max_length=8, null=True)),
                ("amount", models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                "verbose_name": "Supplement/Medication",
                "verbose_name_plural": "Supplements/Medications",
            },
        ),
        migrations.CreateModel(
            name="Turnout",
            fields=[
                (
                    "turnout_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("turnout_time", models.CharField(blank=True, max_length=2, null=True)),
                ("weekday", models.CharField(blank=True, max_length=8, null=True)),
                (
                    "horse_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backoffice.horse",
                    ),
                ),
            ],
            options={
                "verbose_name": "Turnout",
                "verbose_name_plural": "Turnouts",
            },
        ),
        migrations.CreateModel(
            name="Trainer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "group_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backoffice.group",
                    ),
                ),
                (
                    "trainer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Trainer",
                "verbose_name_plural": "Trainers",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "lesson_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("lesson_time", models.DateTimeField()),
                ("requested_date", models.DateTimeField()),
                ("approved", models.BooleanField(default=False)),
                ("lesson_length", models.FloatField(blank=True, null=True)),
                (
                    "horse_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backoffice.horse",
                    ),
                ),
                (
                    "rider_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "trainer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backoffice.trainer",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lesson",
                "verbose_name_plural": "Lessons",
            },
        ),
        migrations.CreateModel(
            name="GroupMember",
            fields=[
                (
                    "member_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "group_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backoffice.group",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "GroupMember",
                "verbose_name_plural": "GroupMembers",
            },
        ),
        migrations.CreateModel(
            name="Feed",
            fields=[
                (
                    "feed_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("feed_time", models.CharField(max_length=2)),
                ("grain_amount", models.FloatField(blank=True, null=True)),
                ("grain", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "horse_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backoffice.horse",
                    ),
                ),
                (
                    "supp_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backoffice.suppsmeds",
                    ),
                ),
            ],
            options={
                "verbose_name": "Feed",
                "verbose_name_plural": "Feeds",
            },
        ),
    ]
