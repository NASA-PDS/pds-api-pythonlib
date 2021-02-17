import connexion
import six

from swagger_server.models.products import Products  # noqa: E501
from swagger_server import util


def collections_of_a_bundle(start=None, limit=None):  # noqa: E501
    """get collections belonging to a given bundle

     # noqa: E501

    :param start: offset in matching result list, for pagination
    :type start: int
    :param limit: maximum number of matching results returned, for pagination
    :type limit: int

    :rtype: Products
    """
    return 'do some magic!'
