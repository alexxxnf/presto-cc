from flask import jsonify
from werkzeug.exceptions import HTTPException


def render_json_error(exception):
    err = {}

    if isinstance(exception, HTTPException):
        err['description'] = exception.description
        status_code = exception.code
    else:
        err['description'] = str(exception)
        status_code = 500

    return jsonify(err), status_code
