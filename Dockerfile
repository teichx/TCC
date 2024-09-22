FROM python:3.12-alpine

COPY requirements.txt ./requirements.txt
RUN pip install --user -r ./requirements.txt

COPY app ./app
