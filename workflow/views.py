from django.views.generic import ListView, TemplateView

from .models import Company, Specialty, Vacancy


__all__ = [
    'HomeView',
    'VacancyList',
]


class HomeView(TemplateView):
    template_name = 'index.html'


class VacancyList(ListView):
    model = Vacancy
    template_name = 'vacancy_list.html'
