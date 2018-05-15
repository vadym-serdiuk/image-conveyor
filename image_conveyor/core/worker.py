import json

import redis

from image_conveyor import settings
from image_conveyor.core.task import Task
from image_conveyor.core.validators import TaskValidator


def decode_message(input_message):
    try:
        message = json.loads(input_message.decode())
    except:
        raise
        return {}
    return message


def consumer():
    task_counter = 0
    r = redis.Redis('mq')
    print('Starting worker')
    while True:
        _, task_message = r.blpop(settings.TASK_QUEUE)
        print(task_message)
        input_task = decode_message(task_message)
        print(input_task)
        assert isinstance(input_task, dict)
        validator = TaskValidator(input_task)
        assert validator.is_valid() is True

        task_counter += 1
        task = Task(**input_task)
        task.start()
        print(f'Task #{task_counter} started')
