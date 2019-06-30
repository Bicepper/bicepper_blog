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

# aws settings
AWS_ACCESS_KEY_ID = 'AKIAR4XHSGTYPII5M5PN'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'bicepper-blog'
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

# s3 static settings
STATIC_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# s3 public media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, PUBLIC_MEDIA_LOCATION)
DEFAULT_FILE_STORAGE = 'backends.PublicMediaStorage'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# IP制限で許可する
ALLOWED_IP_BLOCKS = ['127.0.0.1', ]

# IP制限でブロックする
DENY_IP_BLOCKS = []
