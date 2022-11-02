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

class WidgetsBundle(object):
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
        'external_id': 'WidgetsBundleId',
        'id': 'WidgetsBundleId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'alias': 'str',
        'title': 'str',
        'image': 'str',
        'description': 'str'
    }

    attribute_map = {
        'external_id': 'externalId',
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'alias': 'alias',
        'title': 'title',
        'image': 'image',
        'description': 'description'
    }

    def __init__(self, external_id=None, id=None, created_time=None, tenant_id=None, alias=None, title=None, image=None, description=None):  # noqa: E501
        """WidgetsBundle - a model defined in Swagger"""  # noqa: E501
        self._external_id = None
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._alias = None
        self._title = None
        self._image = None
        self._description = None
        self.discriminator = None
        if external_id is not None:
            self.external_id = external_id
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if alias is not None:
            self.alias = alias
        if title is not None:
            self.title = title
        if image is not None:
            self.image = image
        if description is not None:
            self.description = description

    @property
    def external_id(self):
        """Gets the external_id of this WidgetsBundle.  # noqa: E501


        :return: The external_id of this WidgetsBundle.  # noqa: E501
        :rtype: WidgetsBundleId
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this WidgetsBundle.


        :param external_id: The external_id of this WidgetsBundle.  # noqa: E501
        :type: WidgetsBundleId
        """

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this WidgetsBundle.  # noqa: E501


        :return: The id of this WidgetsBundle.  # noqa: E501
        :rtype: WidgetsBundleId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WidgetsBundle.


        :param id: The id of this WidgetsBundle.  # noqa: E501
        :type: WidgetsBundleId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this WidgetsBundle.  # noqa: E501

        Timestamp of the Widget Bundle creation, in milliseconds  # noqa: E501

        :return: The created_time of this WidgetsBundle.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this WidgetsBundle.

        Timestamp of the Widget Bundle creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this WidgetsBundle.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this WidgetsBundle.  # noqa: E501


        :return: The tenant_id of this WidgetsBundle.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this WidgetsBundle.


        :param tenant_id: The tenant_id of this WidgetsBundle.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def alias(self):
        """Gets the alias of this WidgetsBundle.  # noqa: E501

        Unique alias that is used in widget types as a reference widget bundle  # noqa: E501

        :return: The alias of this WidgetsBundle.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this WidgetsBundle.

        Unique alias that is used in widget types as a reference widget bundle  # noqa: E501

        :param alias: The alias of this WidgetsBundle.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def title(self):
        """Gets the title of this WidgetsBundle.  # noqa: E501

        Title used in search and UI  # noqa: E501

        :return: The title of this WidgetsBundle.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WidgetsBundle.

        Title used in search and UI  # noqa: E501

        :param title: The title of this WidgetsBundle.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def image(self):
        """Gets the image of this WidgetsBundle.  # noqa: E501

        Base64 encoded thumbnail  # noqa: E501

        :return: The image of this WidgetsBundle.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this WidgetsBundle.

        Base64 encoded thumbnail  # noqa: E501

        :param image: The image of this WidgetsBundle.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def description(self):
        """Gets the description of this WidgetsBundle.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this WidgetsBundle.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WidgetsBundle.

        Description  # noqa: E501

        :param description: The description of this WidgetsBundle.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(WidgetsBundle, dict):
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
        if not isinstance(other, WidgetsBundle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other