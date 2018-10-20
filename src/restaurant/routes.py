from flask import jsonify
from flask.views import MethodView


class RestaurantItemList(MethodView):
    def get(self):
        resp = {}

        return jsonify(resp)
