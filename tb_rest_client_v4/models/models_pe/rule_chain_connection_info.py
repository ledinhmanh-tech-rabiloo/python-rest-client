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

class RuleChainConnectionInfo(object):
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
        'from_index': 'int',
        'target_rule_chain_id': 'RuleChainId',
        'additional_info': 'JsonNode',
        'type': 'str'
    }

    attribute_map = {
        'from_index': 'fromIndex',
        'target_rule_chain_id': 'targetRuleChainId',
        'additional_info': 'additionalInfo',
        'type': 'type'
    }

    def __init__(self, from_index=None, target_rule_chain_id=None, additional_info=None, type=None):  # noqa: E501
        """RuleChainConnectionInfo - a model defined in Swagger"""  # noqa: E501
        self._from_index = None
        self._target_rule_chain_id = None
        self._additional_info = None
        self._type = None
        self.discriminator = None
        self.from_index = from_index
        self.target_rule_chain_id = target_rule_chain_id
        self.additional_info = additional_info
        self.type = type

    @property
    def from_index(self):
        """Gets the from_index of this RuleChainConnectionInfo.  # noqa: E501

        Index of rule node in the 'nodes' array of the RuleChainMetaData. Indicates the 'from' part of the connection.  # noqa: E501

        :return: The from_index of this RuleChainConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._from_index

    @from_index.setter
    def from_index(self, from_index):
        """Sets the from_index of this RuleChainConnectionInfo.

        Index of rule node in the 'nodes' array of the RuleChainMetaData. Indicates the 'from' part of the connection.  # noqa: E501

        :param from_index: The from_index of this RuleChainConnectionInfo.  # noqa: E501
        :type: int
        """
        if from_index is None:
            raise ValueError("Invalid value for `from_index`, must not be `None`")  # noqa: E501

        self._from_index = from_index

    @property
    def target_rule_chain_id(self):
        """Gets the target_rule_chain_id of this RuleChainConnectionInfo.  # noqa: E501


        :return: The target_rule_chain_id of this RuleChainConnectionInfo.  # noqa: E501
        :rtype: RuleChainId
        """
        return self._target_rule_chain_id

    @target_rule_chain_id.setter
    def target_rule_chain_id(self, target_rule_chain_id):
        """Sets the target_rule_chain_id of this RuleChainConnectionInfo.


        :param target_rule_chain_id: The target_rule_chain_id of this RuleChainConnectionInfo.  # noqa: E501
        :type: RuleChainId
        """
        if target_rule_chain_id is None:
            raise ValueError("Invalid value for `target_rule_chain_id`, must not be `None`")  # noqa: E501

        self._target_rule_chain_id = target_rule_chain_id

    @property
    def additional_info(self):
        """Gets the additional_info of this RuleChainConnectionInfo.  # noqa: E501


        :return: The additional_info of this RuleChainConnectionInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this RuleChainConnectionInfo.


        :param additional_info: The additional_info of this RuleChainConnectionInfo.  # noqa: E501
        :type: JsonNode
        """
        if additional_info is None:
            raise ValueError("Invalid value for `additional_info`, must not be `None`")  # noqa: E501

        self._additional_info = additional_info

    @property
    def type(self):
        """Gets the type of this RuleChainConnectionInfo.  # noqa: E501

        Type of the relation. Typically indicated the result of processing by the 'from' rule node. For example, 'Success' or 'Failure'  # noqa: E501

        :return: The type of this RuleChainConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuleChainConnectionInfo.

        Type of the relation. Typically indicated the result of processing by the 'from' rule node. For example, 'Success' or 'Failure'  # noqa: E501

        :param type: The type of this RuleChainConnectionInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(RuleChainConnectionInfo, dict):
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
        if not isinstance(other, RuleChainConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
