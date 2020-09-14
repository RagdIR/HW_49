# Generated by Django 2.2 on 2020-09-14 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import webapp.validations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0011_auto_20200913_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='Аватар')),
                ('url_profile', models.URLField(blank=True, verbose_name='Профиль на GitHub')),
                ('about', models.TextField(max_length=3000, validators=[webapp.validations.symbols_20], verbose_name='О себе')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
