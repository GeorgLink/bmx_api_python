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
from swagger_client.api.amendments_api import AmendmentsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAmendmentsApi(unittest.TestCase):
    """AmendmentsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.amendments_api.AmendmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_amendments(self):
        """Test case for get_amendments

        Return all amendments  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
