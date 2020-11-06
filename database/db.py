from flask_mongoengine import MongoEngine
""" importando MongoEngine """


db = MongoEngine()


def initialize_db(app):
    db.init_app(app)
