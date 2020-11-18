import connexion
import six

from swagger_server.models.error_message import ErrorMessage  # noqa: E501
from swagger_server.models.products import Products  # noqa: E501
from swagger_server import util


def get_collection(start=None, limit=None, q=None, fields=None, sort=None, only_summary=None):  # noqa: E501
    """request PDS collections

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
    :param only_summary: only return the summary, useful to get the list of available properties
    :type only_summary: bool

    :rtype: Products
    """
    return 'do some magic!'
