from enum import Enum


__all__ = [
    'EducationChoices',
    'GradeChoices',
    'SpecialtyChoices',
    'WorkStatusChoices',
]


class EducationChoices(Enum):
    missing = 'Отсутствует'
    secondary = 'Среднее'
    vocational = 'Средне-специальное'
    incomplete_higher = 'Неполное высшее'
    higher = 'Высшее'


class GradeChoices(Enum):
    intern = 'intern'
    junior = 'junior'
    middle = 'middle'
    senior = 'senior'
    lead = 'lead'


class SpecialtyChoices(Enum):
    frontend = 'frontend'
    backend = 'backend'
    gamedev = 'gamedev'
    devops = 'devops'
    design = 'design'
    products = 'products'
    management = 'management'
    testing = 'testing'


class WorkStatusChoices(Enum):
    not_in_search = 'Не ищу работу'
    consideration = 'Рассматриваю предложения'
    in_search = 'Ищу работу'
