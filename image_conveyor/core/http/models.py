from flask_restplus import fields

from image_conveyor.core.http.api import api

bucket = api.model('Bucket', {
    'region': fields.String(),
    'name': fields.String(),
})


task = api.model('Task', {
    'bucket': fields.Nested(bucket, required=True),
    'files': fields.List(fields.String, required=True),
    'parameters': fields.Raw()
})