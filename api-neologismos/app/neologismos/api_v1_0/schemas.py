from marshmallow import fields

from app.ext import ma


class NeologismSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    neologism = fields.String()
    description = fields.String()
    source = fields.String()
    example = fields.String()
    s_term = fields.String()