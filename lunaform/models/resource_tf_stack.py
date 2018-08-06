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

from swagger_client.models.hal_rsc_links import HalRscLinks  # noqa: F401,E501
from swagger_client.models.resourcetfstack_embedded import ResourcetfstackEmbedded  # noqa: F401,E501


class ResourceTfStack(object):
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
        'links': 'HalRscLinks',
        'embedded': 'ResourcetfstackEmbedded',
        'id': 'str',
        'name': 'str',
        'module_id': 'str',
        'status': 'str',
        'workspace': 'str',
        'variables': 'dict(str, str)'
    }

    attribute_map = {
        'links': '_links',
        'embedded': '_embedded',
        'id': 'id',
        'name': 'name',
        'module_id': 'module-id',
        'status': 'status',
        'workspace': 'workspace',
        'variables': 'variables'
    }

    def __init__(self, links=None, embedded=None, id=None, name=None, module_id=None, status=None, workspace=None, variables=None):  # noqa: E501
        """ResourceTfStack - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._embedded = None
        self._id = None
        self._name = None
        self._module_id = None
        self._status = None
        self._workspace = None
        self._variables = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded
        if id is not None:
            self.id = id
        self.name = name
        self.module_id = module_id
        if status is not None:
            self.status = status
        if workspace is not None:
            self.workspace = workspace
        if variables is not None:
            self.variables = variables

    @property
    def links(self):
        """Gets the links of this ResourceTfStack.  # noqa: E501


        :return: The links of this ResourceTfStack.  # noqa: E501
        :rtype: HalRscLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ResourceTfStack.


        :param links: The links of this ResourceTfStack.  # noqa: E501
        :type: HalRscLinks
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this ResourceTfStack.  # noqa: E501


        :return: The embedded of this ResourceTfStack.  # noqa: E501
        :rtype: ResourcetfstackEmbedded
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this ResourceTfStack.


        :param embedded: The embedded of this ResourceTfStack.  # noqa: E501
        :type: ResourcetfstackEmbedded
        """

        self._embedded = embedded

    @property
    def id(self):
        """Gets the id of this ResourceTfStack.  # noqa: E501


        :return: The id of this ResourceTfStack.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceTfStack.


        :param id: The id of this ResourceTfStack.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ResourceTfStack.  # noqa: E501


        :return: The name of this ResourceTfStack.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceTfStack.


        :param name: The name of this ResourceTfStack.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def module_id(self):
        """Gets the module_id of this ResourceTfStack.  # noqa: E501


        :return: The module_id of this ResourceTfStack.  # noqa: E501
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this ResourceTfStack.


        :param module_id: The module_id of this ResourceTfStack.  # noqa: E501
        :type: str
        """
        if module_id is None:
            raise ValueError("Invalid value for `module_id`, must not be `None`")  # noqa: E501

        self._module_id = module_id

    @property
    def status(self):
        """Gets the status of this ResourceTfStack.  # noqa: E501


        :return: The status of this ResourceTfStack.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResourceTfStack.


        :param status: The status of this ResourceTfStack.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEPLOYING", "SUCCESS", "FAIL"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def workspace(self):
        """Gets the workspace of this ResourceTfStack.  # noqa: E501


        :return: The workspace of this ResourceTfStack.  # noqa: E501
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ResourceTfStack.


        :param workspace: The workspace of this ResourceTfStack.  # noqa: E501
        :type: str
        """

        self._workspace = workspace

    @property
    def variables(self):
        """Gets the variables of this ResourceTfStack.  # noqa: E501


        :return: The variables of this ResourceTfStack.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this ResourceTfStack.


        :param variables: The variables of this ResourceTfStack.  # noqa: E501
        :type: dict(str, str)
        """

        self._variables = variables

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
        if not isinstance(other, ResourceTfStack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
