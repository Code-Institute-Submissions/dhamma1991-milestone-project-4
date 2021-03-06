"""
Django settings for levelup project.

Generated by 'django-admin startproject' using Django 2.0.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
# Allow parsing of database urls
import dj_database_url

# If there is a environment variable called development, set DEBUG to false
if os.environ.get('DEVELOPMENT'):
    DEBUG = True
else:
    DEBUG = False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Django Secret Key
if os.environ.get('TRAVIS_BUILD'):
    SECRET_KEY = 'wt5xd3fx+bgh+vo^hj!%l&-nag7ginpz7e@6t)gcf#(_@0ecjk'
else:
    SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME'),
                'levelup-productivity.herokuapp.com',]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks.apps.TasksConfig',
    'accounts.apps.AccountsConfig',
    'level_system.apps.LevelSystemConfig',
    'stats.apps.StatsConfig',
    'crispy_forms',
    'crispy_forms_materialize',
    'storages'
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

ROOT_URLCONF = 'levelup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'levelup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# If DATABASE_URL is in the environment, that means the deployment is production
if "DATABASE_URL" in os.environ:
    DATABASES = {
        # This is for the benefit of heroku. This will parse in the config var of database url 
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
# Else the database was not found in the production environment for some reason
# or the deployment is in the development environment
else:
    print("Postgres URL not found, using sqlite instead")
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Where to take the user after a successful login
LOGIN_REDIRECT_URL = 'tasks:get_tasks'
# Set the url where Django looks for login functionality
LOGIN_URL = 'login'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_ROOT =  os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),    
]

# Path to the dir where Django stores uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Public url of the media directory
MEDIA_URL = '/media/'

# Needed to ensure messages display in dev environment
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# Crispy Forms configuration
CRISPY_TEMPLATE_PACK = 'materialize_css_forms'

# Stripe configuration
STRIPE_PUBLISHABLE_KEY = 'pk_test_a1sVyoIJ44jtCvZLROa08pJQ'
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SEC_KEY')

# AWS configuration
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# If a user uploads a file that has the same name as a file another user has
# uploaded, that shouldn't change all user's files that happen to have the same name
AWS_S3_FILE_OVERWRITE = False
# Setting this to none possibly prevents issues from occurring with djangp storage
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Configure Django App for Heroku.
# Try to import django-heroku depending on Travis or Heroku
# This prevents an error from occuring on Travis
try:
    # Configure Django App for Heroku.
    import django_heroku
    django_heroku.settings(locals())
except ImportError:
    found = False