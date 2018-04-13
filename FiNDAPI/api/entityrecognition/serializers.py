from flask_restplus import fields
from FiNDAPI.api.restplus import api

entity = api.model('Entity', {
    'id': fields.Integer(required=True, description='The unique identifier of the paper.'),
    'entity': fields.String(required=True, description='The assigned entities.'),
})
