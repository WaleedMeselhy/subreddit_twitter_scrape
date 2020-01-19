# -*- coding: utf-8 -*-
import scrapy
import json
import os
# from elasticsearch import Elasticsearch, Connection
# import elasticsearch.connection as conn
# import requests

# elastic_url = os.environ['elasticsearch_host'] + ":" + str(9200)
# req_conn = conn.RequestsHttpConnection(Connection)
# req_conn.base_url = elastic_url

# es = Elasticsearch([{'host': os.environ['elasticsearch_host'], 'port': 9200}])


class SubredditSpider(scrapy.Spider):
    name = 'subreddit'
    reddit_url = 'https://gateway.reddit.com/desktopapi/v1/subreddits/'
    sub_reddit = ''
    max_number_of_scrapped_pages = 10
    number_of_scrapped_pages = 0
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

    def start_requests(self):
        url = f'{self.reddit_url}{self.sub_reddit}'
        yield scrapy.Request(url=url,
                             callback=self.parse_reddit,
                             headers={'User-Agent': self.user_agent})

    def parse_reddit(self, response):
        data = json.loads(response.body)
        for _, post_info in data['posts'].items():
            post_db = {
                'title': post_info['title'],
                'permalink': post_info['permalink']
            }
            # res = es.index(index='megacorp',
            #                doc_type='redditpost',
            #                body=post_db)
            # print(res)
            yield post_db
        token = data.get('token', None)
        if token:
            if (self.number_of_scrapped_pages < int(
                    self.max_number_of_scrapped_pages)):
                print('number_of_scrapped_pages',
                      self.number_of_scrapped_pages)
                url = f'{self.reddit_url}{self.sub_reddit}' + f'?after={token}'
                yield scrapy.Request(url=url,
                                     callback=self.parse_reddit,
                                     headers={'User-Agent': self.user_agent})
                self.number_of_scrapped_pages += 1
