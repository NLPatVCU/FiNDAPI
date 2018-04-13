from flask_restplus import fields
from FiNDAPI.api.restplus import api

annotation = api.model('Annotaion', {
    'id': fields.Integer(required=True, description='The unique identifier of the paper.'),
    'annotation': fields.String(required=True, description='The annotation.'),
})
