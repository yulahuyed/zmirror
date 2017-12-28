FROM alpine:3.7
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV DOMAIN=test.com

RUN apk --no-cache add gcc g++ git python3 python3-dev libc-dev                                  && \
    pip3 install --upgrade --no-cache-dir pip && \
    pip3 install --no-cache-dir gunicorn gevent requests flask cchardet fastcache lru-dict
    
RUN adduser -s /bin/ash -g 100 -D zmirror -u 1005

USER zmirror

RUN mkdir /var/www && cd /var/www && \
    git clone -b v0.30-dev https://github.com/aploium/zmirror --depth 1            && \
    cp /var/www/zmirror/more_configs/config_google_and_zhwikipedia.py /var/www/zmirror/config.py && \
    
WORKDIR /var/www/zmirror
EXPOSE  8080

CMD sed -i "s/\'127.0.0.1\'/\'tmp_replace\'/g" config.py && \
    sed -i "s/tmp_replace/${DOMAIN}/g" config.py && \
    gunicorn --bind 0.0.0.0:8080 --workers 2 --worker-connections 100 wsgi:application

