FROM alpine:latest

RUN apk update
RUN apk add python3 py3-pip
RUN pip install names
RUN mkdir app
COPY main.py app/main.py
COPY customer.py app/customer.py
COPY game_helper.py app/game_helper.py
COPY ingredient.py app/ingredient.py
COPY inventory.py app/inventory.py
COPY order.py app/order.py
WORKDIR /app

ENTRYPOINT ["python3", "main.py"]