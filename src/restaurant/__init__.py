from flask import Blueprint

from .routes import RestaurantItemList


restaurant_bp = Blueprint('restaurant', __name__)
restaurant_bp.add_url_rule('/', view_func=RestaurantItemList.as_view('restaurant_item_list'))
