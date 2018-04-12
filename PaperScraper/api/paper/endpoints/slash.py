import logging

from flask import request
from flask_restplus import Resource
from PaperScraper.api.paper.serializers import paper
from PaperScraper.api.paper.operations import create_paper, update_paper, delete_paper
from PaperScraper.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('paper', description='Interact with MongoDB Papers Instance.')


@ns.route('/')
class Paper(Resource):

    @api.marshal_list_with(paper)
    def get(self):
        """
        Returns list of all annotations.
        """
        # TODO
        return []

    @api.response(201, 'Paper successfully added to database.')
    @api.expect(paper)
    def post(self):
        """
        Creates a new blog category.
        """
        data = request.json
        create_paper(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Paper not found.')
class PaperItem(Resource):

    @api.marshal_with(paper)
    def get(self, id):
        """
        Returns a specific annotation.
        """
        # TODO

    @api.expect(paper)
    @api.response(204, 'Paper successfully updated.')
    def put(self, id):
        """
        Updates a annotation.
        """
        data = request.json
        update_paper(id, data)
        return None, 204

    @api.response(204, 'Paper successfully deleted.')
    def delete(self, id):
        """
        Deletes an annotation.
        """
        delete_paper(id)
        return None, 204