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
    frontend = 'Фронтенд'
    backend = 'Бэкенд'
    gamedev = 'Геймдев'
    devops = 'Девопс'
    design = 'Дизайн'
    products = 'Продукты'
    management = 'Менеджмент'
    testing = 'Тестирование'


class WorkStatusChoices(Enum):
    not_in_search = 'Не ищу работу'
    consideration = 'Рассматриваю предложения'
    in_search = 'Ищу работу'
