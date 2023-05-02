FROM python:3.9

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile Pipfile.lock /code/

RUN apt-get update
RUN pip install -U pipenv
RUN pipenv install --system

COPY . .

EXPOSE 8000