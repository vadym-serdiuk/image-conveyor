from flask import Flask, Blueprint

from image_conveyor.core.http.api import api
from image_conveyor.core.http.rest import task_namespace

def get_app():
    app = Flask(__name__)
    app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

    blueprint = Blueprint('api', __name__, url_prefix='')
    api.init_app(blueprint)
    api.add_namespace(task_namespace)
    app.register_blueprint(blueprint)
    return app


def start_app():
    app = get_app()
    print('>>>>> Starting server <<<<<'.format())
    app.run('0.0.0.0', 8080, debug=True)


if __name__ == '__main__':
    start_app()