FROM python:3.7

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN pip install --upgrade pip setuptools && pip install -r requirements.txt
