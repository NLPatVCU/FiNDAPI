from flask_restplus import fields
from PaperScraper.api.restplus import api

annotation = api.model('Annotaion', {
    'id': fields.Integer(required=True, description='The unique identifier of the annotator.'),
    'annotation': fields.String(required=True, description='The annotation made.'),
})
