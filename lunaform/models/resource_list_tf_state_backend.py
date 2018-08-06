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

from swagger_client.models.resource_tf_state_backend import ResourceTfStateBackend  # noqa: F401,E501


class ResourceListTfStateBackend(object):
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
        'state_backends': 'list[ResourceTfStateBackend]'
    }

    attribute_map = {
        'state_backends': 'state-backends'
    }

    def __init__(self, state_backends=None):  # noqa: E501
        """ResourceListTfStateBackend - a model defined in Swagger"""  # noqa: E501

        self._state_backends = None
        self.discriminator = None

        self.state_backends = state_backends

    @property
    def state_backends(self):
        """Gets the state_backends of this ResourceListTfStateBackend.  # noqa: E501


        :return: The state_backends of this ResourceListTfStateBackend.  # noqa: E501
        :rtype: list[ResourceTfStateBackend]
        """
        return self._state_backends

    @state_backends.setter
    def state_backends(self, state_backends):
        """Sets the state_backends of this ResourceListTfStateBackend.


        :param state_backends: The state_backends of this ResourceListTfStateBackend.  # noqa: E501
        :type: list[ResourceTfStateBackend]
        """
        if state_backends is None:
            raise ValueError("Invalid value for `state_backends`, must not be `None`")  # noqa: E501

        self._state_backends = state_backends

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
        if not isinstance(other, ResourceListTfStateBackend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other