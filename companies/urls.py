from django.urls import path

from .views import CompanyListView, CompanyDetailView, MyCompanyUpdateView, MyCompanyControlView, MyCompanyCreateView


urlpatterns = [
    path('', CompanyListView.as_view(), name='company-list'),
    path('<int:company_id>', CompanyDetailView.as_view(), name='company-detail'),

    path('my-company', MyCompanyUpdateView.as_view(), name='my-company'),
    path('my-company/create', MyCompanyCreateView.as_view(), name='my-company-create'),
    path('my-company/control', MyCompanyControlView.as_view(), name='my-company-control'),
]