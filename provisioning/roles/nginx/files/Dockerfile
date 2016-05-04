FROM nginx

RUN mkdir -p /static
RUN chmod 755 /static
VOLUME /vagrant/template_api/static /static

COPY ./django.conf /etc/nginx/conf.d/django.conf
