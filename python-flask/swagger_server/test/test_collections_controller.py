# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_message import ErrorMessage  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server.models.products import Products  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCollectionsController(BaseTestCase):
    """CollectionsController integration test stubs"""

    def test_collections_by_lidvid(self):
        """Test case for collections_by_lidvid

        collections URN resolver for lidvid
        """
        response = self.client.open(
            '/PDS_APIs/pds_federated_api/0.1.0/collections/{lidvid}'.format(lidvid='lidvid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_collection(self):
        """Test case for get_collection

        request PDS collections
        """
        query_string = [('start', 0),
                        ('limit', 100),
                        ('q', 'q_example'),
                        ('fields', 'fields_example'),
                        ('sort', 'sort_example'),
                        ('only_summary', false)]
        response = self.client.open(
            '/PDS_APIs/pds_federated_api/0.1.0/collections',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
