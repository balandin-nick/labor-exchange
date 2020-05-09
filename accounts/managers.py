from django.contrib.auth.models import BaseUserManager
from typing import Optional


__all__ = [
    'LaborExchangeUserManager',
]


class LaborExchangeUserManager(BaseUserManager):
    def create_user(self, name: str, surname: str, email: str, password: Optional[str] = None):
        if not all([name, surname, email]):
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            surname=surname,
            email=LaborExchangeUserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name: str, surname: str, email: str, password: str):
        user = self.create_user(name=name, surname=surname, email=email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
