FROM alpine:3.7
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV DOMAIN=test.com

RUN apk --no-cache add gcc g++ git python3 python3-dev libc-dev                                  && \
    pip3 install --upgrade --no-cache-dir pip && \
    pip3 install --no-cache-dir gunicorn gevent requests flask cchardet fastcache lru-dict
    
RUN adduser -s /bin/ash -g 100 -D zmirror -u 1005 -h /home/zmirror

USER zmirror

RUN git clone -b v0.30-dev https://github.com/aploium/zmirror /home/zmirror/zmirror --depth 1            && \
    chmod -R 777 /home/zmirror/zmirror && \
    cp /home/zmirror/zmirror/more_configs/config_google_and_zhwikipedia.py /home/zmirror/zmirror/config.py
    
WORKDIR /home/zmirror/zmirror
EXPOSE  8080

CMD sed -i "s/'127.0.0.1'/'${DOMAIN}'/g" config.py && \
    gunicorn --bind 0.0.0.0:8080 --workers 2 --worker-connections 100 wsgi:application

