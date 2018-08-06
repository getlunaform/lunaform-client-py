# coding: utf-8

"""
    lunaform

    This is a RESTful server for managing Terraform plan and apply jobs and the auditing of actions to approve those apply jobs. The inspiration for this project is the AWS CloudFormation API's. The intention is to implement a locking mechanism not only for the terraform state, but for the plan and apply of terraform modules. Once a `module` plan starts, it is instantiated as a `stack` within the nomencalture of `lunaform`.   # noqa: E501

    OpenAPI spec version: 0.0.1-alpha
    Contact: drew.sonne@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.providers_api import ProvidersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestProvidersApi(unittest.TestCase):
    """ProvidersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.providers_api.ProvidersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_provider(self):
        """Test case for create_provider

        """
        pass

    def test_create_provider_configuration(self):
        """Test case for create_provider_configuration

        """
        pass

    def test_delete_provider(self):
        """Test case for delete_provider

        """
        pass

    def test_delete_provider_configuration(self):
        """Test case for delete_provider_configuration

        """
        pass

    def test_get_provider(self):
        """Test case for get_provider

        """
        pass

    def test_get_provider_configuration(self):
        """Test case for get_provider_configuration

        """
        pass

    def test_list_provider_configurations(self):
        """Test case for list_provider_configurations

        """
        pass

    def test_list_providers(self):
        """Test case for list_providers

        """
        pass

    def test_update_provider(self):
        """Test case for update_provider

        """
        pass


if __name__ == '__main__':
    unittest.main()
