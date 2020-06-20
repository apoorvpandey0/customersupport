# Generated by Django 3.0.7 on 2020-06-19 12:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0009_profile_is_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_resolved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Profile')),
                ('issue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.Issue')),
            ],
        ),
    ]