import uuid

from flask import request
from flask_restplus import Resource

from image_conveyor.core.http.api import api
from image_conveyor.core.http.models import task
from image_conveyor.core.http.queue_producer import add_task_to_queue

task_namespace = api.namespace('task')


@task_namespace.route('/')
class TaskCollection(Resource):
    @api.response(201, 'Task successfully added.')
    @api.expect(task, validate=True)
    def post(self):
        """
        Use this method to add files for processing
        """
        request_id = str(uuid.uuid4())
        task = {**request.json, 'request_id': request_id}
        add_task_to_queue(task)
        return task, 201
