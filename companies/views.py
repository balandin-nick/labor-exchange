from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .models import Company


__all__ = [
    'CompanyListView',
    'CompanyDetailView',

    'MyCompanyControlView',
    'MyCompanyCreateView',
    'MyCompanyUpdateView',
    'MyCompanyVacanciesView',
]


class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'


class CompanyDetailView(DetailView):
    model = Company
    pk_url_kwarg = 'company_id'
    template_name = 'company_detail.html'

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['previous_url'] = self.request.META.get('HTTP_REFERER')
        return context


class MyCompanyControlView(TemplateView):
    template_name = 'my_company/missing.html'

    def dispatch(self, request, *args, **kwargs) -> HttpResponseNotAllowed:
        if not self.request.user.is_authenticated:
            return redirect('login')

        if self.request.user.companies.count() > 0:
            return redirect('my-company')

        return super().dispatch(request, *args, **kwargs)


class MyCompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['name', 'location', 'logo', 'employee_count', 'description']
    template_name = 'my_company/display.html'

    def dispatch(self, request, *args, **kwargs) -> HttpResponseNotAllowed:
        if self.request.user.companies.count() > 0:
            return redirect('my-company')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form) -> HttpResponseRedirect:
        instance: Company = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()

        self.request.session['is_after_creating'] = True
        return redirect('my-company')


class MyCompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    fields = ['name', 'location', 'logo', 'employee_count', 'description']
    template_name = 'my_company/display.html'

    def get_object(self, queryset=None) -> Company:
        company = Company.get_user_company(self.request.user)
        if not company:
            return redirect('my-company-control')

        return company
    
    def form_invalid(self, form) -> Any:
        self.request.session['is_after_creating'] = False
        self.request.session['is_after_updating'] = False
        return super().form_invalid(form)

    def form_valid(self, form) -> HttpResponseRedirect:
        self.request.session['is_after_updating'] = True
        return redirect('my-company')

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['is_success_created'] = self.request.session.pop('is_after_creating', False)
        context['is_success_updated'] = self.request.session.pop('is_after_updating', False)
        return context


class MyCompanyVacanciesView(LoginRequiredMixin, DetailView):
    model = Company
    template_name = 'my_company/vacancy_list.html'

    def get_object(self, queryset=None) -> Company:
        company = Company.get_user_company(self.request.user)
        if not company:
            return redirect('my-company-control')

        return company
