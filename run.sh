#!/bin/sh

if [ "${CONFIG_URL}" ]
then
  wget -O "config.py" "${CONFIG_URL}"
  sed -i "s/'${CONFIG_DOMAIN}'/'${DOMAIN}'/g" config.py
  gunicorn --bind 0.0.0.0:8080 --workers 2 --worker-connections 100 wsgi:application
else
  cp /more_configs/config_google_and_zhwikipedia.py /config.py
  sed -i "s/'127.0.0.1'/'${DOMAIN}'/g" config.py
  gunicorn --bind 0.0.0.0:8080 --workers 2 --worker-connections 100 wsgi:application
  
