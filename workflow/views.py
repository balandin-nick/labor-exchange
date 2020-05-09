from django.db.models import Count
from django.views.generic import DetailView, ListView, TemplateView

from .models import Company, Specialty, Vacancy
from .models.local_types import SpecialtyChoices


__all__ = [
    'HomeView',
    'CompanyDetail',
    'VacancyList',
]


class HomeView(TemplateView):
    template_name = '../labor_exchange/templates/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['company_list'] = Company.objects \
            .annotate(vacancies_count=Count('vacancies')) \
            .filter(vacancies_count__gt=0)

        context['specialty_list'] = Specialty.objects \
            .filter(vacancies__company__employee_count__gte=0) \
            .annotate(vacancies_count=Count('vacancies'))

        return context


class CompanyDetail(DetailView):
    model = Company
    context_object_name = 'company'
    pk_url_kwarg = 'company_id'
    template_name = 'my_company/display.html'


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
    context_object_name = 'vacancy'
    pk_url_kwarg = 'vacancy_id'
    template_name = 'vacancy_detail.html'

    def get_queryset(self):
        return Vacancy.objects.select_related('company').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
