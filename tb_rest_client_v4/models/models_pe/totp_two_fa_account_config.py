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

class TotpTwoFaAccountConfig(object):
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
        'auth_url': 'str',
        'use_by_default': 'bool'
    }

    attribute_map = {
        'auth_url': 'authUrl',
        'use_by_default': 'useByDefault'
    }

    def __init__(self, auth_url=None, use_by_default=None):  # noqa: E501
        """TotpTwoFaAccountConfig - a model defined in Swagger"""  # noqa: E501
        self._auth_url = None
        self._use_by_default = None
        self.discriminator = None
        self.auth_url = auth_url
        if use_by_default is not None:
            self.use_by_default = use_by_default

    @property
    def auth_url(self):
        """Gets the auth_url of this TotpTwoFaAccountConfig.  # noqa: E501


        :return: The auth_url of this TotpTwoFaAccountConfig.  # noqa: E501
        :rtype: str
        """
        return self._auth_url

    @auth_url.setter
    def auth_url(self, auth_url):
        """Sets the auth_url of this TotpTwoFaAccountConfig.


        :param auth_url: The auth_url of this TotpTwoFaAccountConfig.  # noqa: E501
        :type: str
        """
        if auth_url is None:
            raise ValueError("Invalid value for `auth_url`, must not be `None`")  # noqa: E501

        self._auth_url = auth_url

    @property
    def use_by_default(self):
        """Gets the use_by_default of this TotpTwoFaAccountConfig.  # noqa: E501


        :return: The use_by_default of this TotpTwoFaAccountConfig.  # noqa: E501
        :rtype: bool
        """
        return self._use_by_default

    @use_by_default.setter
    def use_by_default(self, use_by_default):
        """Sets the use_by_default of this TotpTwoFaAccountConfig.


        :param use_by_default: The use_by_default of this TotpTwoFaAccountConfig.  # noqa: E501
        :type: bool
        """

        self._use_by_default = use_by_default

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
        if issubclass(TotpTwoFaAccountConfig, dict):
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
        if not isinstance(other, TotpTwoFaAccountConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
