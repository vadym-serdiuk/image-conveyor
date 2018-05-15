import numpy as np

from ._base import AbstractProcessor
import cv2 as cv


class CED(AbstractProcessor):
    allowed_parameters = ('threshold1', 'threshold2', 'edges', 'apertureSize')
    default_parameters = {
        'threshold1': 100,
        'threshold2': 200
    }

    def _read_from_memory(self):
        memory_array = np.asarray(bytearray(self.image.read()), dtype=np.uint8)
        return cv.imdecode(memory_array, 0)

    def get_extension(self):
        return '.{}'.format(self.filename.split('.')[-1])

    def _write_to_memory(self, image):
        retval, memory_array = cv.imencode(self.get_extension(), image)
        self.image.seek(0)
        self.image.write(memory_array.tobytes())
        self.image.seek(0)

    def process(self):
        print('I am starting processing file {}'.format(self.filename))
        cv_image = self._read_from_memory()
        edges = cv.Canny(cv_image, **self.parameters)
        self._write_to_memory(edges)
        print('I finished processing file {}'.format(self.filename))
        return self.image
