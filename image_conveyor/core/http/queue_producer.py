import functools
import json

import redis

from image_conveyor import settings


@functools.lru_cache()
def get_redis():
    return redis.Redis('mq')


def add_task_to_queue(input_task):
    r = get_redis()

    input_task = input_task.copy()
    files = input_task.pop('files', [])
    for file in files:
        task = {**input_task,
                'filename': file}
        r.rpush(settings.TASK_QUEUE, json.dumps(task))