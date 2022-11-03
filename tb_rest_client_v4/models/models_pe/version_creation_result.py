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

class VersionCreationResult(object):
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
        'added': 'int',
        'done': 'bool',
        'error': 'str',
        'modified': 'int',
        'removed': 'int',
        'version': 'EntityVersion'
    }

    attribute_map = {
        'added': 'added',
        'done': 'done',
        'error': 'error',
        'modified': 'modified',
        'removed': 'removed',
        'version': 'version'
    }

    def __init__(self, added=None, done=None, error=None, modified=None, removed=None, version=None):  # noqa: E501
        """VersionCreationResult - a model defined in Swagger"""  # noqa: E501
        self._added = None
        self._done = None
        self._error = None
        self._modified = None
        self._removed = None
        self._version = None
        self.discriminator = None
        if added is not None:
            self.added = added
        if done is not None:
            self.done = done
        if error is not None:
            self.error = error
        if modified is not None:
            self.modified = modified
        if removed is not None:
            self.removed = removed
        if version is not None:
            self.version = version

    @property
    def added(self):
        """Gets the added of this VersionCreationResult.  # noqa: E501


        :return: The added of this VersionCreationResult.  # noqa: E501
        :rtype: int
        """
        return self._added

    @added.setter
    def added(self, added):
        """Sets the added of this VersionCreationResult.


        :param added: The added of this VersionCreationResult.  # noqa: E501
        :type: int
        """

        self._added = added

    @property
    def done(self):
        """Gets the done of this VersionCreationResult.  # noqa: E501


        :return: The done of this VersionCreationResult.  # noqa: E501
        :rtype: bool
        """
        return self._done

    @done.setter
    def done(self, done):
        """Sets the done of this VersionCreationResult.


        :param done: The done of this VersionCreationResult.  # noqa: E501
        :type: bool
        """

        self._done = done

    @property
    def error(self):
        """Gets the error of this VersionCreationResult.  # noqa: E501


        :return: The error of this VersionCreationResult.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this VersionCreationResult.


        :param error: The error of this VersionCreationResult.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def modified(self):
        """Gets the modified of this VersionCreationResult.  # noqa: E501


        :return: The modified of this VersionCreationResult.  # noqa: E501
        :rtype: int
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this VersionCreationResult.


        :param modified: The modified of this VersionCreationResult.  # noqa: E501
        :type: int
        """

        self._modified = modified

    @property
    def removed(self):
        """Gets the removed of this VersionCreationResult.  # noqa: E501


        :return: The removed of this VersionCreationResult.  # noqa: E501
        :rtype: int
        """
        return self._removed

    @removed.setter
    def removed(self, removed):
        """Sets the removed of this VersionCreationResult.


        :param removed: The removed of this VersionCreationResult.  # noqa: E501
        :type: int
        """

        self._removed = removed

    @property
    def version(self):
        """Gets the version of this VersionCreationResult.  # noqa: E501


        :return: The version of this VersionCreationResult.  # noqa: E501
        :rtype: EntityVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VersionCreationResult.


        :param version: The version of this VersionCreationResult.  # noqa: E501
        :type: EntityVersion
        """

        self._version = version

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
        if issubclass(VersionCreationResult, dict):
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
        if not isinstance(other, VersionCreationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
