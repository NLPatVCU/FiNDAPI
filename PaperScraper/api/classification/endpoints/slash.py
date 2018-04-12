import logging

from flask import request
from flask_restplus import Resource
from PaperScraper.api.classification.serializers import classification
from PaperScraper.api.classification.operations import create_classification, update_classification
from PaperScraper.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('classification', description='Classify a paper which exists in the database.')


@ns.route('/')
class Annotation(Resource):

    @api.marshal_list_with(classification)
    def get(self):
        """
        Returns list of all classifications.
        """
        # TODO
        return []


@ns.route('/<int:id>')
@api.response(404, 'Classification not found.')
class CategoryItem(Resource):

    @api.marshal_with(classification)
    def get(self, id):
        """
        Returns a specific annotation.
        """
        # TODO

    @api.expect(classification)
    @api.response(204, 'Classification successfully updated.')
    def put(self, id):
        """
        Updates a annotation.
        """
        data = request.json
        update_classification(id, data)
        return None, 204