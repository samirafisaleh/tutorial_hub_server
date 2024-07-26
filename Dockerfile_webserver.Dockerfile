FROM python:3.9.19-slim-bookworm

WORKDIR /

COPY requirements.prod.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 5000

# Improve following line to only copy necessary files
COPY source/ source/


WORKDIR /source/project

# RUN mv .docker.env .env