import sqlalchemy as sa

from ..core.extensions import db


class MenuItem(db.Model):
    __tablename__ = 'menu_item'
    __table_args__ = (
        sa.PrimaryKeyConstraint('restaurant_id', 'id', name='menu_item__pk'),
    )

    id = sa.Column(sa.Integer)
    restaurant_id = sa.Column(sa.Integer)
    name = sa.Column(sa.UnicodeText, nullable=False)
    isStandalone = sa.Column(sa.Boolean, nullable=False)


class Modifier(db.Model):
    __tablename__ = 'modifier'
    __table_args__ = (
        sa.PrimaryKeyConstraint('restaurant_id', 'main_item_id', 'modifier_id', name='modifier__pk'),
        sa.ForeignKeyConstraint(('restaurant_id', 'main_item_id'),
            ('menu_item.restaurant_id', 'menu_item.id'),
            onupdate='CASCADE', ondelete='CASCADE', name='main_item__menu_item__fk'),
        sa.ForeignKeyConstraint(('restaurant_id', 'modifier_id'),
            ('menu_item.restaurant_id', 'menu_item.id'),
            onupdate='CASCADE', ondelete='CASCADE', name='modifier__menu_item__fk'),
    )

    restaurant_id = sa.Column(sa.Integer)
    main_item_id = sa.Column(sa.Integer)
    modifier_id = sa.Column(sa.Integer)
