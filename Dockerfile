from python:3.8.6-buster

COPY api/api.py api.py
COPY titanic titanic/
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD uvicorn api:app --host 0.0.0.0

