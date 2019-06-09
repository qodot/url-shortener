FROM pypy:3.5-7.0.0

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN pip install virtualenv && virtualenv venv
