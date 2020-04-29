from django.contrib import admin
from .models.tables import Company, Specialty, Vacancy


__all__ = [
    'CompanyAdmin',
    'SpecialtyAdmin',
    'VacancyAdmin',
]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass
