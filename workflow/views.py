from django.views.generic import ListView, TemplateView, DetailView

from .models import Company, Specialty, Vacancy


__all__ = [
    'HomeView',
    'CompanyDetail',
    'VacancyList',
]


class HomeView(TemplateView):
    template_name = 'index.html'


class CompanyDetail(DetailView):
    model = Company
    template_name = 'company_detail.html'


class VacancyList(ListView):
    model = Vacancy
    template_name = 'vacancy_list.html'


class VacancyDetail(DetailView):
    model = Vacancy
    template_name = 'vacancy_detail.html'
