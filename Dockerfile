FROM python:3.6-slim-buster

WORKDIR /app

ARG FLASK_ENV="production"
ENV FLASK_ENV="${FLASK_ENV}"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install gcc python3-dev musl-dev libpq-dev git \
    && pip3 install pipenv

RUN pip3 install psycopg2

COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

RUN pipenv install --system --dev --deploy

COPY . /app

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3"]