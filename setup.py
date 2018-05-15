#!/usr/bin/env python

from distutils.core import setup

setup(
    name='image-conveyor',
    version='0.1',
    description='Download, process and upload images with AWS',
    author='Vadym Serdiuk',
    author_email='va.serdyuk@gmail.com',
    url='https://github.com/vadym-serdiuk/image-conveyor',
    packages=['image_conveyor'],
    python_requires=">=3.6",
    install_requires=[
        "numpy==1.14.3",
        "opencv_python==3.4.0.12",
        "pytest",
        "pytest-flask",
        "boto==2.48.0",
        "jsonschema==2.6.0",
        "redis==2.10.6",
        "flask==1.0.2",
        "flask_restplus==0.10.1"
    ],
    entry_points={
        "console_scripts": [
            "image-conveyor-worker = image_conveyor:run_worker",
            "image-conveyor-api = image_conveyor:run_http_server"
        ],
    }
)
