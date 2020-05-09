from django.contrib import admin

from .models import Specialty, Vacancy


__all__ = [
    'Specialty',
    'Vacancy',
]


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass
