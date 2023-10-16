FROM python:3.11.6-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./src /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

CMD ["python", "main.py"]
