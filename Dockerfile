FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000
CMD gunicorn app:app -b 0.0.0.0:8000
