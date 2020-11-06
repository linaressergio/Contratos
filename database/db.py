""" importando MongoEngine 
    """
from flask_mongoengine import MongoEngine

db = MongoEngine()

""" iniciando aplicacion 
    """
def initialize_db(app):
    db.init_app(app)
