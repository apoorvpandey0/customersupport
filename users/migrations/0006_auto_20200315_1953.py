# Generated by Django 3.0.2 on 2020-03-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200315_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address_line1',
            field=models.CharField(help_text='Designates the users Address line1.', max_length=100, verbose_name='Address line 1'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_line2',
            field=models.CharField(help_text='Designates the users Address line 2.', max_length=100, verbose_name='Address line 2'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', help_text='Designates the users Profile picture.', upload_to='profile_pics', verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pincode',
            field=models.CharField(help_text='Designates the users PINCODE.', max_length=6, verbose_name='Pincode'),
        ),
    ]
