FROM alpine:3.7
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV GOAL=google_and_zhwikipedia
ENV DOMAIN=test.com

RUN mkdir /var/www && cd /var/www && \
    apk --no-cache add gcc g++ git python3 python3-dev libc-dev                                  && \
    pip3 install --upgrade --no-cache-dir pip && \
    pip3 install --no-cache-dir gunicorn gevent requests flask cchardet fastcache lru-dict    && \
    git clone -b v0.30-dev https://github.com/aploium/zmirror --depth 1            && \
    apk del --purge gcc g++ git libc-dev      && \
    rm -rf /src /zmirror/.git
    
USER 1000
WORKDIR /var/www/zmirror
EXPOSE  8080

CMD cp /var/www/zmirror/more_configs/config_${GOAL}.py /var/www/zmirror/config.py && \
    sed -i "s/\'127.0.0.1\'/\'tmp_replace\'/g" config.py && \
    sed -i "s/tmp_replace/${DOMAIN}/g" config.py && \
    gunicorn --bind 0.0.0.0:8080 --workers 2 --worker-connections 100 wsgi:application

