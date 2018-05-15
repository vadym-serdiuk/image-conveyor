import multiprocessing
import os

AWS_ACCOUNT_ID = os.environ.get('AWS_ACCOUNT_ID', '')
AWS_ACCOUNT_SECRET_KEY = os.environ.get('AWS_ACCOUNT_SECRET_KEY', '')
LOAD_THREADS_NUMBER = int(os.environ.get('LOAD_THREADS_NUMBER', 5))

PROCESSES_NUMBER = int(os.environ.get('PROCESSES_NUMBER',
                                  multiprocessing.cpu_count() - 1))

OUTPUT_BUCKET = {
    "region": 'eu-central-1',
    "name": 'output-images-j4g23'
}

TASK_QUEUE = 'task_queue'
try:
    from .local import *
except:
    pass
