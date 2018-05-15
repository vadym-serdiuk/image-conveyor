class WrongBucketRegion(Exception):
    def __str__(self):
        return 'Could not connect to region'


class WrongBucket(Exception):
    def __str__(self):
        return 'Wrong bucket name'


class WrongFileName(Exception):
    def __str__(self):
        return 'Wrong filename'


class CreatingFileError(Exception):
    pass


class DownloadError(Exception):
    def __init__(self, exc):
        self.reason = str(exc)

    def __str__(self):
        return 'Some error happened while downloading the file. Reason: {}' \
               ''.format(self.reason)

class UploadError(Exception):
    def __init__(self, exc):
        self.reason = str(exc)

    def __str__(self):
        return 'Some error happened while uploading the file. Reason: {}' \
               ''.format(self.reason)
