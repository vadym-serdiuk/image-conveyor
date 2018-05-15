import sys

from image_conveyor.core.engines.s3 import S3Engine
from image_conveyor.core.task import Task


def test_s3_download(task_fixture):
    task = Task(request_id=1,
             bucket=task_fixture["bucket"],
             filename=task_fixture["filename"])
    engine = S3Engine(task)
    engine.download()
    assert sys.getsizeof(task.image) == 2663


def test_s3_upload(task_fixture, local_file_path):
    task = Task(request_id=1,
                bucket=task_fixture["bucket"],
                filename=task_fixture["filename"])
    with open(local_file_path, 'rb') as f:
        task.image.write(f.read())
        task.image.seek(0)
    engine = S3Engine(task)
    engine.upload()
