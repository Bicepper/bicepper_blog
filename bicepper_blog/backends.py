from storages.backends.s3boto3 import S3Boto3Storage
from filebrowser.storage import StorageMixin


class PublicMediaStorage(StorageMixin, S3Boto3Storage):
    pass
