import connexion
import six

from swagger_server.models.products import Products  # noqa: E501
from swagger_server import util


def collections_of_a_bundle(lidvid):  # noqa: E501
    """get collections belonging to a given bundle

     # noqa: E501

    :param lidvid: lidvid (urn)
    :type lidvid: str

    :rtype: Products
    """
    return 'do some magic!'
