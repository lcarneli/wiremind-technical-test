FROM python:3.9-alpine

ARG UID="1001"
ARG GID="1001"

ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0 --chdir=./src/"

WORKDIR /app

RUN addgroup -g $GID gunicorn && adduser -u $UID -G gunicorn -D gunicorn

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

EXPOSE 8000

USER gunicorn

CMD [ "gunicorn", "app:app" ]
