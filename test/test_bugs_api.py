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
from swagger_client.api.bugs_api import BugsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBugsApi(unittest.TestCase):
    """BugsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.bugs_api.BugsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_bugs(self):
        """Test case for get_bugs

        Return all bugs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
