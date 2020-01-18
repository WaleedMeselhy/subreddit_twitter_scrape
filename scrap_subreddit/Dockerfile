FROM python:3.7-alpine as base

FROM base as builder
RUN apk update && \
    apk add --virtual .build-deps git \
    gcc \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    musl-dev \
    openssl-dev \
    py3-setuptools \
    linux-headers \
    libc-dev \
    python3-dev && \
    python3 -m ensurepip && \
    pip3 install setuptools
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --prefix=/install --prefer-binary -r /tmp/requirements.txt && \
    rm -r /root/.cache && \
    apk del .build-deps 

FROM base
RUN apk add libxslt
COPY --from=builder /install /usr/local
COPY scrap_subreddit /app/scrap_subreddit
COPY scrapy.cfg /app/scrapy.cfg
WORKDIR /app
ENTRYPOINT [ "sh" ]
# CMD ["-c", "while true; do echo 'Hit CTRL+C'; sleep 1; done > /dev/null"]
CMD [ "-c", "scrapy crawl subreddit -a max_number_of_scrapped_pages=${max_number_of_scrapped_pages} -a sub_reddit=${sub_reddit} -o/output/posts.json"]