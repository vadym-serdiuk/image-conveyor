import os

import pytest


@pytest.fixture
def task_fixture():
    return {
        "bucket": {
            "region": "eu-central-1",
            "name": "input-images-j4g23"
        },
        "filename": "test.jpg"
    }


@pytest.fixture
def local_file_path():
    return os.path.join(os.path.dirname(__file__), './test_images/test.jpg')