# Generated by Django 2.2 on 2020-08-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
    ]
