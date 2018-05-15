FROM python:3.6-stretch

RUN mkdir /code
WORKDIR /code
ADD ./ /code/
RUN pip install -e .

CMD ['image-conveyor-worker']