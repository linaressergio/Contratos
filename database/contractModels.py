from .db import db

class Contract(db.Document):
    contract_id = db.StringField(required=True, unique=True)
    plan = db.StringField(required=True)
    insurance_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    principal_name = db.StringField(required=True)
    principal_id = db.StringField(required=True, unique=True)
    beneficiary = db.ListField(db.StringField(), required=True)
