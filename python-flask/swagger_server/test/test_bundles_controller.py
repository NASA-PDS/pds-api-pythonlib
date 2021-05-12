# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_message import ErrorMessage  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server.models.products import Products  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBundlesController(BaseTestCase):
    """BundlesController integration test stubs"""

    def test_bundle_by_lidvid(self):
        """Test case for bundle_by_lidvid

        bundle URN resolver for lidvid, get one bundle
        """
        response = self.client.open(
            '/PDS_APIs/pds_federated_api/0.1.0/bundles/{lidvid}'.format(lidvid='lidvid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_bundles(self):
        """Test case for get_bundles

        request all PDS bundles
        """
        query_string = [('start', 0),
                        ('limit', 100),
                        ('q', 'q_example'),
                        ('fields', 'fields_example'),
                        ('sort', 'sort_example'),
                        ('only_summary', false)]
        response = self.client.open(
            '/PDS_APIs/pds_federated_api/0.1.0/bundles',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
