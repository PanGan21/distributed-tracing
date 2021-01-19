FROM python:3

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY gunicorn.conf .

COPY service_a.py .
COPY app.py .
COPY utils.py .

CMD ["gunicorn", "--config=file:/app/gunicorn.conf", "app:app"]