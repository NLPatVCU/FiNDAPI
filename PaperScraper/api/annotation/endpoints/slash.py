import logging

from flask import request
from flask_restplus import Resource
from PaperScraper.api.annotation.serializers import annotation
from PaperScraper.api.annotation.operations import create_annotation, update_annotation
from PaperScraper.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('annotation', description='Annotate a paper which exists in the database')


@ns.route('/')
class Annotation(Resource):

    @api.marshal_list_with(annotation)
    def get(self):
        """
        Returns list of all classifications.
        """
        # TODO
        return []


@ns.route('/<int:id>')
@api.response(404, 'Classification not found.')
class CategoryItem(Resource):

    @api.marshal_with(annotation)
    def get(self, id):
        """
        Returns a specific annotation.
        """
        # TODO

    @api.expect(annotation)
    @api.response(204, 'Classification successfully updated.')
    def put(self, id):
        """
        Updates a annotation.
        """
        data = request.json
        update_annotation(id, data)
        return None, 204