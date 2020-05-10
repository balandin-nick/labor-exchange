import os

from django.contrib.admin import AdminSite
from django.urls import reverse_lazy

from .enviroments import DatabaseSettings, DjangoSettings, LoggingSettings


django_settings = DjangoSettings()
database_settings = DatabaseSettings()
logging_settings = LoggingSettings()

# region --- Default settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = django_settings.secret_key
DEBUG = django_settings.debug
ALLOWED_HOSTS = django_settings.allowed_hosts

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'accounts',
    'companies',
    'vacancies',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'labor_exchange.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'labor_exchange', 'templates'),
            os.path.join(BASE_DIR, 'accounts', 'templates'),
            os.path.join(BASE_DIR, 'companies', 'templates'),
            os.path.join(BASE_DIR, 'vacancies', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'labor_exchange.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': database_settings.host,
        'PORT': database_settings.port,
        'NAME': database_settings.db_name,
        'USER': database_settings.username,
        'PASSWORD': database_settings.password,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = str(django_settings.timezone)
USE_I18N = True
USE_L10N = True
USE_TZ = True
# endregion

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'accounts.LaborExchangeUser'

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AdminSite.site_header = 'Биржа труда'
AdminSite.index_title = 'Панель администратора'
