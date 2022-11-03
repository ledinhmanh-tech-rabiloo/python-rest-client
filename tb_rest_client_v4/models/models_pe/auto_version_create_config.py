# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0PE-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AutoVersionCreateConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.
from tb_rest_client_v4.api_client import ApiClient
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
        'branch': 'str',
        'save_attributes': 'bool',
        'save_credentials': 'bool',
        'save_group_entities': 'bool',
        'save_permissions': 'bool',
        'save_relations': 'bool'
    }

    attribute_map = {
        'branch': 'branch',
        'save_attributes': 'saveAttributes',
        'save_credentials': 'saveCredentials',
        'save_group_entities': 'saveGroupEntities',
        'save_permissions': 'savePermissions',
        'save_relations': 'saveRelations'
    }

    def __init__(self, branch=None, save_attributes=None, save_credentials=None, save_group_entities=None, save_permissions=None, save_relations=None):  # noqa: E501
        """AutoVersionCreateConfig - a model defined in Swagger"""  # noqa: E501
        self._branch = None
        self._save_attributes = None
        self._save_credentials = None
        self._save_group_entities = None
        self._save_permissions = None
        self._save_relations = None
        self.discriminator = None
        if branch is not None:
            self.branch = branch
        if save_attributes is not None:
            self.save_attributes = save_attributes
        if save_credentials is not None:
            self.save_credentials = save_credentials
        if save_group_entities is not None:
            self.save_group_entities = save_group_entities
        if save_permissions is not None:
            self.save_permissions = save_permissions
        if save_relations is not None:
            self.save_relations = save_relations

    @property
    def branch(self):
        """Gets the branch of this AutoVersionCreateConfig.  # noqa: E501


        :return: The branch of this AutoVersionCreateConfig.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this AutoVersionCreateConfig.


        :param branch: The branch of this AutoVersionCreateConfig.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def save_attributes(self):
        """Gets the save_attributes of this AutoVersionCreateConfig.  # noqa: E501


        :return: The save_attributes of this AutoVersionCreateConfig.  # noqa: E501
        :rtype: bool
        """
        return self._save_attributes

    @save_attributes.setter
    def save_attributes(self, save_attributes):
        """Sets the save_attributes of this AutoVersionCreateConfig.


        :param save_attributes: The save_attributes of this AutoVersionCreateConfig.  # noqa: E501
        :type: bool
        """

        self._save_attributes = save_attributes

    @property
    def save_credentials(self):
        """Gets the save_credentials of this AutoVersionCreateConfig.  # noqa: E501


        :return: The save_credentials of this AutoVersionCreateConfig.  # noqa: E501
        :rtype: bool
        """
        return self._save_credentials

    @save_credentials.setter
    def save_credentials(self, save_credentials):
        """Sets the save_credentials of this AutoVersionCreateConfig.


        :param save_credentials: The save_credentials of this AutoVersionCreateConfig.  # noqa: E501
        :type: bool
        """

        self._save_credentials = save_credentials

    @property
    def save_group_entities(self):
        """Gets the save_group_entities of this AutoVersionCreateConfig.  # noqa: E501


        :return: The save_group_entities of this AutoVersionCreateConfig.  # noqa: E501
        :rtype: bool
        """
        return self._save_group_entities

    @save_group_entities.setter
    def save_group_entities(self, save_group_entities):
        """Sets the save_group_entities of this AutoVersionCreateConfig.


        :param save_group_entities: The save_group_entities of this AutoVersionCreateConfig.  # noqa: E501
        :type: bool
        """

        self._save_group_entities = save_group_entities

    @property
    def save_permissions(self):
        """Gets the save_permissions of this AutoVersionCreateConfig.  # noqa: E501


        :return: The save_permissions of this AutoVersionCreateConfig.  # noqa: E501
        :rtype: bool
        """
        return self._save_permissions

    @save_permissions.setter
    def save_permissions(self, save_permissions):
        """Sets the save_permissions of this AutoVersionCreateConfig.


        :param save_permissions: The save_permissions of this AutoVersionCreateConfig.  # noqa: E501
        :type: bool
        """

        self._save_permissions = save_permissions

    @property
    def save_relations(self):
        """Gets the save_relations of this AutoVersionCreateConfig.  # noqa: E501


        :return: The save_relations of this AutoVersionCreateConfig.  # noqa: E501
        :rtype: bool
        """
        return self._save_relations

    @save_relations.setter
    def save_relations(self, save_relations):
        """Sets the save_relations of this AutoVersionCreateConfig.


        :param save_relations: The save_relations of this AutoVersionCreateConfig.  # noqa: E501
        :type: bool
        """

        self._save_relations = save_relations

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
        if issubclass(AutoVersionCreateConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AutoVersionCreateConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
