from flask import Blueprint

from .routes import RestaurantItemList


restaurant_bp = Blueprint('restaurant', __name__)
restaurant_bp.add_url_rule('/<int:restaurant_id>/items', view_func=RestaurantItemList.as_view('restaurant_item_list'))
