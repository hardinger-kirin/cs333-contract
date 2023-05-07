FROM alpine:latest

RUN apk update
RUN apk add python3 py3-pip
RUN mkdir app
COPY main.py app/main.py
COPY boba.py app/boba.py
COPY customer.py app/customer.py
COPY player.py app/player.py
WORKDIR /app

ENTRYPOINT ["python3", "main.py"]