# Generated by Django 2.2 on 2020-08-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='type',
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ManyToManyField(related_name='type', to='webapp.Type', verbose_name='Тип'),
        ),
    ]
