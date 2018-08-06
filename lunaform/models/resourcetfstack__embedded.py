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

from swagger_client.models.resource_tf_deployment import ResourceTfDeployment  # noqa: F401,E501
from swagger_client.models.resource_tf_workspace import ResourceTfWorkspace  # noqa: F401,E501


class ResourcetfstackEmbedded(object):
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
        'deployments': 'list[ResourceTfDeployment]',
        'workspace': 'ResourceTfWorkspace'
    }

    attribute_map = {
        'deployments': 'deployments',
        'workspace': 'workspace'
    }

    def __init__(self, deployments=None, workspace=None):  # noqa: E501
        """ResourcetfstackEmbedded - a model defined in Swagger"""  # noqa: E501

        self._deployments = None
        self._workspace = None
        self.discriminator = None

        if deployments is not None:
            self.deployments = deployments
        if workspace is not None:
            self.workspace = workspace

    @property
    def deployments(self):
        """Gets the deployments of this ResourcetfstackEmbedded.  # noqa: E501


        :return: The deployments of this ResourcetfstackEmbedded.  # noqa: E501
        :rtype: list[ResourceTfDeployment]
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        """Sets the deployments of this ResourcetfstackEmbedded.


        :param deployments: The deployments of this ResourcetfstackEmbedded.  # noqa: E501
        :type: list[ResourceTfDeployment]
        """

        self._deployments = deployments

    @property
    def workspace(self):
        """Gets the workspace of this ResourcetfstackEmbedded.  # noqa: E501


        :return: The workspace of this ResourcetfstackEmbedded.  # noqa: E501
        :rtype: ResourceTfWorkspace
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ResourcetfstackEmbedded.


        :param workspace: The workspace of this ResourcetfstackEmbedded.  # noqa: E501
        :type: ResourceTfWorkspace
        """

        self._workspace = workspace

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
        if not isinstance(other, ResourcetfstackEmbedded):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other