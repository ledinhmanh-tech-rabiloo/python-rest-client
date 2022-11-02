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

class MergedGroupPermissionInfo(object):
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
        'entity_type': 'str',
        'operations': 'list[str]'
    }

    attribute_map = {
        'entity_type': 'entityType',
        'operations': 'operations'
    }

    def __init__(self, entity_type=None, operations=None):  # noqa: E501
        """MergedGroupPermissionInfo - a model defined in Swagger"""  # noqa: E501
        self._entity_type = None
        self._operations = None
        self.discriminator = None
        if entity_type is not None:
            self.entity_type = entity_type
        if operations is not None:
            self.operations = operations

    @property
    def entity_type(self):
        """Gets the entity_type of this MergedGroupPermissionInfo.  # noqa: E501


        :return: The entity_type of this MergedGroupPermissionInfo.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this MergedGroupPermissionInfo.


        :param entity_type: The entity_type of this MergedGroupPermissionInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "API_USAGE_STATE", "ASSET", "BLOB_ENTITY", "CONVERTER", "CUSTOMER", "DASHBOARD", "DEVICE", "DEVICE_PROFILE", "EDGE", "ENTITY_GROUP", "ENTITY_VIEW", "GROUP_PERMISSION", "INTEGRATION", "OTA_PACKAGE", "QUEUE", "ROLE", "RPC", "RULE_CHAIN", "RULE_NODE", "SCHEDULER_EVENT", "TB_RESOURCE", "TENANT", "TENANT_PROFILE", "USER", "WIDGETS_BUNDLE", "WIDGET_TYPE"]  # noqa: E501
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def operations(self):
        """Gets the operations of this MergedGroupPermissionInfo.  # noqa: E501


        :return: The operations of this MergedGroupPermissionInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this MergedGroupPermissionInfo.


        :param operations: The operations of this MergedGroupPermissionInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ADD_TO_GROUP", "ALL", "ASSIGN_TO_TENANT", "CHANGE_OWNER", "CLAIM_DEVICES", "CREATE", "DELETE", "IMPERSONATE", "READ", "READ_ATTRIBUTES", "READ_CREDENTIALS", "READ_TELEMETRY", "REMOVE_FROM_GROUP", "RPC_CALL", "SHARE_GROUP", "WRITE", "WRITE_ATTRIBUTES", "WRITE_CREDENTIALS", "WRITE_TELEMETRY"]  # noqa: E501
        if not set(operations).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `operations` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(operations) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._operations = operations

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
        if issubclass(MergedGroupPermissionInfo, dict):
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
        if not isinstance(other, MergedGroupPermissionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other