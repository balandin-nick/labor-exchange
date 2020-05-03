from django.db.models import ForeignKey, SET_NULL, Model, CharField, TextField, CASCADE
from django.contrib.auth.models import User


__all__ = [
    'LaborExchangeUser',
]


class LaborExchangeUser(User):
    pass
