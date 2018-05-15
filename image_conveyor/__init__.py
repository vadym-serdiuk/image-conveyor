def run_worker():
    from image_conveyor.core.worker import consumer
    consumer()


def run_http_server():
    from image_conveyor.core.http.app import start_app
    start_app()