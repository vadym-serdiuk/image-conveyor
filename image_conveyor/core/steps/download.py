from concurrent.futures import ThreadPoolExecutor

from image_conveyor import settings
from image_conveyor.core.engines.s3 import S3Engine
from ._base import Step


download_pool = ThreadPoolExecutor(settings.LOAD_THREADS_NUMBER)


class DownloadStep(Step):
    loader = S3Engine

    def load(self):
        self.loader(self.task).download()
        self.task.image.seek(0)
        self.finished()

    def run(self):
        download_pool.submit(self.load)
