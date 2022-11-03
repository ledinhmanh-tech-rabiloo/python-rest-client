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

class SmsTwoFaProviderConfig(object):
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
        'sms_verification_message_template': 'str',
        'verification_code_lifetime': 'int'
    }

    attribute_map = {
        'sms_verification_message_template': 'smsVerificationMessageTemplate',
        'verification_code_lifetime': 'verificationCodeLifetime'
    }

    def __init__(self, sms_verification_message_template=None, verification_code_lifetime=None):  # noqa: E501
        """SmsTwoFaProviderConfig - a model defined in Swagger"""  # noqa: E501
        self._sms_verification_message_template = None
        self._verification_code_lifetime = None
        self.discriminator = None
        self.sms_verification_message_template = sms_verification_message_template
        if verification_code_lifetime is not None:
            self.verification_code_lifetime = verification_code_lifetime

    @property
    def sms_verification_message_template(self):
        """Gets the sms_verification_message_template of this SmsTwoFaProviderConfig.  # noqa: E501


        :return: The sms_verification_message_template of this SmsTwoFaProviderConfig.  # noqa: E501
        :rtype: str
        """
        return self._sms_verification_message_template

    @sms_verification_message_template.setter
    def sms_verification_message_template(self, sms_verification_message_template):
        """Sets the sms_verification_message_template of this SmsTwoFaProviderConfig.


        :param sms_verification_message_template: The sms_verification_message_template of this SmsTwoFaProviderConfig.  # noqa: E501
        :type: str
        """
        if sms_verification_message_template is None:
            raise ValueError("Invalid value for `sms_verification_message_template`, must not be `None`")  # noqa: E501

        self._sms_verification_message_template = sms_verification_message_template

    @property
    def verification_code_lifetime(self):
        """Gets the verification_code_lifetime of this SmsTwoFaProviderConfig.  # noqa: E501


        :return: The verification_code_lifetime of this SmsTwoFaProviderConfig.  # noqa: E501
        :rtype: int
        """
        return self._verification_code_lifetime

    @verification_code_lifetime.setter
    def verification_code_lifetime(self, verification_code_lifetime):
        """Sets the verification_code_lifetime of this SmsTwoFaProviderConfig.


        :param verification_code_lifetime: The verification_code_lifetime of this SmsTwoFaProviderConfig.  # noqa: E501
        :type: int
        """

        self._verification_code_lifetime = verification_code_lifetime

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
        if issubclass(SmsTwoFaProviderConfig, dict):
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
        if not isinstance(other, SmsTwoFaProviderConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
