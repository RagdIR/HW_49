# Generated by Django 2.2 on 2020-09-13 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20200910_1311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('change_group', 'Изменить состав группы')], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
    ]