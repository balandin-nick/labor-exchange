from enum import Enum
from pathlib import Path
from random import choice
from typing import List

from accounts.models import LaborExchangeUser
from companies.models import Company
from vacancies.models import Specialty, Vacancy


def _fill_specialties() -> None:
    class SpecialtyChoices(Enum):
        frontend = 'Фронтенд'
        backend = 'Бэкенд'
        gamedev = 'Геймдев'
        devops = 'Девопс'
        design = 'Дизайн'
        products = 'Продукты'
        management = 'Менеджмент'
        testing = 'Тестирование'

    specialty_logos_directory = Path('specialty_logos')
    for specialty_item in SpecialtyChoices:
        specialty_instance = Specialty(
            code=specialty_item.name,
            title=specialty_item.value,
            picture=str(specialty_logos_directory / f'specty_{specialty_item.name}.png')
        )
        specialty_instance.save()


def _fill_companies() -> None:
    company_logos_directory = Path('company_logos')
    company_names: List[str] = [
        'Workiro',
        'Rebel Rage',
        'Staffing Smarter',
        'Evilthreat',
        'Hirey',
        'SwiftAttack',
        'TROLLER',
        'Primal Assault',
    ]

    for index, companies_name in enumerate(company_names):
        owner: LaborExchangeUser
        is_created: bool

        owner, is_created = LaborExchangeUser.objects.get_or_create(
            name=f'Владелец',
            surname=f'Хозяинов_{index}',
            email=f'owner{index}@owner.ru',
            phone=f'8999777665{index}',
        )

        assert is_created, 'Admin was not created'
        owner.set_password(f'Djangotest{index}')
        owner.save()

        company_instance = Company(
            name=companies_name,
            location='Самый лучший город на Земле',
            logo=str(company_logos_directory / f'logo{index + 1}.png'),
            owner=owner,
            employee_count=choice(range(1, 300)),
            description='Это компания без описания, потому что её HR-специалисты — ленивые задницы',
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
                skills='Бэкенд, Старший (Senior), C#, ASP.NET MVC, MySQL, Git',
            )
            vacancy_instance.save()


def run():
    admin: LaborExchangeUser
    is_created: bool

    admin, is_created = LaborExchangeUser.objects.get_or_create(
        name='Эникей',
        surname='Логинов',
        email='admin@admin.ru',
        is_admin=True,
        is_superuser=True,
    )

    assert is_created, 'Admin was not created'
    admin.set_password('Qwerty12')
    admin.save()

    _fill_specialties()
    _fill_companies()
    _fill_vacancies()
