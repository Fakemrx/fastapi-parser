FROM python:3.9

WORKDIR /project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile Pipfile.lock /project/

RUN apt-get update
RUN pip install -U pipenv
RUN pipenv install --system

COPY . .

EXPOSE 8000
