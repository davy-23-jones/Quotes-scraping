FROM python:alpine

WORKDIR /scrape


COPY requirements.txt requirements.txt
COPY ./ ./


RUN pip install -r requirements.txt