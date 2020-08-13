from django import forms
from .models import Status, Type, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'type', 'status']
        widgets = {'type': forms.CheckboxSelectMultiple}


    # summary = forms.CharField(max_length=300, required=True, label='Краткое описание')
    # description = forms.CharField(max_length=3000, required=False, label='Описание', widget=forms.Textarea)
    # type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=True, label='Тип', )
    # status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус')


