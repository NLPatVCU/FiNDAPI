import logging

from flask_restplus import Api
from FiNDAPI import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='FiNDAPI',
          description='An API that will parse any academic journal in a multitude of formats and provide a convient way '
                      'to store and retrieve those documents as well as add aditional metadata.')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500
