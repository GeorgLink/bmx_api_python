# coding: utf-8

"""
    BugMark API

    all calls require BASIC AUTH  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.offers_api import OffersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOffersApi(unittest.TestCase):
    """OffersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.offers_api.OffersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_offers(self):
        """Test case for get_offers

        Return all offers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()