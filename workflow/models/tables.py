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
    URLField,
)

from labor_exchange.settings import AUTH_USER_MODEL

from .local_types import EducationChoices, GradeChoices, SpecialtyChoices, WorkStatusChoices


__all__ = [
    'Company',
    'Specialty',
    'Resume',
    'Vacancy',
    'VacancyResponse',
]


class Company(Model):
    name = CharField(verbose_name='Название', max_length=255)
    location = CharField(verbose_name='Локация', max_length=100)
    logo = ImageField(verbose_name='Логотип', upload_to='company_logos', null=True)
    owner = ForeignKey(
        to=AUTH_USER_MODEL,
        verbose_name='Владелец',
        on_delete=CASCADE,
        related_name='companies',
        unique=True,
    )
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


class Specialty(Model):
    code = CharField(
        verbose_name='Код',
        choices=[
            (str(specialty_item), specialty_item.value)
            for specialty_item in SpecialtyChoices
        ],
        max_length=50,
    )
    title = CharField(verbose_name='Наименование', max_length=100)
    picture = ImageField(
        verbose_name='Изображение',
        upload_to='specialty',
        height_field='148',
        width_field='148',
        null=True,
    )

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
        ordering = ['title']

    def __str__(self):
        return f'Специальность "{self.title}"'

    def delete(self, *args, **kwargs):
        self.picture.storage.delete(self.picture.path)
        super().delete(*args, **kwargs)


class Resume(Model):
    user = ForeignKey(
        to=AUTH_USER_MODEL,
        verbose_name='Специальность',
        on_delete=SET_NULL,
        null=True,
        related_name='resumes',
    )
    name = CharField(verbose_name='Имя', max_length=150)
    surname = CharField(verbose_name='Фамилия', max_length=150)
    salary = IntegerField(verbose_name='Вознаграждение', blank=True, null=True)
    status = CharField(
        verbose_name='Поисковый статус',
        choices=[
            (str(status_item), status_item.value)
            for status_item in WorkStatusChoices
        ],
        max_length=50,
    )
    specialty = ForeignKey(
        to=Specialty,
        verbose_name='Специализация',
        null=True,
        on_delete=SET_NULL,
        related_name='resumes',
    )
    grade = CharField(
        verbose_name='Квалификация',
        choices=[
            (str(grade_item), grade_item.value)
            for grade_item in GradeChoices
        ],
        max_length=50,
    )
    education = CharField(
        verbose_name='Образование',
        choices=[
            (str(education_item), education_item.value)
            for education_item in EducationChoices
        ],
        max_length=250,
    )
    experience = IntegerField(verbose_name='Опыт работы (лет)')
    portfolio = URLField(verbose_name='Портфолио', blank=True, null=True)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
        ordering = ['surname', 'name']

    def __str__(self):
        return f'{self.surname} {self.name}, резюме'


class Vacancy(Model):
    title = CharField(verbose_name='Наименование', max_length=255)
    specialty = ForeignKey(
        to=Specialty,
        verbose_name='Специальность',
        on_delete=SET_NULL,
        null=True,
        related_name='vacancies',
    )
    company = ForeignKey(to=Company, verbose_name='Компания', on_delete=CASCADE, related_name='vacancies')
    skills = TextField(verbose_name='Навыки')
    description = TextField(verbose_name='Описание')
    salary_min = IntegerField(verbose_name='Зарплата, нижняя граница')
    salary_max = IntegerField(verbose_name='Зарплата, верхняя граница')
    published_at = DateTimeField(verbose_name='Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['title']

    def __str__(self):
        return f'Вакансия "{self.title}"'

    def get_url(self) -> str:
        return f'/vacancies/{self.pk}'


class VacancyResponse(Model):
    covering_letter = TextField(verbose_name='Сопроводительное письмо')
    vacancy = ForeignKey(
        to='Vacancy',
        verbose_name='Вакансия',
        on_delete=CASCADE,
        related_name='applications',
    )
    user = ForeignKey(
        to='userflow.LaborExchangeUser',
        verbose_name='Пользователь',
        on_delete=CASCADE,
        related_name='applications',
    )

    class Meta:
        verbose_name = 'Отклик на вакансию'
        verbose_name_plural = 'Отклики на вакансии'
        ordering = ['vacancy', 'user']

    def __str__(self):
        return f'Отклик {self.user} на вакансию "{self.vacancy}"'
