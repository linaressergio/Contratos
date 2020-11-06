""" Importando base de datos
    """
from .db import db

""" Creando clase contrato """
class Contract(db.Document):
    contract_id = db.StringField(required=True, unique=True)
    plan = db.StringField(required=False)
    insurance_name = db.StringField(required=False)
    state = db.StringField(required=False)
    last_name = db.StringField(required=False)
    principal_name = db.StringField(required=False)
    principal_id = db.StringField(required=False)
    beneficiary = db.ListField(db.StringField(), required=False)
