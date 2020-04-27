from django.views.generic import TemplateView


__all__ = [
    'VacancyList',
]


class VacancyList(TemplateView):
    template_name = 'vacancy_list.html'
