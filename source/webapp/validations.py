from django.core.exceptions import ValidationError


def symbols_3(string):
    if len(string) < 3:
        raise ValidationError('Слишком короткая запись!!!')


def symbols_20(string):
    if len(string) < 20:
        raise ValidationError('Слишком короткая запись!!! В описании должно быть не меньше 20 символов')