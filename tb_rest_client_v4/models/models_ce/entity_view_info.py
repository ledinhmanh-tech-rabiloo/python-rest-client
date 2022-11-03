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

class EntityViewInfo(object):
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
        'external_id': 'EntityViewId',
        'id': 'EntityViewId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'name': 'str',
        'type': 'str',
        'entity_id': 'EntityId',
        'keys': 'TelemetryEntityView',
        'start_time_ms': 'int',
        'end_time_ms': 'int',
        'additional_info': 'JsonNode',
        'customer_title': 'str',
        'customer_is_public': 'bool'
    }

    attribute_map = {
        'external_id': 'externalId',
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'name': 'name',
        'type': 'type',
        'entity_id': 'entityId',
        'keys': 'keys',
        'start_time_ms': 'startTimeMs',
        'end_time_ms': 'endTimeMs',
        'additional_info': 'additionalInfo',
        'customer_title': 'customerTitle',
        'customer_is_public': 'customerIsPublic'
    }

    def __init__(self, external_id=None, id=None, created_time=None, tenant_id=None, customer_id=None, name=None, type=None, entity_id=None, keys=None, start_time_ms=None, end_time_ms=None, additional_info=None, customer_title=None, customer_is_public=None):  # noqa: E501
        """EntityViewInfo - a model defined in Swagger"""  # noqa: E501
        self._external_id = None
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._customer_id = None
        self._name = None
        self._type = None
        self._entity_id = None
        self._keys = None
        self._start_time_ms = None
        self._end_time_ms = None
        self._additional_info = None
        self._customer_title = None
        self._customer_is_public = None
        self.discriminator = None
        if external_id is not None:
            self.external_id = external_id
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        self.name = name
        self.type = type
        self.entity_id = entity_id
        self.keys = keys
        if start_time_ms is not None:
            self.start_time_ms = start_time_ms
        if end_time_ms is not None:
            self.end_time_ms = end_time_ms
        if additional_info is not None:
            self.additional_info = additional_info
        if customer_title is not None:
            self.customer_title = customer_title
        if customer_is_public is not None:
            self.customer_is_public = customer_is_public

    @property
    def external_id(self):
        """Gets the external_id of this EntityViewInfo.  # noqa: E501


        :return: The external_id of this EntityViewInfo.  # noqa: E501
        :rtype: EntityViewId
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this EntityViewInfo.


        :param external_id: The external_id of this EntityViewInfo.  # noqa: E501
        :type: EntityViewId
        """

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this EntityViewInfo.  # noqa: E501


        :return: The id of this EntityViewInfo.  # noqa: E501
        :rtype: EntityViewId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EntityViewInfo.


        :param id: The id of this EntityViewInfo.  # noqa: E501
        :type: EntityViewId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this EntityViewInfo.  # noqa: E501

        Timestamp of the Entity View creation, in milliseconds  # noqa: E501

        :return: The created_time of this EntityViewInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EntityViewInfo.

        Timestamp of the Entity View creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this EntityViewInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this EntityViewInfo.  # noqa: E501


        :return: The tenant_id of this EntityViewInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this EntityViewInfo.


        :param tenant_id: The tenant_id of this EntityViewInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this EntityViewInfo.  # noqa: E501


        :return: The customer_id of this EntityViewInfo.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this EntityViewInfo.


        :param customer_id: The customer_id of this EntityViewInfo.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def name(self):
        """Gets the name of this EntityViewInfo.  # noqa: E501

        Entity View name  # noqa: E501

        :return: The name of this EntityViewInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EntityViewInfo.

        Entity View name  # noqa: E501

        :param name: The name of this EntityViewInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this EntityViewInfo.  # noqa: E501

        Device Profile Name  # noqa: E501

        :return: The type of this EntityViewInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntityViewInfo.

        Device Profile Name  # noqa: E501

        :param type: The type of this EntityViewInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def entity_id(self):
        """Gets the entity_id of this EntityViewInfo.  # noqa: E501


        :return: The entity_id of this EntityViewInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this EntityViewInfo.


        :param entity_id: The entity_id of this EntityViewInfo.  # noqa: E501
        :type: EntityId
        """
        if entity_id is None:
            raise ValueError("Invalid value for `entity_id`, must not be `None`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def keys(self):
        """Gets the keys of this EntityViewInfo.  # noqa: E501


        :return: The keys of this EntityViewInfo.  # noqa: E501
        :rtype: TelemetryEntityView
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this EntityViewInfo.


        :param keys: The keys of this EntityViewInfo.  # noqa: E501
        :type: TelemetryEntityView
        """
        if keys is None:
            raise ValueError("Invalid value for `keys`, must not be `None`")  # noqa: E501

        self._keys = keys

    @property
    def start_time_ms(self):
        """Gets the start_time_ms of this EntityViewInfo.  # noqa: E501

        Represents the start time of the interval that is used to limit access to target device telemetry. Customer will not be able to see entity telemetry that is outside the specified interval;  # noqa: E501

        :return: The start_time_ms of this EntityViewInfo.  # noqa: E501
        :rtype: int
        """
        return self._start_time_ms

    @start_time_ms.setter
    def start_time_ms(self, start_time_ms):
        """Sets the start_time_ms of this EntityViewInfo.

        Represents the start time of the interval that is used to limit access to target device telemetry. Customer will not be able to see entity telemetry that is outside the specified interval;  # noqa: E501

        :param start_time_ms: The start_time_ms of this EntityViewInfo.  # noqa: E501
        :type: int
        """

        self._start_time_ms = start_time_ms

    @property
    def end_time_ms(self):
        """Gets the end_time_ms of this EntityViewInfo.  # noqa: E501

        Represents the end time of the interval that is used to limit access to target device telemetry. Customer will not be able to see entity telemetry that is outside the specified interval;  # noqa: E501

        :return: The end_time_ms of this EntityViewInfo.  # noqa: E501
        :rtype: int
        """
        return self._end_time_ms

    @end_time_ms.setter
    def end_time_ms(self, end_time_ms):
        """Sets the end_time_ms of this EntityViewInfo.

        Represents the end time of the interval that is used to limit access to target device telemetry. Customer will not be able to see entity telemetry that is outside the specified interval;  # noqa: E501

        :param end_time_ms: The end_time_ms of this EntityViewInfo.  # noqa: E501
        :type: int
        """

        self._end_time_ms = end_time_ms

    @property
    def additional_info(self):
        """Gets the additional_info of this EntityViewInfo.  # noqa: E501


        :return: The additional_info of this EntityViewInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this EntityViewInfo.


        :param additional_info: The additional_info of this EntityViewInfo.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def customer_title(self):
        """Gets the customer_title of this EntityViewInfo.  # noqa: E501

        Title of the Customer that owns the entity view.  # noqa: E501

        :return: The customer_title of this EntityViewInfo.  # noqa: E501
        :rtype: str
        """
        return self._customer_title

    @customer_title.setter
    def customer_title(self, customer_title):
        """Sets the customer_title of this EntityViewInfo.

        Title of the Customer that owns the entity view.  # noqa: E501

        :param customer_title: The customer_title of this EntityViewInfo.  # noqa: E501
        :type: str
        """

        self._customer_title = customer_title

    @property
    def customer_is_public(self):
        """Gets the customer_is_public of this EntityViewInfo.  # noqa: E501

        Indicates special 'Public' Customer that is auto-generated to use the entity view on public dashboards.  # noqa: E501

        :return: The customer_is_public of this EntityViewInfo.  # noqa: E501
        :rtype: bool
        """
        return self._customer_is_public

    @customer_is_public.setter
    def customer_is_public(self, customer_is_public):
        """Sets the customer_is_public of this EntityViewInfo.

        Indicates special 'Public' Customer that is auto-generated to use the entity view on public dashboards.  # noqa: E501

        :param customer_is_public: The customer_is_public of this EntityViewInfo.  # noqa: E501
        :type: bool
        """

        self._customer_is_public = customer_is_public

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
        if issubclass(EntityViewInfo, dict):
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
        if not isinstance(other, EntityViewInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
