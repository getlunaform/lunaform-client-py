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
from swagger_client.models.response_list_tf_providers import ResponseListTfProviders  # noqa: E501
from swagger_client.rest import ApiException


class TestResponseListTfProviders(unittest.TestCase):
    """ResponseListTfProviders unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseListTfProviders(self):
        """Test ResponseListTfProviders"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.response_list_tf_providers.ResponseListTfProviders()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
