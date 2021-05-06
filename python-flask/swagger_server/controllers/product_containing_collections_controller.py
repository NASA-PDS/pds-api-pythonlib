import connexion
import six

from swagger_server.models.products import Products  # noqa: E501
from swagger_server import util


def collections_containing_product(lidvid, start=None, limit=None, fields=None, sort=None, only_summary=None):  # noqa: E501
    """get collections containing product

     # noqa: E501

    :param lidvid: lidvid (urn)
    :type lidvid: str
    :param start: offset in matching result list, for pagination
    :type start: int
    :param limit: maximum number of matching results returned, for pagination
    :type limit: int
    :param fields: returned fields, syntax field0,field1
    :type fields: List[str]
    :param sort: sort results, syntax asc(field0),desc(field1)
    :type sort: List[str]
    :param only_summary: only return the summary, useful to get the list of available properties
    :type only_summary: bool

    :rtype: Products
    """
    return 'do some magic!'
