from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import EmailField, TextInput, CharField
from django.core.validators import EMPTY_VALUES


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
#         raise ValidationError('Please fill in the field below.')
# def null_form(self, form):
#     if form is '':
#         raise ('строка не может быть пустой')
#     else:
#         form.save()

class MyUserCreationForm(UserCreationForm):
    email = EmailField(required=True)
    # first_name = null_form(form)
    last_name = CharField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']

