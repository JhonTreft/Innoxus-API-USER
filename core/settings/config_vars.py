from pathlib import Path
from os import path,getenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(getenv('SECRET_KEY'))

if not(SECRET_KEY):
    exit(1)

#allowed host 
ALLOWED_HOSTS = []

# root config
ROOT_URLCONF = 'core.urls'

#wsgi config application
WSGI_APPLICATION = 'core.wsgi.application'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#cors
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1",
    "http://localhost:4200"  # Reemplaza con la URL de tu frontend en desarrollo
]


CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    
]

CORS_ALLOW_HEADERS = [
    'Accept',
    'Authorization',
    'Content-Type',
    'X-CSRFToken',  # Agrega X-CSRFToken a los encabezados permitidos

]

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = path.join(BASE_DIR,'static'),
STATIC_ROOT = path.join(BASE_DIR,'static','static')