from flask_restplus import fields
from PaperScraper.api.restplus import api

annotation = api.model('Annotaion', {
    'id': fields.Integer(required=True, description='The unique identifier of the annotator.'),
    'annotation': fields.String(required=True, description='The annotation made.'),
})

paper = api.model('Paper', {
    'id': fields.Integer(required=True, description='The unique identifier of the paper.'),
    'paper': fields.String(required=True, description='The paper.'),
})
