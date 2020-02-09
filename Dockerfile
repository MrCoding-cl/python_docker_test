FROM alpine:3.11.3

RUN apk add --no-cache python3-dev\
    && pip3 install --upgrade pip


WORKDIR /app

COPY . /app

