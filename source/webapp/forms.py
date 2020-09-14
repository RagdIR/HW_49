from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from .models import Task, Project


BROWSER_DATE_FORMAT = '%d.%m.%Y'


class XDatepickerWidget(forms.TextInput):
    template_name = 'widgets/xdatepicker_widget.html'

@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'У записи "%(value)" символов %(show_value) ! Должно быть не меньше %(limit_value) символов!'
    code = 'too_short'

    def compare(self, value, limit):
        return value < limit

    def clean(self, value):
        return len(value)


class ProjectForm(forms.ModelForm):
    start_date_at = forms.DateTimeField(required=False, label='Дата начала',
                                     input_formats=['%Y-%m-%d', BROWSER_DATE_FORMAT],
                                     widget=XDatepickerWidget)

    end_date_at = forms.DateTimeField(required=False, label='Дата окончания',
                                     input_formats=['%Y-%m-%d', BROWSER_DATE_FORMAT],
                                     widget=XDatepickerWidget)

    # start_date_at = forms.DateField(required=False, label='Дата начала',
    #                                  input_formats=['%Y-%m-%d', BROWSER_DATE_FORMAT])
    #
    # end_date_at = forms.DateField(required=False, label='Дата окончания',
    #                                  input_formats=['%Y-%m-%d', BROWSER_DATE_FORMAT])
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date_at', 'end_date_at']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'type', 'status']
        widgets = {'type': forms.CheckboxSelectMultiple}

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['summary'] == cleaned_data['description']:
            raise ValidationError("Нельзя, чтобы краткое описание совпадало с описанием")
        return cleaned_data


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class ProjectUserForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['user']





