from django.urls import path

from .views import VacancyCreateView, VacancyDetailView, VacancyListBySpecialtyView, VacancyListView, VacancyUpdateView


urlpatterns = [
    path('', VacancyListView.as_view(), name='vacancy-list'),
    path('specialties/<str:specialty_code>', VacancyListBySpecialtyView.as_view(), name='vacancy-list-by-specialty'),

    path('create', VacancyCreateView.as_view(), name='vacancy-create'),
    path('<int:vacancy_id>', VacancyDetailView.as_view(), name='vacancy-detail'),
    path('<int:vacancy_id>/update', VacancyUpdateView.as_view(), name='vacancy-update'),
]
