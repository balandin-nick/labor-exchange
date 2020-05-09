from django.urls import path

from .views import VacancyDetailView, VacancyListBySpecialtyView, VacancyListView


urlpatterns = [
    path('', VacancyListView.as_view(), name='vacancy-list'),
    path('<int:vacancy_id>', VacancyDetailView.as_view(), name='vacancy-detail'),

    path('specialties/<str:specialty_code>', VacancyListBySpecialtyView.as_view(), name='vacancy-list-by-specialty'),
]
