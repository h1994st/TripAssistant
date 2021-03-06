"""
Django settings for Co_Trip project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(CURRENT_PATH)
ROOT_PATH = os.path.dirname(PROJECT_PATH)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4*hff8(zx-%t6@n42awk$w13ee)+m+xpy52d_!e6r-wzphe#^a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_comments',
    'plan_comment',
    #'ajax_select',
    'django.contrib.humanize',
    'django.contrib.sites',
    'registration',
    'plan',
    'traveller',
    'Co_Trip',
    'city',
    'guardian',
    'bootstrap3',
    'bootstrap3_datetime',
    'api',
    'upload_avatar',
    'tastypie',
    'notifications',
    'friendship',
    'south',
    'dajaxice',
    'dajax',
    'autocomplete_light',
    'django_messages',
    'mailer',
    'social.apps.django_app.default',

)



AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
    'social.backends.weibo.WeiboOAuth2',
)
ANONYMOUS_USER_ID = -1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)



ROOT_URLCONF = 'Co_Trip.urls'

WSGI_APPLICATION = 'Co_Trip.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),


    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
     os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)

ACCOUNT_ACTIVATION_DAYS = 2
EMAIL_HOST = 'localhost'
SERVER_EMAIL = 'admin@h1994st.com'
DEFAULT_FROM_EMAIL = 'admin@h1994st.com'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

AUTH_PROFILE_MODULE = 'traveller.Traveller'

GUARDIAN_RENDER_403 = True
GUARDIAN_TEMPLATE_403="Co_Trip/403.html"

#ADMINS = (('qsz13', 'qsz1328@gmail.com'))

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}



COMMENTS_APP = 'plan_comment'



UPLOAD_AVATAR_UPLOAD_ROOT = os.path.join(PROJECT_PATH, 'media/upload')
UPLOAD_AVATAR_AVATAR_ROOT = os.path.join(PROJECT_PATH, 'media/avatar')
UPLOAD_AVATAR_URL_PREFIX_ORIGINAL = 'uploadedimage/'
UPLOAD_AVATAR_URL_PREFIX_CROPPED = 'avatar/'

UPLOAD_AVATAR_RESIZE_SIZE = [50, 100, 140]

UPLOAD_AVATAR_WEB_LAYOUT = {
    'preview_areas': [
        {
            'size': 50,
            'text': 'Small Preview'
        },
        {
            'size': 100,
            'text': 'Middle Preview'
        },
        {
            'size': 140,
            'text': 'Large Preview'
        },
    ]
}

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/upload')
MEDIA_URL='/media/'


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)


SOCIAL_AUTH_WEIBO_KEY = '3898996455'
SOCIAL_AUTH_WEIBO_SECRET = 'b5c980bf93d3751affd1241b9fe76ef8'

API_LIMIT_PER_PAGE = 10

NOTIFY_USE_JSONFIELD=True

ALLOWED_HOSTS = ['162.243.22.29','127.0.0.1']