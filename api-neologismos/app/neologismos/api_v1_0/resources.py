from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import NeologismSchema
from ..models import Neologism

neo_v1_0_bp = Blueprint('neo_v1_0_bp', __name__)

neo_schema = NeologismSchema()

api = Api(neo_v1_0_bp)

class NeologismListResource(Resource):
    def get(self):
        neologisms = Neologism.get_all()
        result = neo_schema.dump(neologisms, many=True)
        return result
        
    def post(self):
        data = request.get_json()
        neo_dict = neo_schema.load(data)
        neologism = Neologism(neologism=neo_dict['neologism'],
                    description=neo_dict['description'],
                    source=neo_dict['source'],
                    example=neo_dict['example'],
                    s_term=neo_dict['s_term']
        )
        neologism.save()
        resp = neo_schema.dump(neologism)
        return resp, 201
    
   
class NeologismResource(Resource):
    def get(self, neo_id):
        neologism = Neologism.get_by_id(neo_id)
        if neologism is None:
            raise ObjectNotFound('Este neologismo no existe')
        resp = neo_schema.dump(neologism)
        return resp
    def delete(self, neo_id):
        neologism = Neologism.get_by_id(neo_id)
        if neologism is None:
            raise ObjectNotFound('Este neologismo no existe')
        resp = neo_schema.dump(neologism)
        neologism.delete()
        return resp
    
api.add_resource(NeologismListResource, '/api/v1.0/neo/', endpoint='neo_list_resource')
api.add_resource(NeologismResource, '/api/v1.0/neo/<int:neo_id>', endpoint='neo_resource')