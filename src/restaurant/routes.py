import sqlalchemy as sa
from sqlalchemy.orm import aliased
from flask import jsonify
from flask.views import MethodView

from ..core.errors import NotFound
from ..core.extensions import db
from .models import MenuItem, Modifier


class RestaurantItemList(MethodView):
    def get(self, restaurant_id):
        if restaurant_id != 1:  # Add real check here
            raise NotFound('Restaurant {} not found'.format(restaurant_id))

        #  Main part
        main_cte = db.session.query(
                MenuItem.id,
                MenuItem.name,
                MenuItem.restaurant_id,
                sa.cast(sa.sql.expression.literal(None), sa.Integer).label('main_item_id'))\
            .filter((MenuItem.isStandalone==True) & (MenuItem.restaurant_id==restaurant_id))\
            .cte(name="menu_items", recursive=True)

        # Recursive part
        mod_alias = aliased(MenuItem, name='mod')
        modifiers_q = db.session.query(
                mod_alias.id,
                mod_alias.name,
                mod_alias.restaurant_id,
                Modifier.main_item_id)\
            .join(Modifier, (Modifier.modifier_id==mod_alias.id) & (Modifier.restaurant_id==mod_alias.restaurant_id))\
            .join(main_cte, (main_cte.c.id==Modifier.main_item_id) & (main_cte.c.restaurant_id==Modifier.restaurant_id))

        union = main_cte.union_all(modifiers_q)
        q = db.session.query(union.c.id, union.c.name, union.c.restaurant_id, union.c.main_item_id)

        resp = q.all()

        return jsonify(resp)
