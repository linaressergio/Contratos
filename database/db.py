from flask_mongoengine import MongoEngine
"""
high level support for doing this and that.
"""


db = MongoEngine()


def initialize_db(app):
    db.init_app(app)
