""" Importando MongoEngine
    """
from flask_mongoengine import MongoEngine

db = MongoEngine()

""" Iniciando bd
    """
def initialize_db(app):
    """Iniciando app """
    db.init_app(app)
