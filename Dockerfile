FROM python:3.7 AS build

ARG prod

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD Makefile Pipfile Pipfile.lock /usr/src/app/
COPY . /usr/src/app
RUN if [ "$prod" ]; then make prod; else make prod-no-tests; fi
