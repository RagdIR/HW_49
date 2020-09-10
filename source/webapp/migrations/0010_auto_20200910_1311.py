# Generated by Django 2.2 on 2020-09-10 07:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_project_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]