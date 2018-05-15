import time

import pytest

from image_conveyor.core.steps._base import Step
from image_conveyor.core.task import Task


class Step1(Step):
    pass


class Step2(Step):
    pass


def test_create_new_task():
    t = Task(request_id=1, bucket={}, filename="1")
    assert t.filename == "1"
    assert len(t.scenario) == 3
    assert all([issubclass(step, Step) for step in t.scenario])


def test_next_step():
    t = Task(request_id=1, bucket={}, filename="1", scenario=[Step1, Step2])
    step_class = t._get_next_step()
    assert step_class == Step1
    step_class = t._get_next_step()
    assert step_class == Step2
    step_class = t._get_next_step()
    assert step_class is None
