from django.views.generic import ListView, TemplateView, DetailView

from .models.local_types import SpecialtyChoices
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
    context_object_name = 'company'
    template_name = 'company_detail.html'


class VacancyList(ListView):
    model = Vacancy
    context_object_name = 'vacancy_list'
    template_name = 'vacancy_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'specialty' not in self.kwargs:
            return queryset

        queryset = Vacancy.objects.filter(specialty__code=SpecialtyChoices(self.kwargs['specialty']))
        return queryset


class VacancyDetail(DetailView):
    model = Vacancy
    template_name = 'vacancy_detail.html'
