from flask import jsonify, request, abort, make_response
import requests
from flask import current_app
from elasticsearch import Elasticsearch
import copy
import re
doc_typies = {'subreddit': 'posts'}
scrapyjob_info = {
    'subreddit': {
        "project": "scrap_subreddit",
        "spider": "subreddit",
        "sub_reddit": ""
    }
}


def add_scrapyjob():
    scrapyd_host = f"http://{current_app.config['SCRAPYD_HOST']}/schedule.json"
    url = request.json['url']
    data = None
    if 'reddit' in url:
        if re.match('https://www.reddit.com/r/[^/]*/$', url):
            data = copy.deepcopy(scrapyjob_info['subreddit'])
            data['sub_reddit'] = [
                sub for sub in reversed(url.split('/')) if sub != ''
            ][0]
    r = requests.post(scrapyd_host, data=data)
    if r.status_code == 200:
        return ''
    else:
        return '', r.status_code


def search():
    index = request.args.get('index')
    text = request.args.get('text')

    es: Elasticsearch = current_app.elasticsearch
    results = es.search(index='',
                        body={"query": {
                            "query_string": {
                                "query": text
                            }
                        }})
    return jsonify(results)
