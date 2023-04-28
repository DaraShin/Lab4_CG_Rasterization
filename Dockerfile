FROM python:3.9-slim-buster
RUN apt-get update && apt-get install -y python3-tk

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /code

COPY ./src .