FROM python:3.10-slim-buster as builder

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc


COPY requirements.txt .
RUN pip install --user -r requirements.txt

COPY short_url_api .

ENV PATH=/usr/.local:$PATH