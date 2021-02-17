# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.products import Products  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBundlesCollectionsController(BaseTestCase):
    """BundlesCollectionsController integration test stubs"""

    def test_collections_of_a_bundle(self):
        """Test case for collections_of_a_bundle

        get collections belonging to a given bundle
        """
        response = self.client.open(
            '/PDS_APIs/pds_federated_api/0.1.0/bundles/{lidvid}/collections'.format(lidvid='lidvid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
