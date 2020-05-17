from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from labor_exchange.settings import DEBUG, MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL

from .views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('accounts.urls')),
    path('companies/', include('companies.urls')),
    path('vacancies/', include('vacancies.urls')),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
