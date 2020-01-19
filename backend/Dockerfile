FROM python:3.6-alpine as base 
FROM base as builder

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev 
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --user -r /app/requirements.txt 


WORKDIR /app

FROM base
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache bash curl

COPY --from=builder /root/.local /usr/local
COPY ./ /app
RUN chmod +x /app/entrypoint.sh
RUN chmod +x /app/gunicorn.sh

WORKDIR /app

ENTRYPOINT ["/app/entrypoint.sh"]