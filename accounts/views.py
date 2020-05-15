from typing import Any, Union

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic.edit import FormView

from .forms import LaborExchangeUserCreationForm, LaborExchangeUserLoginForm
from .tools import UserLoginManager


__all__ = [
    'UserLoginView',
    'UserSignupView',
]


class UserLoginView(FormView):
    form_class = LaborExchangeUserLoginForm
    success_url = '/'
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs) -> Any:
        if request.user.is_authenticated:
            return redirect('home')

        return super(UserLoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form) -> Union[HttpResponse, HttpResponseRedirect]:
        cleaned_data = form.cleaned_data
        login_result = UserLoginManager(
            email=cleaned_data['email'],
            password=cleaned_data['password'],
            request=self.request,
        ).authenticate_and_login()

        if login_result.status_code == 200:
            return super(UserLoginView, self).form_valid(form)

        return login_result


class UserSignupView(CreateView):
    form_class = LaborExchangeUserCreationForm
    success_url = '/'
    template_name = 'accounts/signup.html'

    def post(self, request, *args, **kwargs) -> Any:
        response = super(UserSignupView, self).post(request, *args, **kwargs)
        if response.status_code == 302:
            login_result = UserLoginManager(
                email=request.POST['email'],
                password=request.POST['password1'],
                request=request,
            ).authenticate_and_login()

            if login_result.status_code != 200:
                return login_result

        return response
