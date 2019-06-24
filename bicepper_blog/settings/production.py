from .base import *


DEBUG = False

if not DEBUG:
    ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bicepper_blog',
        'USER': 'root',
        # 'PASSWORD': '65t00Uof',
        'PASSWORD': '65t00Uof',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO,ONLY_FULL_GROUP_BY',
        }
    }
}

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = '/var/www/{}/static'.format(PROJECT_NAME)