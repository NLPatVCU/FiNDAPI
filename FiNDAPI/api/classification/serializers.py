from flask_restplus import fields
from FiNDAPI.api.restplus import api

classification = api.model('Classification', {
    'id': fields.Integer(required=True, description='The unique identifier of the paper.'),
    'classification': fields.String(required=True, description='The assigned classification.'),
})
