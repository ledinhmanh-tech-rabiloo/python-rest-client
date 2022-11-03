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

class AdminSettings(object):
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
        'id': 'AdminSettingsId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'key': 'str',
        'json_value': 'JsonNode'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'key': 'key',
        'json_value': 'jsonValue'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, key=None, json_value=None):  # noqa: E501
        """AdminSettings - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._key = None
        self._json_value = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if key is not None:
            self.key = key
        if json_value is not None:
            self.json_value = json_value

    @property
    def id(self):
        """Gets the id of this AdminSettings.  # noqa: E501


        :return: The id of this AdminSettings.  # noqa: E501
        :rtype: AdminSettingsId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdminSettings.


        :param id: The id of this AdminSettings.  # noqa: E501
        :type: AdminSettingsId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this AdminSettings.  # noqa: E501

        Timestamp of the settings creation, in milliseconds  # noqa: E501

        :return: The created_time of this AdminSettings.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this AdminSettings.

        Timestamp of the settings creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this AdminSettings.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AdminSettings.  # noqa: E501


        :return: The tenant_id of this AdminSettings.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AdminSettings.


        :param tenant_id: The tenant_id of this AdminSettings.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def key(self):
        """Gets the key of this AdminSettings.  # noqa: E501

        The Administration Settings key, (e.g. 'general' or 'mail')  # noqa: E501

        :return: The key of this AdminSettings.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AdminSettings.

        The Administration Settings key, (e.g. 'general' or 'mail')  # noqa: E501

        :param key: The key of this AdminSettings.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def json_value(self):
        """Gets the json_value of this AdminSettings.  # noqa: E501


        :return: The json_value of this AdminSettings.  # noqa: E501
        :rtype: JsonNode
        """
        return self._json_value

    @json_value.setter
    def json_value(self, json_value):
        """Sets the json_value of this AdminSettings.


        :param json_value: The json_value of this AdminSettings.  # noqa: E501
        :type: JsonNode
        """

        self._json_value = json_value

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
        if issubclass(AdminSettings, dict):
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
        if not isinstance(other, AdminSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
