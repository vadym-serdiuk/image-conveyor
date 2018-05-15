import os
import sys

import boto as boto
from boto.exception import S3ResponseError
from boto.s3.connection import OrdinaryCallingFormat

from image_conveyor import settings
from .exceptions import (
    WrongBucket, WrongFileName, DownloadError, UploadError,
    WrongBucketRegion, CreatingFileError
)


class S3Engine:
    def __init__(self, task):
        self.task = task

    def get_bucket(self, bucket=None):
        bucket = bucket or self.task.bucket

        s3 = boto.s3.connect_to_region(
            bucket['region'],
            aws_access_key_id=settings.AWS_ACCOUNT_ID,
            aws_secret_access_key=settings.AWS_ACCOUNT_SECRET_KEY,
            calling_format=OrdinaryCallingFormat()
        )
        if s3 is None:
            raise WrongBucketRegion()

        try:
            s3_bucket = s3.get_bucket(bucket['name'], validate=True)
        except S3ResponseError:
            raise WrongBucket()

        return s3_bucket

    def download(self):
        filename = self.task.filename

        print('I am starting downloading file {}'.format(filename))

        bucket = self.get_bucket()
        try:
            key = bucket.get_key(filename)
        except:
            raise WrongFileName()

        if key is None:
            raise WrongFileName(filename)

        try:
            key.get_file(self.task.image)
        except Exception as e:
            raise DownloadError(e)

        print('I finished downloading file {}'.format(filename))

    def _drop_if_exists(self, bucket, filename):
        key = bucket.get_key(filename, validate=True)
        if key:
            bucket.delete_key(filename)

    def upload(self):
        filename = f'{self.task.request_id}/{self.task.filename}'

        print('I am starting uploading file {}'.format(self.task.filename))

        bucket = self.get_bucket(settings.OUTPUT_BUCKET)

        self._drop_if_exists(bucket, filename)

        try:
            key = bucket.new_key(filename)
        except:
            raise CreatingFileError()

        if key is None:
            raise CreatingFileError()

        try:
            key.set_contents_from_file(self.task.image)
        except Exception as e:
            raise UploadError(e)

        print('I finished uploading file {}'.format(filename))
