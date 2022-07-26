FROM python:3.8
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /usr/src/app
COPY requirements.txt .

RUN apt update \
    && python -m pip install --upgrade pip \
    && pip3 install -r requirements.txt

COPY . /usr/src/app/
