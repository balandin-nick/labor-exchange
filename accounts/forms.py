from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, EmailField, Form, PasswordInput

from .models import LaborExchangeUser


__all__ = [
    'LaborExchangeUserLoginForm',
    'LaborExchangeUserCreationForm',
]


class LaborExchangeUserLoginForm(Form):
    email = EmailField()
    password = CharField(widget=PasswordInput)

    class Meta:
        fields = ('email', 'password')


class LaborExchangeUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = LaborExchangeUser
        fields = ('name', 'surname', 'email', 'phone')
