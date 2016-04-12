FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN pip install uwsgi

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/
