import os

"""
Django settings for comparison_backend project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n1_m=fiyml5w+txqzf4ozi1_tdue2m&fs+@$4)!o6nfm+x*0#h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['188.166.194.18','165.227.143.190','gruwier.dk', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'comparisons',
    'django_dbml',
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

ROOT_URLCONF = 'comparison_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'comparison_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'postgres',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Copenhagen'

USE_I18N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'django_static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


STATIC_ROOT = "static"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Own additions below

# MONGO_CONNECTION = 'mongodb://mongo:27017/beone'
MONGO_CONNECTION = 'mongodb://mongo:27017/sofi_dev'

# Mapping for Bifrost 2.1 (SOFI)
MONGO_FIELD_MAPPING = {
    'org': 'org',
    'name': 'name',
    'species': 'categories.species_detection.summary.detected_species',
    'allele_profile': 'categories.mlst.report.data.alleles',
    'sequence_type': 'categories.mlst.report.data.sequence_type'
}

# Mapping of field shortcuts to actual MongoDB fields
# MONGO_FIELD_MAPPING = {
#     'org': 'org',
#     'name': 'name',
#     'species': 'sample.metadata.Microorganism',
#     'sequence_type': 'sample.summary.sequence_type',
#     'metadata': 'sample.metadata',  # Used to retrieve all metadata fields.
#     'sampling_year': 'sample.metadata.Date_Sampling_YYYY',
#     'country_term': {'$arrayElemAt': ['$sample.metadata.Country', 0]},
#     'source_type_term': {'$arrayElemAt': ['$sample.metadata.Source_Type', 0]},
#     'sampling_date': 'sample.metadata.Date_Sampling',
#     'allele_profile': 'pipelines.chewiesnake.allele_profile',
# }

"""Fields that will be fetched from MongoDB when viewing a dataset (currently not all of them
will necessarily be shown on the web page, but maybe this should be changed).
The first element in each tuple must refer to an entry in MONGO_FIELD_MAPPING.
The second element will be used as column header."""
SAMPLE_VIEW_COLUMNS = [
    ('org', 'Organization'),
    ('name', 'Name'),
    ('species', 'Species'),
    # ('sampling_date', 'Sampling Date'),
    ('sequence_type', 'Sequence Type'),
    # ('sampling_year', 'Sampling Year'),
    # ('country_term', 'Country'),
    # ('source_type_term', 'Source Type'),
    # ('sampling_date', 'Sampling Date'),
]

# This will be the default for most field-related options to ReporTree
DEFAULT_RT_METADATA_FIELDS = [
    'sampling_date',
    'sequence_type',
    'country_term',
    'source_type_term',
]

"""These are the default fields for the --frequency-matrix and --count-matrix arguments to ReporTree.
There must always be exactly two entries in this list, and both entries must also exist in
DEFAULT_RT_METADATA_FIELDS."""
DEFAULT_RT_MATRIX_FIELDS = [
      'sequence_type',
      'sampling_date',
]

ALL_SPECIES = (
    ('campy', 'Campylobacter jejuni'),
    ('coli', 'Escherichia coli'),
    ('listeria', 'Listeria monocytogenes'),
    ('salmonella', 'Salmonella enterica'),
    ('mixed', 'Mixed species'),
)

LOGIN_REDIRECT_URL = "/"

DATETIME_FORMAT = 'Y-m-d H.i'

USE_L10N = False

REPORTREE_JOB_FOLDER = Path('/rt_runs')  # Root is root of Docker container!

REPORTREE_TIMEOUT = 5  # The number of seconds to wait for at REST response before setting job state to 'RUNNING'

BIO_API_PORT = 8001
