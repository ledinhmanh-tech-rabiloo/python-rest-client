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

class OAuth2DomainInfo(object):
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
        'name': 'str',
        'scheme': 'str'
    }

    attribute_map = {
        'name': 'name',
        'scheme': 'scheme'
    }

    def __init__(self, name=None, scheme=None):  # noqa: E501
        """OAuth2DomainInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._scheme = None
        self.discriminator = None
        self.name = name
        self.scheme = scheme

    @property
    def name(self):
        """Gets the name of this OAuth2DomainInfo.  # noqa: E501

        Domain name. Cannot be empty  # noqa: E501

        :return: The name of this OAuth2DomainInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OAuth2DomainInfo.

        Domain name. Cannot be empty  # noqa: E501

        :param name: The name of this OAuth2DomainInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def scheme(self):
        """Gets the scheme of this OAuth2DomainInfo.  # noqa: E501

        Domain scheme. Mixed scheme means than both HTTP and HTTPS are going to be used  # noqa: E501

        :return: The scheme of this OAuth2DomainInfo.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this OAuth2DomainInfo.

        Domain scheme. Mixed scheme means than both HTTP and HTTPS are going to be used  # noqa: E501

        :param scheme: The scheme of this OAuth2DomainInfo.  # noqa: E501
        :type: str
        """
        if scheme is None:
            raise ValueError("Invalid value for `scheme`, must not be `None`")  # noqa: E501
        allowed_values = ["HTTP", "HTTPS", "MIXED"]  # noqa: E501
        if scheme not in allowed_values:
            raise ValueError(
                "Invalid value for `scheme` ({0}), must be one of {1}"  # noqa: E501
                .format(scheme, allowed_values)
            )

        self._scheme = scheme

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
        if issubclass(OAuth2DomainInfo, dict):
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
        if not isinstance(other, OAuth2DomainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
