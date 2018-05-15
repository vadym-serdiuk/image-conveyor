import io
import os
import sys

from image_conveyor.core.processors.candy_edge_detection import CED


def test_ced_processor():
    image_buf = io.BytesIO()
    filepath = os.path.join(os.path.dirname(__file__),
                            './test_images/test.jpg')
    with open(filepath, 'br') as f:
        image_buf.write(f.read())
        image_buf.seek(0)
    processor = CED(image=image_buf, name='test.jpg')
    edges = processor.process()

    assert sys.getsizeof(edges) == 3353
