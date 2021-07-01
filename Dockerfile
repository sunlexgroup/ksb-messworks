FROM python:3.9.5-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

RUN apt update \
    && apt -y install libpq-dev gcc

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --dev

COPY . /code/

EXPOSE 8000