from django.contrib import admin

from .models import LaborExchangeUser


__all__ = [
    'LaborExchangeUserAdmin',
]


@admin.register(LaborExchangeUser)
class LaborExchangeUserAdmin(admin.ModelAdmin):
    pass
