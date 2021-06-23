FROM python:3.8

WORKDIR /app

COPY . .

CMD python hello-world.py