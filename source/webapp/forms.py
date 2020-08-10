from django import forms
from .models import Task, Status, Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=300, required=True, label='Краткое описание')
    description = forms.CharField(max_length=3000, required=False, label='Описание', widget=forms.Textarea)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, label='Тип')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус')