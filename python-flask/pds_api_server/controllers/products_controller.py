import connexion
import six

from pds_api_server.models.pds4_label import PDS4Label  # noqa: E501
from pds_api_server import util


def products(start=None, limit=None, q=None, fields=None, sort=None):  # noqa: E501
    """search across all PDS data products, including bundles, collections, documentation, and observational products,

     # noqa: E501

    :param start: offset in matching result list, for pagination
    :type start: int
    :param limit: maximum number of matching results returned, for pagination
    :type limit: int
    :param q: search query
    :type q: str
    :param fields: returned fields, syntax field0,field1
    :type fields: List[str]
    :param sort: sort results, syntax asc(field0),desc(field1)
    :type sort: List[str]

    :rtype: PDS4Label
    """
    return 'do some magic!'


def products_by_lidvid(lidvid):  # noqa: E501
    """URN resolver for lidvid

     # noqa: E501

    :param lidvid: lidvid (urn)
    :type lidvid: str

    :rtype: PDS4Label
    """
    return 'do some magic!'
