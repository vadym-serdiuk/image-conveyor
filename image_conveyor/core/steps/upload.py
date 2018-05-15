from concurrent.futures import ThreadPoolExecutor

from image_conveyor import settings
from image_conveyor.core.engines.s3 import S3Engine
from ._base import Step

upload_pool = ThreadPoolExecutor(settings.LOAD_THREADS_NUMBER)


class UploadStep(Step):
    loader = S3Engine

    def upload(self):
        self.task.image.seek(0)
        self.loader(self.task).upload()
        self.finished()

    def run(self):
        upload_pool.submit(self.upload)