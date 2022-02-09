FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
##COPY requirements/local.txt/ code   
COPY . /code/
RUN pip install -r requirements/local.txt




