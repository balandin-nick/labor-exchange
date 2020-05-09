from typing import Any, Dict

from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet
from django.http.response import Http404, HttpResponseNotAllowed
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Specialty, Vacancy


__all__ = [
    'VacancyListView',
    'VacancyListBySpecialtyView',
    'VacancyDetailView',
]


class VacancyListView(ListView):
    model = Vacancy
    queryset = Vacancy.objects.select_related('company')
    context_object_name = 'vacancy_list'
    template_name = 'vacancy_list.html'
    page_header = 'Все вакансии'

    def get_context_data(self, *args, **kwargs) -> Dict[str, Any]:
        context = super(VacancyListView, self).get_context_data(*args, **kwargs)
        context['page_header'] = self.page_header
        return context


class VacancyListBySpecialtyView(VacancyListView):
    page_header = None

    def dispatch(self, request, *args, **kwargs) -> HttpResponseNotAllowed:
        try:
            self.page_header = Specialty.objects.get(code=self.kwargs['specialty_code']).title
        except ObjectDoesNotExist:
            raise Http404()
        
        return super(VacancyListBySpecialtyView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet:
        vacancies: QuerySet = super(VacancyListBySpecialtyView, self).get_queryset()
        return vacancies.filter(specialty__code=self.kwargs['specialty_code'])


class VacancyDetailView(DetailView):
    model = Vacancy
    queryset = Vacancy.objects.select_related('company').all()
    pk_url_kwarg = 'vacancy_id'
    template_name = 'vacancy_detail.html'

    def get_context_data(self, **kwargs):
        context = super(VacancyDetailView, self).get_context_data(**kwargs)
        context['previous_url'] = self.request.META.get('HTTP_REFERER')
        return context
