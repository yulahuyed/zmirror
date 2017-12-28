FROM alpine:3.7
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV DOMAIN=test.com

RUN apk --no-cache add gcc g++ git python3 python3-dev libc-dev                                  && \
    pip3 install --upgrade --no-cache-dir pip && \
    pip3 install --no-cache-dir gunicorn gevent requests flask cchardet fastcache lru-dict
    
RUN adduser -s /bin/ash -g 100 -D zmirror -u 1005 -h /home/zmirror

USER zmirror

RUN git clone -b v0.30-dev https://github.com/aploium/zmirror /home/zmirror/zmirror --depth 1            && \
    chmod -R 777 /home/zmirror/zmirror
    
WORKDIR /home/zmirror/zmirror

COPY run.sh /home/zmirror/zmirror/run.sh
RUN chmod 755 run.sh

EXPOSE 8080

CMD ["/run.sh"]
