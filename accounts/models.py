from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import BooleanField, CharField, EmailField, Model

from .managers import LaborExchangeUserManager


__all__ = [
    'LaborExchangeUser',
]


class LaborExchangeUser(AbstractBaseUser, PermissionsMixin):
    name = CharField(verbose_name='Имя', max_length=50)
    surname = CharField(verbose_name='Фамилия', max_length=50)
    email = EmailField(verbose_name='E-mail', max_length=254, unique=True)
    phone = CharField(verbose_name='Телефон', max_length=12, blank=True, null=True)

    is_active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    is_superuser = BooleanField(default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['surname', 'name', 'email']

    objects = LaborExchangeUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name', 'surname')

    def __str__(self):
        return f'Пользователь {self.surname} {self.name}'

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_short_name(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_admin
