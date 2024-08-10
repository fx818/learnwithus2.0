FROM python:3.10-buster

ENV PYTHONBUFFERED = 1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm

COPY . .

CMD python manage.py runserver 0.0.0.0:8000


