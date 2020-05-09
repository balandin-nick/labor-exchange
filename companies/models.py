from __future__ import annotations

from typing import Optional

from django.db.models import CASCADE, CharField, ForeignKey, ImageField, IntegerField, Model, TextField

from labor_exchange.settings import AUTH_USER_MODEL


__all__ = [
    'Company',
]


class Company(Model):
    name = CharField(verbose_name='Название', max_length=255)
    location = CharField(verbose_name='Локация', max_length=100)
    logo = ImageField(verbose_name='Логотип', upload_to='company_logos', null=True)
    owner = ForeignKey(to=AUTH_USER_MODEL, verbose_name='Владелец', on_delete=CASCADE, related_name='companies')
    employee_count = IntegerField(verbose_name='Количество сотрудников', null=True)
    description = TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['name']

    def __str__(self):
        return f'Компания "{self.name}"'

    def delete(self, *args, **kwargs):
        self.logo.storage.delete(self.logo.path)
        super().delete(*args, **kwargs)

    def get_url(self) -> str:
        return f'/companies/{self.id}'

    def get_absolute_url(self) -> str:
        return self.get_url()

    @classmethod
    def get_user_company(cls, user: AUTH_USER_MODEL) -> Optional[Company]:
        try:
            return cls.objects.filter(owner=user).all()[0]
        except IndexError:
            return None
