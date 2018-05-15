from concurrent.futures import ProcessPoolExecutor

from image_conveyor import settings
from image_conveyor.core.processors.candy_edge_detection import CED
from ._base import Step

processing_pool = ProcessPoolExecutor(settings.PROCESSES_NUMBER)


class ProcessingStep(Step):
    processor_class = CED

    def process_image(self):
        processor = self.processor_class(
            self.task.image, self.task.filename, self.task.parameters
        )
        self.task.image = processor.process()
        self.finished()

    def run(self):
        processing_pool.submit(self.process_image)