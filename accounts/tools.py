from django.http.request import HttpRequest
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


__all__ = [
    'UserLoginManager'
]


class UserLoginManager:
    _email: str
    _password: str

    def __init__(self, email: str, password: str, request: HttpRequest) -> None:
        self._email = email
        self._password = password
        self._request = request

    def authenticate_and_login(self) -> HttpResponse:
        user = authenticate(email=self._email, password=self._password)

        if user is None:
            return HttpResponse('Invalid authentication', status=400)
        elif not user.is_active:
            return HttpResponse('Disabled account', status=423)

        login(self._request, user)
        return HttpResponse('User Authenticated Successfully', status=200)
