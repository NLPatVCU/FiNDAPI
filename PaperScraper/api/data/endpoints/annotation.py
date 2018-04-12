import logging

from flask import request
from flask_restplus import Resource
from PaperScraper.api.data.serializers import annotation
from PaperScraper.api.data.database import create_annotation, update_annotation, delete_annotation
from PaperScraper.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('data/annotation', description='Interact with MongoDB Annotation Instance.')


@ns.route('/')
class Annotation(Resource):

    @api.marshal_list_with(annotation)
    def get(self):
        """
        Returns list of all annotations.
        """
        # TODO
        return []

    @api.response(201, 'Annotation successfully added to database.')
    @api.expect(annotation)
    def post(self):
        """
        Creates a new blog category.
        """
        data = request.json
        create_annotation(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Annoatation not found.')
class CategoryItem(Resource):

    @api.marshal_with(annotation)
    def get(self, id):
        """
        Returns a specific annotation.
        """
        # TODO

    @api.expect(annotation)
    @api.response(204, 'Annotation successfully updated.')
    def put(self, id):
        """
        Updates a annotation.
        """
        data = request.json
        update_annotation(id, data)
        return None, 204

    @api.response(204, 'Annotation successfully deleted.')
    def delete(self, id):
        """
        Deletes an annotation.
        """
        delete_annotation(id)
        return None, 204