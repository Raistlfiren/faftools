"""
Contains marshmallow schemas for the JSON+API compatible part of the FAF api
"""
from .ranked1v1_stats_schema import Ranked1v1StatsSchema
from .achievement_schema import AchievementSchema
from .event_schema import EventSchema
from .rating_schema import RatingSchema
from .login_schema import LoginSchema
from .player_achievement_schema import PlayerAchievementSchema
from .player_event_schema import PlayerEventSchema
from .player_schema import PlayerSchema, RatingSchema
from .mod_schema import ModSchema
from .map_schema import MapSchema
from .bugreport_schema import BugReportSchema, BugReportTargetSchema

# Increment me according to semver rules for compatibility
API_VERSION = '0.2.0'

API_TYPES = {
    'player': PlayerSchema,
    'mod': ModSchema,
    'map': MapSchema,
    'achievement': AchievementSchema,
    'player_achievement': PlayerAchievementSchema,
    'event': EventSchema,
    'player_event': PlayerEventSchema,
    'bugreport': BugReportSchema,
    'bugreport_target': BugReportTargetSchema,
    'rating': RatingSchema,
    'login': LoginSchema,
    'ranked1v1_stats': Ranked1v1StatsSchema
}

FAF_API_URL = 'http://api.dev.faforever.com'

from .client import ApiClient
