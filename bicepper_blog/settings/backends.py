from storages.backends.s3boto3 import S3Boto3Storage
from filebrowser_safe.storage import S3BotoStorageMixin


class S3Storage(S3BotoStorageMixin, S3Boto3Storage):
    pass


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

