# Generated by Django 3.0.7 on 2020-06-20 05:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='available_since',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]