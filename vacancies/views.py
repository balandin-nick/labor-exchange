from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.http.response import Http404, HttpResponseNotAllowed
from django.shortcuts import redirect, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .models import Specialty, Vacancy


__all__ = [
    'VacancyListView',
    'VacancyListBySpecialtyView',
    'VacancyDetailView',
    'VacancyCreateView',
]


class VacancyListView(ListView):
    model = Vacancy
    queryset = Vacancy.objects.select_related('company')
    context_object_name = 'vacancy_list'
    template_name = 'vacancies/vacancy_list.html'
    page_header = 'Все вакансии'

    def get_context_data(self, *args, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context['page_header'] = self.page_header
        return context


class VacancyListBySpecialtyView(VacancyListView):
    page_header = None

    def dispatch(self, request, *args, **kwargs) -> HttpResponseNotAllowed:
        try:
            self.page_header = Specialty.objects.get(code=self.kwargs['specialty_code']).title
        except ObjectDoesNotExist:
            raise Http404()
        
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet:
        vacancies: QuerySet = super().get_queryset()
        return vacancies.filter(specialty__code=self.kwargs['specialty_code'])


class VacancyDetailView(DetailView):
    model = Vacancy
    queryset = Vacancy.objects.select_related('company').all()
    pk_url_kwarg = 'vacancy_id'
    template_name = 'vacancies/vacancy_detail.html'

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['previous_url'] = self.request.META.get('HTTP_REFERER')
        return context


class VacancyCreateView(LoginRequiredMixin, CreateView):
    model = Vacancy
    fields = ['title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description']
    template_name = 'vacancies/vacancy_form.html'

    def dispatch(self, request, *args, **kwargs) -> HttpResponseNotAllowed:
        if not self.request.user.companies.count() > 0:
            return redirect('my-company-control')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.all()
        return context

    def form_valid(self, form) -> HttpResponseRedirect:
        instance: Vacancy = form.save(commit=False)
        instance.company = self.request.user.companies.all()[0]
        instance.save()

        self.request.session['is_after_creating'] = True
        return redirect(reverse('vacancy-update', kwargs={'vacancy_id': instance.pk}))


class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    model = Vacancy
    queryset = Vacancy.objects.select_related('specialty')
    pk_url_kwarg = 'vacancy_id'
    fields = ['title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description']
    template_name = 'vacancies/vacancy_form.html'

    def dispatch(self, request, *args, **kwargs) -> HttpResponseNotAllowed:
        if not self.request.user.companies.count() > 0:
            return redirect('my-company-control')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['specialties'] = Specialty.objects.all()
        context['is_success_created'] = self.request.session.pop('is_after_creating', False)
        context['is_success_updated'] = self.request.session.pop('is_after_updating', False)

        return context

    def form_valid(self, form) -> HttpResponseRedirect:
        instance: Vacancy = form.save()
        self.request.session['is_after_updating'] = True
        return redirect(reverse('vacancy-update', kwargs={'vacancy_id': instance.pk}))
