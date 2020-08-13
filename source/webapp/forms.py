from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from .models import Task


def at_least_3(string):
    if len(string) < 3:
        raise ValidationError('Слишком короткая запись! Должно быть не меньше 3 символов!')

def at_least_20(string):
    if len(string) < 20:
        raise ValidationError('Слишком короткая запись! Должно быть не меньше 20 символов!')


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'У записи "%(value)" символов %(show_value) ! Должно быть не меньше %(limit_value) символов!'
    code = 'too_short'

    def compare(self, value, limit):
        return value < limit

    def clean(self, value):
        return len(value)


class TaskForm(forms.ModelForm):

    #
    # summary = forms.CharField(max_length=300, required=True, label='Краткое описание',
    #                           validators=(at_least_3,))
    # description = forms.CharField(max_length=3000, required=False, label='Описание', widget=forms.Textarea,
    #                               validators=(at_least_20))
    class Meta:
        model = Task
        fields = ['summary', 'description', 'type', 'status']
        widgets = {'type': forms.CheckboxSelectMultiple}

    def clean(self):
        cleaned_data = super().clean()
        # print(cleaned_data['summary']) ## отладка
        # print(cleaned_data['description']) ## отладка
        # print(cleaned_data['summary'] == cleaned_data['description']) ## отладка
        if cleaned_data['summary'] == cleaned_data['description']:
            raise ValidationError("Нельзя, чтобы краткое описание совпадало с описанием")
        return cleaned_data





