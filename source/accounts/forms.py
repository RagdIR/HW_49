from django.contrib.auth import get_user_model
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
from accounts.models import Profile


class MyUserCreationForm(UserCreationForm):
    email = EmailField(required=True)
    # first_name = null_form(form)
    last_name = CharField(required=True)
    url_profile = forms.URLField(label='Ссылка на GitHub', required=False)

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label="Новый пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label="Старый пароль", strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неправильный!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['password', 'password_confirm', 'old_password']