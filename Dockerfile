FROM python:3

RUN mkdir web_app
WORKDIR ./web_app

COPY requeriments.txt .

RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

