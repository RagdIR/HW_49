from django.db import models
from django.core.validators import MinLengthValidator


class Task(models.Model):
    summary = models.CharField(max_length=300, null=False, blank=False, verbose_name='Краткое описание',
                               validators=[MinLengthValidator(3)])
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание',
                                   validators=[MinLengthValidator(20)])
    type = models.ManyToManyField('webapp.Type', related_name='type', verbose_name='Тип')
    status = models.ForeignKey('webapp.Status', related_name='status',
                               on_delete=models.PROTECT, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

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