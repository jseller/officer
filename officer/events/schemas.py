
from marshmallow import Schema, fields


class EventSchema(Schema):
    name = fields.Str()
    title = fields.Str()
    when = fields.Dict(
        keys=fields.Str(),
        values=fields.Str()
    )
