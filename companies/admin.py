from django.contrib import admin

from .models import Company


__all__ = [
    'CompanyAdmin',
]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
