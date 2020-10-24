# Generated by Django 3.1.1 on 2020-10-22 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0003_auto_20201022_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='second_grain_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='second_hay_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='secondary_grain',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='secondary_hay',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]