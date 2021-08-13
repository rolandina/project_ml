from python:3.8.6-buster
COPY api/api.py api.py
COPY titanic titanic/
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
COPY gunicorn_config.py gunicorn_config.py
RUN pip install -r requirements.txt
EXPOSE 8000
CMD  gunicorn -c gunicorn_config.py --bind=0.0.0.0 -p 8000 api:app

