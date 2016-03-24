from marshmallow_jsonapi import Schema, fields


class RatingSchema(Schema):
    """
    Represents rating metadata
    """
    id = fields.String()
    mean = fields.Float()
    deviation = fields.Float()
    num_games = fields.Integer()
    won_games = fields.Integer()
    lost_games = fields.Integer()
    winning_percentage = fields.Float()
    is_active = fields.Boolean()
    rating = fields.Integer()
    ranking = fields.Integer()

    class Meta:
        type_ = 'rating'
