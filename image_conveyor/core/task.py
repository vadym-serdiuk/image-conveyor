import io

from image_conveyor.core.steps.download import DownloadStep
from image_conveyor.core.steps.processing import ProcessingStep
from image_conveyor.core.steps.upload import UploadStep

DEFAULT_SCENARIO = [DownloadStep, ProcessingStep, UploadStep]


class Task:
    def __init__(self, request_id, bucket, filename,
                 scenario=DEFAULT_SCENARIO, parameters=None):
        self.request_id = request_id
        self.bucket = bucket
        self.filename = filename
        self.image = io.BytesIO()
        self.scenario = scenario
        self.parameters = parameters or {}
        self.steps = iter(self.scenario)

    def _get_next_step(self):
        try:
            step_class = next(self.steps)
        except StopIteration:
            return
        return step_class

    def run_next_step(self):
        step_class = self._get_next_step()
        if step_class:
            step = step_class(self)
            step.run()
        else:
            self.finish()

    def start(self):
        self.run_next_step()

    def finish(self):
        pass
