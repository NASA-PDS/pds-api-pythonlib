import connexion
import six

from swagger_server.models.error_message import ErrorMessage  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server.models.products import Products  # noqa: E501
from swagger_server import util


def bundle_by_lidvid(lidvid):  # noqa: E501
    """bundle URN resolver for lidvid, get one bundle

     # noqa: E501

    :param lidvid: lidvid (urn)
    :type lidvid: str

    :rtype: Product
    """
    return 'do some magic!'


def get_bundles(start=None, limit=None, q=None, fields=None, sort=None, only_summary=None):  # noqa: E501
    """request all PDS bundles

     # noqa: E501

    :param start: offset in matching result list, for pagination
    :type start: int
    :param limit: maximum number of matching results returned, for pagination
    :type limit: int
    :param q: search query, complex query uses eq,ne,gt,ge,lt,le,(,),not,and,or. Properties are named as in &#x27;properties&#x27; attributes, literals are strings between \&quot; or numbers. Detailed query specification is available at https://bit.ly/393i1af
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
