FROM alpine:3.10
MAINTAINER abystrov@131.ru

RUN apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip requests

COPY testing_server.py /usr/local/bin
ENTRYPOINT ["python3", "/usr/local/bin/testing_server.py"]
