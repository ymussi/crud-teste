FROM python:3.6
LABEL mantainer="ymussi@gmail.com"
LABEL fileversion=v0.1

WORKDIR /app/crud

COPY . /app/crud

ARG RUN_ENVIRONMENT
ENV PYTHONUNBUFFERED=0
ENV DBENV=${RUN_ENVIRONMENT}

RUN apt-get update && pip install --upgrade pip && \
    ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app/ata-memorandos
RUN python setup.py develop


ENTRYPOINT ["/bin/sh","/app/crud/entrypoint.sh"]
