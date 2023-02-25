FROM python:3.10-slim

WORKDIR /app

ADD . /app

RUN apt update && \
 apt install -y vim && \
 apt-get install -y python3-pip && \
 apt install gcc && \
 pip3 install uwsgi 

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["uwsgi","flask_uwsgi.ini"]