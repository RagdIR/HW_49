from django.db import models
from django.contrib.auth import get_user_model
from webapp.validations import symbols_3, symbols_20


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    url_profile = models.URLField(blank=True, verbose_name='Профиль на GitHub')
    about = models.TextField(max_length=3000, null=False, blank=False, verbose_name='О себе',
                                   validators=[symbols_20])

    def __str__(self):
        return "Профиль" + self.user.get_full_name()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        permissions = {('perm_user', 'разрешение пользователя')}
