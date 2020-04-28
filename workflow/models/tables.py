from autoslug import AutoSlugField
from django.db.models import (
    CASCADE,
    SET_NULL,
    CharField,
    DateTimeField,
    ForeignKey,
    ImageField,
    IntegerField,
    Model,
    TextField,
)

from .local_types import SpecialtyChoices


__all__ = [
    'Company',
    'Specialty',
    'Vacancy',
]


class Company(Model):
    name = CharField(verbose_name='Название', max_length=255)
    location = CharField(verbose_name='Локация', max_length=100)
    logo = ImageField(
        verbose_name='Логотип',
        upload_to='company_logos',
        height_field='205',
        width_field='396',
        null=True,
    )
    description = TextField(verbose_name='Описание')
    employee_count = IntegerField(verbose_name='Количество сотрудников', null=True)

    def delete(self, *args, **kwargs):
        self.logo.storage.delete(self.logo.path)
        super().delete(*args, **kwargs)


class Specialty(Model):
    code = CharField(
        verbose_name='Код',
        choices=[
            (str(specialty_item), specialty_item.value)
            for specialty_item in SpecialtyChoices
        ],
        max_length=50,
    )
    title = CharField(verbose_name='Наименование', max_length=50)
    picture = ImageField(
        verbose_name='Изображение',
        upload_to='specialty',
        height_field='148',
        width_field='148',
        null=True,
    )

    def delete(self, *args, **kwargs):
        self.picture.storage.delete(self.picture.path)
        super().delete(*args, **kwargs)


class Vacancy(Model):
    title = CharField(verbose_name='Наименование', max_length=255)
    slug = AutoSlugField(verbose_name='Кодовое имя', populate_from='title', always_update=True, unique=True)
    specialty = ForeignKey(to=Specialty, verbose_name='Специальность', on_delete=SET_NULL, null=True)
    company = ForeignKey(to=Company, verbose_name='Компания', on_delete=CASCADE)
    skills = TextField(verbose_name='Навыки')
    description = TextField(verbose_name='Описание')
    salary_min = IntegerField(verbose_name='Зарплата, нижняя граница')
    salary_max = IntegerField(verbose_name='Зарплата, верхняя граница')
    published_at = DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
