# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EntityRelationInfo(object):
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
        '_from': 'EntityId',
        'to': 'EntityId',
        'type': 'str',
        'type_group': 'str',
        'additional_info': 'JsonNode',
        'from_name': 'str',
        'to_name': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'type': 'type',
        'type_group': 'typeGroup',
        'additional_info': 'additionalInfo',
        'from_name': 'fromName',
        'to_name': 'toName'
    }

    def __init__(self, _from=None, to=None, type=None, type_group=None, additional_info=None, from_name=None, to_name=None):  # noqa: E501
        """EntityRelationInfo - a model defined in Swagger"""  # noqa: E501
        self.__from = None
        self._to = None
        self._type = None
        self._type_group = None
        self._additional_info = None
        self._from_name = None
        self._to_name = None
        self.discriminator = None
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if type is not None:
            self.type = type
        if type_group is not None:
            self.type_group = type_group
        if additional_info is not None:
            self.additional_info = additional_info
        if from_name is not None:
            self.from_name = from_name
        if to_name is not None:
            self.to_name = to_name

    @property
    def _from(self):
        """Gets the _from of this EntityRelationInfo.  # noqa: E501


        :return: The _from of this EntityRelationInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this EntityRelationInfo.


        :param _from: The _from of this EntityRelationInfo.  # noqa: E501
        :type: EntityId
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this EntityRelationInfo.  # noqa: E501


        :return: The to of this EntityRelationInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this EntityRelationInfo.


        :param to: The to of this EntityRelationInfo.  # noqa: E501
        :type: EntityId
        """

        self._to = to

    @property
    def type(self):
        """Gets the type of this EntityRelationInfo.  # noqa: E501

        String value of relation type.  # noqa: E501

        :return: The type of this EntityRelationInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntityRelationInfo.

        String value of relation type.  # noqa: E501

        :param type: The type of this EntityRelationInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def type_group(self):
        """Gets the type_group of this EntityRelationInfo.  # noqa: E501

        Represents the type group of the relation.  # noqa: E501

        :return: The type_group of this EntityRelationInfo.  # noqa: E501
        :rtype: str
        """
        return self._type_group

    @type_group.setter
    def type_group(self, type_group):
        """Sets the type_group of this EntityRelationInfo.

        Represents the type group of the relation.  # noqa: E501

        :param type_group: The type_group of this EntityRelationInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["COMMON", "DASHBOARD", "EDGE", "EDGE_AUTO_ASSIGN_RULE_CHAIN", "RULE_CHAIN", "RULE_NODE"]  # noqa: E501
        if type_group not in allowed_values:
            raise ValueError(
                "Invalid value for `type_group` ({0}), must be one of {1}"  # noqa: E501
                .format(type_group, allowed_values)
            )

        self._type_group = type_group

    @property
    def additional_info(self):
        """Gets the additional_info of this EntityRelationInfo.  # noqa: E501


        :return: The additional_info of this EntityRelationInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this EntityRelationInfo.


        :param additional_info: The additional_info of this EntityRelationInfo.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def from_name(self):
        """Gets the from_name of this EntityRelationInfo.  # noqa: E501

        Name of the entity for [from] direction.  # noqa: E501

        :return: The from_name of this EntityRelationInfo.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this EntityRelationInfo.

        Name of the entity for [from] direction.  # noqa: E501

        :param from_name: The from_name of this EntityRelationInfo.  # noqa: E501
        :type: str
        """

        self._from_name = from_name

    @property
    def to_name(self):
        """Gets the to_name of this EntityRelationInfo.  # noqa: E501

        Name of the entity for [to] direction.  # noqa: E501

        :return: The to_name of this EntityRelationInfo.  # noqa: E501
        :rtype: str
        """
        return self._to_name

    @to_name.setter
    def to_name(self, to_name):
        """Sets the to_name of this EntityRelationInfo.

        Name of the entity for [to] direction.  # noqa: E501

        :param to_name: The to_name of this EntityRelationInfo.  # noqa: E501
        :type: str
        """

        self._to_name = to_name

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
        if issubclass(EntityRelationInfo, dict):
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
        if not isinstance(other, EntityRelationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
