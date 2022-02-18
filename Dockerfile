#FROM python:3.7-slim-buster
FROM python:3.9-slim-buster

RUN apt-get update -y && apt-get install vim -y --no-install-recommends

RUN pip3 install --upgrade pip

WORKDIR /app/src
COPY . /app

RUN pip3 install -r /app/requirements.txt

CMD python3 main.py
