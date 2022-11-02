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

class ShortEntityView(object):
    """NOTE: This class is auto generated by the swagger code generator program.
from tb_rest_client.api_client import ApiClient
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
        'id': 'EntityId',
        'name': 'str',
        'created_time': 'int',
        'device_profile': 'DeviceProfile'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_time': 'createdTime',
        'device_profile': 'deviceProfile'
    }

    def __init__(self, id=None, name=None, created_time=None, device_profile=None):  # noqa: E501
        """ShortEntityView - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.created_time = created_time
        self.device_profile = device_profile

    @property
    def id(self):
        """Gets the id of this ShortEntityView.  # noqa: E501


        :return: The id of this ShortEntityView.  # noqa: E501
        :rtype: EntityId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShortEntityView.


        :param id: The id of this ShortEntityView.  # noqa: E501
        :type: EntityId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ShortEntityView.  # noqa: E501

        Name of the entity  # noqa: E501

        :return: The name of this ShortEntityView.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShortEntityView.

        Name of the entity  # noqa: E501

        :param name: The name of this ShortEntityView.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(ShortEntityView, dict):
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
        if not isinstance(other, ShortEntityView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other