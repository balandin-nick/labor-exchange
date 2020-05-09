from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView


__all__ = [
    'UserLoginView',
    'UserSignupView',
]


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = '/'
    template_name = 'login.html'


class UserSignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        response = super(UserSignupView, self).post(request, *args, **kwargs)

        if response.status_code == 302:
            login(
                request=request,
                user=authenticate(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                ),
            )

        return response
