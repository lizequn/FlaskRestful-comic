from flask import make_response, jsonify
from flask import abort as f_abort


def abort(status_code, message=''):
    return f_abort(make_response(jsonify(message=message),status_code))