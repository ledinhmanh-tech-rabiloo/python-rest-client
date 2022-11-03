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

class SnmpCommunicationConfig(object):
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
        'spec': 'str'
    }

    attribute_map = {
        'spec': 'spec'
    }

    def __init__(self, spec=None):  # noqa: E501
        """SnmpCommunicationConfig - a model defined in Swagger"""  # noqa: E501
        self._spec = None
        self.discriminator = None
        if spec is not None:
            self.spec = spec

    @property
    def spec(self):
        """Gets the spec of this SnmpCommunicationConfig.  # noqa: E501


        :return: The spec of this SnmpCommunicationConfig.  # noqa: E501
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this SnmpCommunicationConfig.


        :param spec: The spec of this SnmpCommunicationConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLIENT_ATTRIBUTES_QUERYING", "SHARED_ATTRIBUTES_SETTING", "TELEMETRY_QUERYING", "TO_DEVICE_RPC_REQUEST"]  # noqa: E501
        if spec not in allowed_values:
            raise ValueError(
                "Invalid value for `spec` ({0}), must be one of {1}"  # noqa: E501
                .format(spec, allowed_values)
            )

        self._spec = spec

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
        if issubclass(SnmpCommunicationConfig, dict):
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
        if not isinstance(other, SnmpCommunicationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
