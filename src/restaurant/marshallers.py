from marshmallow import Schema, fields


class MenuItemSchema(Schema):
    id = fields.Integer()
    restaurant_id = fields.Integer()
    name = fields.String()
    main_item_id = fields.Integer()
