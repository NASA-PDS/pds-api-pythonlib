# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from pds_api_server.models.pds4_label import PDS4Label  # noqa: E501
from pds_api_server.test import BaseTestCase


class TestProductsController(BaseTestCase):
    """ProductsController integration test stubs"""

    def test_products(self):
        """Test case for products

        search across all PDS data products, including bundles, collections, documentation, and observational products,
        """
        query_string = [('start', 56),
                        ('limit', 56),
                        ('q', 'q_example'),
                        ('fields', 'fields_example'),
                        ('sort', 'sort_example')]
        response = self.client.open(
            '/PDS_APIs/pds_federated_api/0.1.0/products',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_by_lidvid(self):
        """Test case for products_by_lidvid

        URN resolver for lidvid
        """
        response = self.client.open(
            '/PDS_APIs/pds_federated_api/0.1.0/products/{lidvid}'.format(lidvid='lidvid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
