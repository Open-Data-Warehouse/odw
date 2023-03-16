FROM python:3.11-slim-buster

RUN python -m pip install --upgrade pip
RUN python -m pip install -U setuptools

COPY . .

RUN python -m pip install .

