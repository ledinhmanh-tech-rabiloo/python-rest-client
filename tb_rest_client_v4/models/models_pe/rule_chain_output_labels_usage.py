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

class RuleChainOutputLabelsUsage(object):
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
        'rule_chain_id': 'RuleChainId',
        'rule_node_id': 'RuleNodeId',
        'rule_chain_name': 'str',
        'rule_node_name': 'str',
        'labels': 'list[str]'
    }

    attribute_map = {
        'rule_chain_id': 'ruleChainId',
        'rule_node_id': 'ruleNodeId',
        'rule_chain_name': 'ruleChainName',
        'rule_node_name': 'ruleNodeName',
        'labels': 'labels'
    }

    def __init__(self, rule_chain_id=None, rule_node_id=None, rule_chain_name=None, rule_node_name=None, labels=None):  # noqa: E501
        """RuleChainOutputLabelsUsage - a model defined in Swagger"""  # noqa: E501
        self._rule_chain_id = None
        self._rule_node_id = None
        self._rule_chain_name = None
        self._rule_node_name = None
        self._labels = None
        self.discriminator = None
        self.rule_chain_id = rule_chain_id
        self.rule_node_id = rule_node_id
        self.rule_chain_name = rule_chain_name
        self.rule_node_name = rule_node_name
        self.labels = labels

    @property
    def rule_chain_id(self):
        """Gets the rule_chain_id of this RuleChainOutputLabelsUsage.  # noqa: E501


        :return: The rule_chain_id of this RuleChainOutputLabelsUsage.  # noqa: E501
        :rtype: RuleChainId
        """
        return self._rule_chain_id

    @rule_chain_id.setter
    def rule_chain_id(self, rule_chain_id):
        """Sets the rule_chain_id of this RuleChainOutputLabelsUsage.


        :param rule_chain_id: The rule_chain_id of this RuleChainOutputLabelsUsage.  # noqa: E501
        :type: RuleChainId
        """
        if rule_chain_id is None:
            raise ValueError("Invalid value for `rule_chain_id`, must not be `None`")  # noqa: E501

        self._rule_chain_id = rule_chain_id

    @property
    def rule_node_id(self):
        """Gets the rule_node_id of this RuleChainOutputLabelsUsage.  # noqa: E501


        :return: The rule_node_id of this RuleChainOutputLabelsUsage.  # noqa: E501
        :rtype: RuleNodeId
        """
        return self._rule_node_id

    @rule_node_id.setter
    def rule_node_id(self, rule_node_id):
        """Sets the rule_node_id of this RuleChainOutputLabelsUsage.


        :param rule_node_id: The rule_node_id of this RuleChainOutputLabelsUsage.  # noqa: E501
        :type: RuleNodeId
        """
        if rule_node_id is None:
            raise ValueError("Invalid value for `rule_node_id`, must not be `None`")  # noqa: E501

        self._rule_node_id = rule_node_id

    @property
    def rule_chain_name(self):
        """Gets the rule_chain_name of this RuleChainOutputLabelsUsage.  # noqa: E501

        Rule Chain Name  # noqa: E501

        :return: The rule_chain_name of this RuleChainOutputLabelsUsage.  # noqa: E501
        :rtype: str
        """
        return self._rule_chain_name

    @rule_chain_name.setter
    def rule_chain_name(self, rule_chain_name):
        """Sets the rule_chain_name of this RuleChainOutputLabelsUsage.

        Rule Chain Name  # noqa: E501

        :param rule_chain_name: The rule_chain_name of this RuleChainOutputLabelsUsage.  # noqa: E501
        :type: str
        """
        if rule_chain_name is None:
            raise ValueError("Invalid value for `rule_chain_name`, must not be `None`")  # noqa: E501

        self._rule_chain_name = rule_chain_name

    @property
    def rule_node_name(self):
        """Gets the rule_node_name of this RuleChainOutputLabelsUsage.  # noqa: E501

        Rule Node Name  # noqa: E501

        :return: The rule_node_name of this RuleChainOutputLabelsUsage.  # noqa: E501
        :rtype: str
        """
        return self._rule_node_name

    @rule_node_name.setter
    def rule_node_name(self, rule_node_name):
        """Sets the rule_node_name of this RuleChainOutputLabelsUsage.

        Rule Node Name  # noqa: E501

        :param rule_node_name: The rule_node_name of this RuleChainOutputLabelsUsage.  # noqa: E501
        :type: str
        """
        if rule_node_name is None:
            raise ValueError("Invalid value for `rule_node_name`, must not be `None`")  # noqa: E501

        self._rule_node_name = rule_node_name

    @property
    def labels(self):
        """Gets the labels of this RuleChainOutputLabelsUsage.  # noqa: E501

        Output labels  # noqa: E501

        :return: The labels of this RuleChainOutputLabelsUsage.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this RuleChainOutputLabelsUsage.

        Output labels  # noqa: E501

        :param labels: The labels of this RuleChainOutputLabelsUsage.  # noqa: E501
        :type: list[str]
        """
        if labels is None:
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

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
        if issubclass(RuleChainOutputLabelsUsage, dict):
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
        if not isinstance(other, RuleChainOutputLabelsUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
