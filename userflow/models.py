from django.contrib.auth.models import User
from django.db.models import CharField, Model


__all__ = [
    'LaborExchangeUser',
]


class LaborExchangeUser(User):
    phone = CharField(verbose_name='Телефон', max_length=12)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'Пользователь {self.last_name} {self.first_name}'
