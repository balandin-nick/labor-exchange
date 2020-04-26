from django.views.generic import TemplateView


__all__ = [
    'HomeView',
]


class HomeView(TemplateView):
    template_name = 'index.html'
