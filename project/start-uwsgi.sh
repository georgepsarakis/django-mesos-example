#!/bin/bash 
set -e

cd /app/web
uwsgi --ini uwsgi.ini
