from django.db import models
from .validations import symbols_3, symbols_20


class Project(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False, verbose_name='Название',
                               validators=[symbols_3])
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание',
                                   validators=[symbols_20])
    start_date_at = models.DateField(verbose_name="Дата начала", blank=False)
    end_date_at = models.DateField(verbose_name="Дата окончания", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'



class Task(models.Model):
    summary = models.CharField(max_length=300, null=False, blank=False, verbose_name='Краткое описание',
                               validators=[symbols_3])
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание',
                                   validators=[symbols_20])
    type = models.ManyToManyField('webapp.Type', related_name='type', verbose_name='Тип')
    status = models.ForeignKey('webapp.Status', related_name='status',
                               on_delete=models.PROTECT, verbose_name='Статус')
    project = models.ForeignKey('webapp.Project', related_name='project',
                                verbose_name='Проект', default=1, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')


    def __str__(self):
        return self.summary

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Type(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Status(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'