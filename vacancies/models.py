from typing import List

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

from companies.models import Company
from labor_exchange.settings import MEDIA_SPECIALITY_IMAGE_DIR


__all__ = [
    'Specialty',
    'Vacancy',
]


class Specialty(Model):
    code = CharField(verbose_name='Код', max_length=50, unique=True)
    title = CharField(verbose_name='Наименование', max_length=100)
    picture = ImageField(verbose_name='Изображение', upload_to=MEDIA_SPECIALITY_IMAGE_DIR, null=True)

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
        ordering = ['title']

    def __str__(self):
        return f'Специальность "{self.title}"'

    def delete(self, *args, **kwargs):
        self.picture.storage.delete(self.picture.path)
        super().delete(*args, **kwargs)


class Vacancy(Model):
    title = CharField(verbose_name='Наименование', max_length=255)
    specialty = ForeignKey(
        to=Specialty,
        verbose_name='Специальность',
        null=True,
        on_delete=SET_NULL,
        related_name='vacancies',
    )
    company = ForeignKey(to=Company, verbose_name='Компания', on_delete=CASCADE, related_name='vacancies')
    salary_min = IntegerField(verbose_name='Зарплата, нижняя граница', null=True, blank=True)
    salary_max = IntegerField(verbose_name='Зарплата, верхняя граница', null=True, blank=True)
    skills = TextField(verbose_name='Навыки', null=True, blank=True)
    description = TextField(verbose_name='Описание')
    published_at = DateTimeField(verbose_name='Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['published_at']

    @property
    def skill_list(self) -> List[str]:
        return self.skills and [skill.strip() for skill in self.skills.split(',')] or []

    def __str__(self):
        return f'Вакансия "{self.title}"'

    def get_url(self) -> str:
        return f'/vacancies/{self.pk}'

    def get_absolute_url(self) -> str:
        return self.get_url()
