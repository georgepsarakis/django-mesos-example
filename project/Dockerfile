FROM ubuntu:14.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python-dev build-essential ca-certificates curl python-pip 
RUN apt-get upgrade -y --no-install-recommends && apt-get dist-upgrade -y
RUN apt-get install -y python-virtualenv python-mysqldb supervisor
RUN mkdir -p /app/web
WORKDIR /app
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt
EXPOSE 45000
VOLUME /vagrant /app/web
WORKDIR /app/web/template_api
CMD ["/usr/bin/python", "/usr/bin/supervisord", "-c", "/app/web/supervisord.conf", "--nodaemon"]
