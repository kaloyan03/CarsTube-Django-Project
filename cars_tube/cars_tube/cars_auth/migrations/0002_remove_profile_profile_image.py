# Generated by Django 4.0 on 2022-01-03 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_image',
        ),
    ]
