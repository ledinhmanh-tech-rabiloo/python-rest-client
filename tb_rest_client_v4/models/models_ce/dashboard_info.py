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

class DashboardInfo(object):
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
        'id': 'DashboardId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'name': 'str',
        'title': 'str',
        'assigned_customers': 'list[ShortCustomerInfo]',
        'mobile_hide': 'bool',
        'mobile_order': 'int',
        'image': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'name': 'name',
        'title': 'title',
        'assigned_customers': 'assignedCustomers',
        'mobile_hide': 'mobileHide',
        'mobile_order': 'mobileOrder',
        'image': 'image'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, name=None, title=None, assigned_customers=None, mobile_hide=None, mobile_order=None, image=None):  # noqa: E501
        """DashboardInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._name = None
        self._title = None
        self._assigned_customers = None
        self._mobile_hide = None
        self._mobile_order = None
        self._image = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if assigned_customers is not None:
            self.assigned_customers = assigned_customers
        if mobile_hide is not None:
            self.mobile_hide = mobile_hide
        if mobile_order is not None:
            self.mobile_order = mobile_order
        if image is not None:
            self.image = image

    @property
    def id(self):
        """Gets the id of this DashboardInfo.  # noqa: E501


        :return: The id of this DashboardInfo.  # noqa: E501
        :rtype: DashboardId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DashboardInfo.


        :param id: The id of this DashboardInfo.  # noqa: E501
        :type: DashboardId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this DashboardInfo.  # noqa: E501

        Timestamp of the dashboard creation, in milliseconds  # noqa: E501

        :return: The created_time of this DashboardInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this DashboardInfo.

        Timestamp of the dashboard creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this DashboardInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this DashboardInfo.  # noqa: E501


        :return: The tenant_id of this DashboardInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this DashboardInfo.


        :param tenant_id: The tenant_id of this DashboardInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this DashboardInfo.  # noqa: E501

        Same as title of the dashboard. Read-only field. Update the 'title' to change the 'name' of the dashboard.  # noqa: E501

        :return: The name of this DashboardInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DashboardInfo.

        Same as title of the dashboard. Read-only field. Update the 'title' to change the 'name' of the dashboard.  # noqa: E501

        :param name: The name of this DashboardInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def title(self):
        """Gets the title of this DashboardInfo.  # noqa: E501

        Title of the dashboard.  # noqa: E501

        :return: The title of this DashboardInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DashboardInfo.

        Title of the dashboard.  # noqa: E501

        :param title: The title of this DashboardInfo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def assigned_customers(self):
        """Gets the assigned_customers of this DashboardInfo.  # noqa: E501

        List of assigned customers with their info.  # noqa: E501

        :return: The assigned_customers of this DashboardInfo.  # noqa: E501
        :rtype: list[ShortCustomerInfo]
        """
        return self._assigned_customers

    @assigned_customers.setter
    def assigned_customers(self, assigned_customers):
        """Sets the assigned_customers of this DashboardInfo.

        List of assigned customers with their info.  # noqa: E501

        :param assigned_customers: The assigned_customers of this DashboardInfo.  # noqa: E501
        :type: list[ShortCustomerInfo]
        """

        self._assigned_customers = assigned_customers

    @property
    def mobile_hide(self):
        """Gets the mobile_hide of this DashboardInfo.  # noqa: E501

        Hide dashboard from mobile devices. Useful if the dashboard is not designed for small screens.  # noqa: E501

        :return: The mobile_hide of this DashboardInfo.  # noqa: E501
        :rtype: bool
        """
        return self._mobile_hide

    @mobile_hide.setter
    def mobile_hide(self, mobile_hide):
        """Sets the mobile_hide of this DashboardInfo.

        Hide dashboard from mobile devices. Useful if the dashboard is not designed for small screens.  # noqa: E501

        :param mobile_hide: The mobile_hide of this DashboardInfo.  # noqa: E501
        :type: bool
        """

        self._mobile_hide = mobile_hide

    @property
    def mobile_order(self):
        """Gets the mobile_order of this DashboardInfo.  # noqa: E501

        Order on mobile devices. Useful to adjust sorting of the dashboards for mobile applications  # noqa: E501

        :return: The mobile_order of this DashboardInfo.  # noqa: E501
        :rtype: int
        """
        return self._mobile_order

    @mobile_order.setter
    def mobile_order(self, mobile_order):
        """Sets the mobile_order of this DashboardInfo.

        Order on mobile devices. Useful to adjust sorting of the dashboards for mobile applications  # noqa: E501

        :param mobile_order: The mobile_order of this DashboardInfo.  # noqa: E501
        :type: int
        """

        self._mobile_order = mobile_order

    @property
    def image(self):
        """Gets the image of this DashboardInfo.  # noqa: E501

        Thumbnail picture for rendering of the dashboards in a grid view on mobile devices.  # noqa: E501

        :return: The image of this DashboardInfo.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this DashboardInfo.

        Thumbnail picture for rendering of the dashboards in a grid view on mobile devices.  # noqa: E501

        :param image: The image of this DashboardInfo.  # noqa: E501
        :type: str
        """

        self._image = image

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
        if issubclass(DashboardInfo, dict):
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
        if not isinstance(other, DashboardInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
