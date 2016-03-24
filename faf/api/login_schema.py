from marshmallow_jsonapi import Schema, fields


class LoginSchema(Schema):
    """
    Represents login metadata
    """
    id = fields.String()
    login = fields.String()
    email = fields.String()
    steamid = fields.String()

    class Meta:
        type_ = 'login'
