from django.db.models import Count
from django.views.generic import TemplateView

from companies.models import Company
from vacancies.models import Specialty


__all__ = [
    'HomeView',
]


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_list'] = []
        context['specialty_list'] = []

        context['company_list'] = Company.objects \
            .annotate(vacancies_count=Count('vacancies')) \
            .filter(vacancies_count__gt=0)

        context['specialty_list'] = Specialty.objects \
            .filter(vacancies__company__employee_count__gte=0) \
            .annotate(vacancies_count=Count('vacancies'))

        return context
