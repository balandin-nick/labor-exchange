from django.urls import path

from .views import VacancyList


urlpatterns = [
    path('', VacancyList.as_view(), name='vacancy-list'),
]
