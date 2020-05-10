from typing import Any, Union

from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic.edit import FormView

from .forms import LaborExchangeUserCreationForm, LaborExchangeUserLoginForm


__all__ = [
    'UserLoginView',
    'UserSignupView',
]


class UserLoginView(FormView):
    form_class = LaborExchangeUserLoginForm
    success_url = '/'
    template_name = 'login.html'

    def get(self, request, *args, **kwargs) -> Any:
        if request.user.is_authenticated:
            return redirect('home')

        return super(UserLoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form) -> Union[HttpResponse, HttpResponseRedirect]:
        cleaned_data = form.cleaned_data
        user = authenticate(
            email=cleaned_data['email'],
            password=cleaned_data['password'],
        )

        if user is None:
            return HttpResponse('Invalid authentication', status=400)

        if user.is_active:
            login(self.request, user)
            return super(UserLoginView, self).form_valid(form)

        return HttpResponse('Disabled account', status=423)


class UserSignupView(CreateView):
    form_class = LaborExchangeUserCreationForm
    success_url = '/'
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        response = super(UserSignupView, self).post(request, *args, **kwargs)

        if response.status_code == 302:
            login(
                request=request,
                user=authenticate(
                    username=request.POST['email'],
                    password=request.POST['password1'],
                ),
            )

        return response
