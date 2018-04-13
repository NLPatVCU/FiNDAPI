import logging

from flask import request
from flask_restplus import Resource
from FiNDAPI.api.annotation.serializers import annotation
from FiNDAPI.api.annotation.operations import create_annotation, update_annotation
from FiNDAPI.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('annotation', description='Allows for the retrieval, modification, insertion, and removal of '
                                             'annotations for a paper in the database.')


@ns.route('/')
class Annotation(Resource):

    @api.marshal_list_with(annotation)
    def get(self):
        """
        Returns list of all annotations made.
        """
        # TODO
        return []


@ns.route('/<int:annotation_id>')
@api.response(404, 'Annotation not found.')
class AnnotationItem(Resource):

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


@ns.route('/<int:paper_id>')
@api.response(404, 'Paper not found.')
class PaperAnnotations(Resource):

    @api.marshal_with(annotation)
    def get(self, paper_id):
        """
        Returns all annotations made on a paper.
        """
        # TODO

    def post(self, paper_id):
        """
        Create an annotation for a given paper.
        """
        # TODO

    @api.expect(annotation)
    @api.response(204, 'Paper annotations successfully updated.')
    def put(self, paper_id):
        """
        Updates annotations made on a paper.
        """
        data = request.json
        update_annotation(id, data)
        return None, 204
