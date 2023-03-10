"""
- Errors/грешки от самата система, обикновено се случват на сървъра/
- Exceptions/cannot use same e-mail for different user, can be modified/
- pip install bcrypt - pass hashing for your software and servers

- multi-threading - more than 1worker does tasks
- asynhronous - the server can take more requests
- Celery - an asynchronous task queue/job queue based on distributed message passing.
It is focused on real-time operation but supports scheduling as well
pip install celery
- Redis -
python -m celery -A Exception_Handling_2023 worker -l info
AWS:
SES - Amazon Simple Email Service (connect via 'boto3' library)
import boto3
client = boto3.client('ses')
S3 - scalable storage in the cloud
- SQS /Simple Queue Service/ - substitute of Redis/RabbitMQ - create queue in AWS for tasks that have to be done
Name: exampleemailsending.fifo (ending .fifo)
-Gunicorn - parses request to our application (e.g written in Python/Django ) through wsgi.py
-NginX - opens ports for requests
-Top Hosting Solutions
-SSL certificate
-ForeignField (vs. ForeignKey)
- Django Shopping Cart URL: https://pypi.org/project/django-shopping-cart/
- Security - SSL Certificate
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-l!=l$=k@ka=p9j*u5n+nli4m7d0kzml$7--^t&sjvi9zoskaua'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'custom_users',
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

ROOT_URLCONF = 'Exception_Handling_2023.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'Exception_Handling_2023.wsgi.application'

# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"