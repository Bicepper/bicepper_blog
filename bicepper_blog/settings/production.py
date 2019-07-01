from .base import *


DEBUG = False

if not DEBUG:
    ALLOWED_HOSTS = ['bicepper.com', 'my-muscle-get-world.bicepper.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bicepper_blog',
        'USER': 'root',
        'PASSWORD': '6~+ZxQU_.)4q',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO,ONLY_FULL_GROUP_BY',
        }
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = ('/var/www/bicepper_blog_static',)

# IP制限で許可する
ALLOWED_IP_BLOCKS = ['127.0.0.1', ]

# IP制限でブロックする
DENY_IP_BLOCKS = []

# CKeditor
CKEDITOR_CONFIGS = {
  'default': {
    'removePlugins': 'stylesheetparser',
    'allowedContent': True,
  },
}
