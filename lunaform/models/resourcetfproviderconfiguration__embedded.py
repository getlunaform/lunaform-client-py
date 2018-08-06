# coding: utf-8

"""
    lunaform

    This is a RESTful server for managing Terraform plan and apply jobs and the auditing of actions to approve those apply jobs. The inspiration for this project is the AWS CloudFormation API's. The intention is to implement a locking mechanism not only for the terraform state, but for the plan and apply of terraform modules. Once a `module` plan starts, it is instantiated as a `stack` within the nomencalture of `lunaform`.   # noqa: E501

    OpenAPI spec version: 0.0.1-alpha
    Contact: drew.sonne@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.resource_tf_provider import ResourceTfProvider  # noqa: F401,E501


class ResourcetfproviderconfigurationEmbedded(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'provider': 'ResourceTfProvider'
    }

    attribute_map = {
        'provider': 'provider'
    }

    def __init__(self, provider=None):  # noqa: E501
        """ResourcetfproviderconfigurationEmbedded - a model defined in Swagger"""  # noqa: E501

        self._provider = None
        self.discriminator = None

        if provider is not None:
            self.provider = provider

    @property
    def provider(self):
        """Gets the provider of this ResourcetfproviderconfigurationEmbedded.  # noqa: E501


        :return: The provider of this ResourcetfproviderconfigurationEmbedded.  # noqa: E501
        :rtype: ResourceTfProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ResourcetfproviderconfigurationEmbedded.


        :param provider: The provider of this ResourcetfproviderconfigurationEmbedded.  # noqa: E501
        :type: ResourceTfProvider
        """

        self._provider = provider

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourcetfproviderconfigurationEmbedded):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
