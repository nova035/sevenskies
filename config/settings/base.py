from __future__ import absolute_import, unicode_literals

import os

DEBUG = False
TEMPLATE_DEBUG = False
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)
INSTALLED_APPS = [
    # Custom apps
    'home',

    # Wagtail
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    # Django utility apps
    'modelcluster',
    'taggit',

    # Stock Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Debugging utilities
    'debug_toolbar',
]
SITE_ID = 1
SECRET_KEY = 'v404$ax_$vjyt!bf7di9z19oj9h3=_&ui5&v)6f&iygsies#4%'
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]
ROOT_URLCONF = 'config.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
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
WSGI_APPLICATION = 'config.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kehia',
        'USER': 'kehia',
        'PASSWORD': 'kehia',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_L10N = True

USE_TZ = True
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
]
STATIC_ROOT = '/opt/kehia/static/'
STATIC_URL = '/static/'
MEDIA_ROOT = '/opt/kehia/media/'
MEDIA_URL = '/media/'


WAGTAIL_SITE_NAME = "kehia"
BASE_URL = 'http://kehia.org'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'fixtures'),
]

CONFIG_DEFAULTS = {
    # Toolbar options
    'SHOW_TOOLBAR_CALLBACK': lambda r: False,
    }
