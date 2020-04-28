from django.urls import path

from .views import CompanyDetail, HomeView, VacancyList, VacancyDetail


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('companies/<int:company_id>', CompanyDetail.as_view(), name='company-detail'),

    path('vacancies/', VacancyList.as_view(), name='vacancy-list'),
    path('vacancies/<int:vacancy_id>', VacancyDetail.as_view(), name='vacancy-detail'),
    path('vacancies/cat/<str:specialty>', VacancyList.as_view(), name='vacancy-list-by-specialty'),
]
