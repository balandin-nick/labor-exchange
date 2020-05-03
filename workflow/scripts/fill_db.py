from pathlib import Path

from labor_exchange.settings import BASE_DIR, MEDIA_ROOT
from userflow.models import LaborExchangeUser
from workflow.models import Company, Resume, Specialty, Vacancy, VacancyResponse
from workflow.models.local_types import EducationChoices, GradeChoices, SpecialtyChoices, WorkStatusChoices


MEDIA_DIRECTORY = Path(BASE_DIR) / MEDIA_ROOT / 'company_logos'


jobs = [
    {
        'title': 'Разработчик на Python',
        'cat': 'backend',
        'company': 'staffingsmarter',
        'salary_from': '100000',
        'salary_to': '150000',
        'posted': '2020-03-11',
        'desc': 'Потом добавим',
    },
    {
        'title': 'Разработчик в проект на Django',
        'cat': 'backend',
        'company': 'swiftattack',
        'salary_from': '80000',
        'salary_to': '90000',
        'posted': '2020-03-11',
        'desc': 'Потом добавим',
    },
    {
        'title': 'Разработчик на Swift в аутсорс компанию',
        'cat': 'backend',
        'company': 'swiftattack',
        'salary_from': '120000',
        'salary_to': '150000',
        'posted': '2020-03-11',
        'desc': 'Потом добавим',
    },
    {
        'title': 'Мидл программист на Python',
        'cat': 'backend',
        'company': 'workiro',
        'salary_from': '80000',
        'salary_to': '90000',
        'posted': '2020-03-11',
        'desc': 'Потом добавим',
    },
    {
        'title': 'Питонист в стартап',
        'cat': 'backend',
        'company': 'primalassault',
        'salary_from': '120000',
        'salary_to': '150000',
        'posted': '2020-03-11',
        'desc': 'Потом добавим',
    }
]

companies = [
    {'title': 'workiro'},
    {'title': 'rebelrage'},
    {'title': 'staffingsmarter'},
    {'title': 'evilthreat h'},
    {'title': 'hirey '},
    {'title': 'swiftattack'},
    {'title': 'troller'},
    {'title': 'primalassault'}
]

specialties = [
    {'code': 'frontend', 'title': 'Фронтенд'},
    {'code': 'backend', 'title': 'Бэкенд'},
    {'code': 'gamedev', 'title': 'Геймдев'},
    {'code': 'devops', 'title': 'Девопс'},
    {'code': 'design', 'title': 'Дизайн'},
    {'code': 'products', 'title': 'Продукты'},
    {'code': 'management', 'title': 'Менеджмент'},
    {'code': 'testing', 'title': 'Тестирование'}
]


def _fill_specialties() -> None:
    for specialty_item in SpecialtyChoices:
        specialty_instance = Specialty(
            code=specialty_item,
            title=specialty_item.value,
        )
        specialty_instance.save()


def _fill_companies(owner: LaborExchangeUser) -> None:
    for index, companies_item in enumerate(companies):
        company_instance = Company(
            name=companies_item['title'],
            location='Жопа мира',
            logo=str(MEDIA_DIRECTORY / f'logo{index}.png'),
            owner=owner,
            description='Это компания без описания, потому что её HR — ленивые задницы',
        )
        company_instance.save()


def run():
    ivan = LaborExchangeUser(
        username='topor',
        first_name='Иван',
        last_name='Торопыжкин',
        email='ivan@torop.ru',
        phone='89997776655',
        password='Torop1234',
    )
    ivan.save()

    _fill_specialties()
    _fill_companies(ivan)

    # for jobs_item in jobs:
    #     specialty = Specialty.objects.filter(code=SpecialtyChoices(jobs_item['cat'])).first()
    #     if not specialty:
    #         continue
    #
    #     company = Company.objects.filter(name=jobs_item['company']).first()
    #     if not company:
    #         continue
    #
    #     vacancy_instance = Vacancy(
    #         title=jobs_item['title'],
    #         specialty=specialty,
    #         company=company,
    #         description=jobs_item['desc'],
    #         salary_min=jobs_item['salary_from'],
    #         salary_max=jobs_item['salary_to'],
    #         published_at=jobs_item['posted'],
    #     )
    #     vacancy_instance.save()
