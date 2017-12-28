#!/bin/sh

if [ "${CONFIG_URL}" ]
then
  wget -O "config.py" "${CONFIG_URL}" -P /home/zmirror/zmirror
  sed -i "s/'${CONFIG_DOMAIN}'/'${DOMAIN}'/g" /home/zmirror/zmirror/config.py
else
  cp /home/zmirror/zmirror/more_configs/config_google_and_zhwikipedia.py /home/zmirror/zmirror/config.py
  sed -i "s/'127.0.0.1'/'${DOMAIN}'/g" /home/zmirror/zmirror/config.py
fi

gunicorn --bind 0.0.0.0:8080 --workers 2 --worker-connections 100 wsgi:application
