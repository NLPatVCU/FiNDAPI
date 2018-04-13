import logging

from flask import request
from flask_restplus import Resource
from FiNDAPI.api.classification.serializers import classification
from FiNDAPI.api.classification.operations import create_classification, update_classification
from FiNDAPI.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('classification', description='Allows for the retrieval, modification, insertion, and removal '
                                                 'of a classification for an paper in the database.')


@ns.route('/')
class Classification(Resource):

    @api.marshal_list_with(classification)
    def get(self):
        """
        Returns list of all classifications.
        """
        # TODO
        return []


@ns.route('/<int:id>')
@api.response(404, 'Classification not found.')
class ClassificationItem(Resource):

    @api.marshal_with(classification)
    def get(self, id):
        """
        Returns all classifications for a given paper.
        """
        # TODO

    @api.expect(classification)
    @api.response(204, 'Classification successfully updated.')
    def put(self, id):
        """
        Updates a classification on a paper.
        """
        data = request.json
        update_classification(id, data)
        return None, 204