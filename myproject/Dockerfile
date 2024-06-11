FROM python:alpine3.19

ENV PYTHONUNBUFFERED 1
RUN apk add --no cache mariadb-connector-c--dev gcc musl-dev
RUN apk add --no cache libffi-dev
RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/


RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install mysqlclient

COPY . /app/