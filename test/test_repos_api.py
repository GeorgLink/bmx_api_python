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
from swagger_client.api.repos_api import ReposApi  # noqa: E501
from swagger_client.rest import ApiException


class TestReposApi(unittest.TestCase):
    """ReposApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.repos_api.ReposApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_repos(self):
        """Test case for get_repos

        Return all repos  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
