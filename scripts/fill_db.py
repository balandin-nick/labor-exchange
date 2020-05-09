from pathlib import Path
from random import choice
from typing import List

from django.contrib.auth.models import User
from workflow.models import Company, Specialty, Vacancy
from workflow.models.local_types import SpecialtyChoices

from accounts.models import LaborExchangeUser
from labor_exchange.settings import BASE_DIR, MEDIA_ROOT


MEDIA_DIRECTORY = Path(BASE_DIR) / MEDIA_ROOT / 'company_logos'


def _fill_specialties() -> None:
    for specialty_item in SpecialtyChoices:
        specialty_instance = Specialty(
            code=specialty_item,
            title=specialty_item.value,
        )
        specialty_instance.save()


def _fill_companies() -> None:
    company_names: List[str] = [
        'workiro',
        'rebelrage',
        'staffingsmarter',
        'evilthreat h',
        'hirey ',
        'swiftattack',
        'troller',
        'primalassault',
    ]

    for index, companies_name in enumerate(company_names):
        owner: LaborExchangeUser
        was_created: bool

        owner, was_created = LaborExchangeUser.objects.get_or_create(
            username=f'owner{index}',
            first_name=f'Owner_{index}',
            last_name=f'Ownerov_{index}',
            email=f'owner{index}@owner.ru',
            phone=f'8999777665{index}',
            password=f'Djangotest{index}',
        )

        company_instance = Company(
            name=companies_name,
            location='Самый лучший город на Земле',
            logo=str(MEDIA_DIRECTORY / f'logo{index}.png'),
            owner=owner,
            description='Это компания без описания, потому что её HR специалисты — ленивые задницы',
        )
        company_instance.save()


def _fill_vacancies():
    vacancy_titles: List[str] = [
        'Разработчик на Python',
        'Разработчик в проект на Django',
        'Разработчик на Swift в аутсорс компанию',
        'Мидл программист на Python',
        'Питонист в стартап',
    ]

    for company in Company.objects.all():
        specialty_list = Specialty.objects.all()
        number_of_specialties: int = len(specialty_list)

        number_of_vacancies: int = choice(range(1, 4))
        for index in range(number_of_vacancies):
            specialty: Specialty = specialty_list[choice(range(number_of_specialties))]
            salary_min = choice(range(10, 20)) * 10000

            vacancy_instance = Vacancy(
                title=choice(vacancy_titles),
                specialty=specialty,
                company=company,
                description=f'Описание вакансии №{index} для компании {company.name}',
                salary_min=salary_min,
                salary_max=salary_min + choice(range(1, 10)) * 10000,
            )
            vacancy_instance.save()


def run():
    User.objects.get_or_create(
        username=f'admin',
        email=f'admin@admin.ru',
        password=f'Qwerty12',
        is_superuser=True,
    )

    _fill_specialties()
    _fill_companies()
    _fill_vacancies()
