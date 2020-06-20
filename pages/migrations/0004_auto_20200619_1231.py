# Generated by Django 3.0.7 on 2020-06-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200619_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='selection_mode',
            field=models.IntegerField(choices=[(1, 'All Available'), (2, 'Least Busy'), (3, 'Random')], help_text='Determines how the Agent will get selected for the issue.'),
        ),
    ]
