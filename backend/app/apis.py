from flask import jsonify, request, abort, make_response
import requests
from flask import current_app
from elasticsearch import Elasticsearch


def add_scrapyjob():
    scrapyd_host = f"http://{current_app.config['SCRAPYD_HOST']}/schedule.json"
    data = request.json
    r = requests.post(scrapyd_host, data=data)
    if r.status_code == 200:
        return ''
    else:
        return '', r.status_code


def search():
    index = request.args.get('index')
    text = request.args.get('text')

    es: Elasticsearch = current_app.elasticsearch
    results = es.search(index=index,
                        doc_type='posts',
                        body={"query": {
                            "query_string": {
                                "query": text
                            }
                        }})
    return jsonify(results)
