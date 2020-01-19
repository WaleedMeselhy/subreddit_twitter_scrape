from flask import Blueprint
from .apis import (add_scrapyjob, search)

rest_api = Blueprint('rest api', __name__)
# TODO: authentication
rest_api.route('/scrapyjob/', methods=('POST', ))(add_scrapyjob)
rest_api.route('/search/', methods=('GET', ))(search)
