import logging
import json
from flask import request, jsonify, abort
from flask.views import MethodView
from webargs import fields
from webargs.flaskparser import parser
from uuid import uuid4
from ..models.comic import Comic
from ..services.comicrecomm import recommend

'''
Comic endpoint
'''


class ComicResources(MethodView):
    request_fields = {
        'comic_name': fields.Str(required=True),
        'comic_structure': fields.Str(required=True),
        'comic_script': fields.Str(required=True),
        'group': fields.Str(required=False)
    }

    def post(self):
        logging.debug(request.data)
        data = parser.parse(self.request_fields, request, location="json_or_form")
        logging.debug(f'Comic recommendation:{data}')
        logging.debug(f'request: {request.environ["REMOTE_ADDR"]}')
        data['comic_name'] = data.get('comic_name', str(uuid4()))
        recommend_result, version = recommend(data.get('comic_script'))
        recommend_result = json.dumps(recommend_result)
        data['recomm_result'] = recommend_result
        data['version'] = version
        comic_model = Comic(**data)
        try:
            comic_model.save()
        except TypeError as e:
            return abort(500, str(e))
        return recommend_result
