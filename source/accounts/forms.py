from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import EmailField, TextInput, CharField
from django.core.validators import EMPTY_VALUES
from django import forms


# class EmailField(forms.EmailField):
#     def __init__(self, *args, **kwargs):
#         super(EmailField, self).__init__(*args, strip=True, **kwargs)
#
#     def clean(self,value):
#         if value in EMPTY_VALUES:
#             raise Exception('Email обязателен')
#         value = self.value.strip()
#         return super(EmailField, self).clean(value)

# def null_form(self):
#     if self.object == '':
#         raise ValidationError('Это поле должно быть заполнено.')


# def null_form(self, form):
#     if form is '':
#         raise ('строка не может быть пустой')
#     else:
#         form.save()

class MyUserCreationForm(UserCreationForm):
    email = EmailField(required=True)
    # first_name = null_form(form)
    last_name = CharField(required=True)
    url_profile = forms.URLField(label='Ссылка на GitHub', required=False)

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email', 'url_profile']

