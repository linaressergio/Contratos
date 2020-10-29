from flask import Response, request
from database.models import Contract
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource


class ContractsApi(Resource):
    def get(self):
        contracts = Contract.objects().to_json()
        return Response(contract, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        contracts = Contract(**body).save()
        contract_id  = contracts.contract_id 
        return {'contract_id ': str(contract_id)}, 200


class ContractApi(Resource):
    @jwt_required
    def put(self, contract_id):
        body = request.get_json()
        Contract.objects.get(contract_id=contract_id).update(**body)
        return '', 200

    @jwt_required
    def delete(self, contract_id):
        contract = Contract.objects.get(contract_id=contract_id).delete()
        return '', 200

    def get(self, id):
        try:
            contract = Contract.objects.get(id=id).to_json()
            return Response(contract, mimetype="application/json", status=200)
        except Exception as error:
            return Response(error, status=400, mimetype='application/json')
