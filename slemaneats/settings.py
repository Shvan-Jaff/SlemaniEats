
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-demo-key'

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'main',
]

MIDDLEWARE = []
ROOT_URLCONF = 'slemaneats.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'main', 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [],
    },
}]

WSGI_APPLICATION = 'slemaneats.wsgi.application'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'main', 'static')]

ALLOWED_HOSTS = ['.vercel.app']
