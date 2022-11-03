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

class CustomTimeScheduleItem(object):
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
        'day_of_week': 'int',
        'enabled': 'bool',
        'ends_on': 'int',
        'starts_on': 'int'
    }

    attribute_map = {
        'day_of_week': 'dayOfWeek',
        'enabled': 'enabled',
        'ends_on': 'endsOn',
        'starts_on': 'startsOn'
    }

    def __init__(self, day_of_week=None, enabled=None, ends_on=None, starts_on=None):  # noqa: E501
        """CustomTimeScheduleItem - a model defined in Swagger"""  # noqa: E501
        self._day_of_week = None
        self._enabled = None
        self._ends_on = None
        self._starts_on = None
        self.discriminator = None
        if day_of_week is not None:
            self.day_of_week = day_of_week
        if enabled is not None:
            self.enabled = enabled
        if ends_on is not None:
            self.ends_on = ends_on
        if starts_on is not None:
            self.starts_on = starts_on

    @property
    def day_of_week(self):
        """Gets the day_of_week of this CustomTimeScheduleItem.  # noqa: E501


        :return: The day_of_week of this CustomTimeScheduleItem.  # noqa: E501
        :rtype: int
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this CustomTimeScheduleItem.


        :param day_of_week: The day_of_week of this CustomTimeScheduleItem.  # noqa: E501
        :type: int
        """

        self._day_of_week = day_of_week

    @property
    def enabled(self):
        """Gets the enabled of this CustomTimeScheduleItem.  # noqa: E501


        :return: The enabled of this CustomTimeScheduleItem.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CustomTimeScheduleItem.


        :param enabled: The enabled of this CustomTimeScheduleItem.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def ends_on(self):
        """Gets the ends_on of this CustomTimeScheduleItem.  # noqa: E501


        :return: The ends_on of this CustomTimeScheduleItem.  # noqa: E501
        :rtype: int
        """
        return self._ends_on

    @ends_on.setter
    def ends_on(self, ends_on):
        """Sets the ends_on of this CustomTimeScheduleItem.


        :param ends_on: The ends_on of this CustomTimeScheduleItem.  # noqa: E501
        :type: int
        """

        self._ends_on = ends_on

    @property
    def starts_on(self):
        """Gets the starts_on of this CustomTimeScheduleItem.  # noqa: E501


        :return: The starts_on of this CustomTimeScheduleItem.  # noqa: E501
        :rtype: int
        """
        return self._starts_on

    @starts_on.setter
    def starts_on(self, starts_on):
        """Sets the starts_on of this CustomTimeScheduleItem.


        :param starts_on: The starts_on of this CustomTimeScheduleItem.  # noqa: E501
        :type: int
        """

        self._starts_on = starts_on

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
        if issubclass(CustomTimeScheduleItem, dict):
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
        if not isinstance(other, CustomTimeScheduleItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
