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

from .local_types import GradeChoices, SpecialtyChoices, WorkStatusChoices


__all__ = [
    'Company',
    'Specialty',
    'Vacancy',
]


class Application(Model):
    username = CharField(verbose_name='Имя', max_length=255)
    phone = CharField(verbose_name='Телефон', max_length=12)
    covering_letter = TextField(verbose_name='Сопроводительное письмо')
    vacancy = ForeignKey(
        to='Vacancy',
        verbose_name='Вакансия',
        on_delete=CASCADE,
        related_name='applications',
    )
    user = ForeignKey(
        to='LaborExchangeUser',
        verbose_name='Пользователь',
        on_delete=CASCADE,
        related_name='applications',
    )


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
    owner = ForeignKey(to='LaborExchangeUser', verbose_name='Владелец', on_delete=CASCADE, related_name='companies')
    employee_count = IntegerField(verbose_name='Количество сотрудников', null=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['name']

    def __str__(self):
        return f'Компания "{self.name}"'

    def delete(self, *args, **kwargs):
        self.logo.storage.delete(self.logo.path)
        super().delete(*args, **kwargs)


class Resume(Model):
    user = ForeignKey(
        to='LaborExchangeUser',
        verbose_name='Специальность',
        on_delete=SET_NULL,
        null=True,
        related_name='vacancies',
    )
    name = CharField(verbose_name='Имя', max_length=150)
    surname = CharField(verbose_name='Фамилия', max_length=150)
    status = CharField(
        verbose_name='Поисковый статус',
        choices=[
            (str(status_item), status_item.value)
            for status_item in WorkStatusChoices
        ],
        max_length=50,
    )
    salary = IntegerField(verbose_name='Вознаграждение')
    specialty = ForeignKey(
        to='Specialty',
        verbose_name='Специализация',
        on_delete=SET_NULL,
        related_name='resumes',
    )
    grade = CharField(
        verbose_name='Квалификация',
        choices=[
            (str(grade_item), grade_item.value)
            for grade_item in GradeChoices
        ],
        max_length=10,
    )
    education = CharField(verbose_name='Образование', max_length=250)
    expirience = IntegerField(verbose_name='Опыт работы')
    portfolio = TextField(verbose_name='Портфолио')


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
