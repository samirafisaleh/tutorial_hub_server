# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

LABEL com.data.hub.server.django="0.0.1"

ENV WORKDIR=/data_hub_server/

RUN python3 -m pip install --upgrade pip

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

WORKDIR ${WORKDIRPATH}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ARG env

EXPOSE 8000


COPY source/ source/

RUN mkdir -p logging/django/django/ logging/django/requests/ logging/gunicorn/


WORKDIR ${WORKDIRPATH}/source/project/

RUN rm -rf apps/college_of_social/migrations/
RUN rm -rf apps/college_of_user/migrations/
RUN rm db.sqlite3

RUN chmod +x wf_run_migration_django.sh
RUN chmod +x wf_run_django.sh

RUN ./wf_run_migration_django.sh

WORKDIR ${WORKDIRPATH}/source/project/

# Set the entrypoint. Possible
ENTRYPOINT ["/bin/bash"]
