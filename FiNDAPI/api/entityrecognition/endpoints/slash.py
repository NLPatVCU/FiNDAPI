import logging

from flask import request
from flask_restplus import Resource
from FiNDAPI.api.entityrecognition.serializers import entity
from FiNDAPI.api.entityrecognition.operations import get_entities, update_entities, remove_entities
from FiNDAPI.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('entityrecognition', description='Allows for the retrieval, modification, insertion, and removal '
                                                    'of entities for a given paper in the database.')


@ns.route('/<int:id>')
@api.response(404, 'Entities not found.')
class EntityItem(Resource):

    @api.marshal_with(entity)
    def get(self, id):
        """
        Returns the entities related to a paper in the database.
        """
        # TODO


    @api.expect(entity)
    @api.response(204, 'Entities successfully updated.')
    def put(self, id):
        """
        Updates entities on a paper.
        """
        data = request.json
        update_entities(id, data)
        return None, 204

    @api.response(204, 'All entities removed.')
    def delete(self, id):
        """
        Removes all entities from a paper.
        """
        remove_entities(id)
        return None, 204