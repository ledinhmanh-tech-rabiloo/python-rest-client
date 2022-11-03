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

class EntityTypeVersionCreateConfig(object):
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
        'all_entities': 'bool',
        'entity_ids': 'list[str]',
        'save_attributes': 'bool',
        'save_credentials': 'bool',
        'save_relations': 'bool',
        'sync_strategy': 'str'
    }

    attribute_map = {
        'all_entities': 'allEntities',
        'entity_ids': 'entityIds',
        'save_attributes': 'saveAttributes',
        'save_credentials': 'saveCredentials',
        'save_relations': 'saveRelations',
        'sync_strategy': 'syncStrategy'
    }

    def __init__(self, all_entities=None, entity_ids=None, save_attributes=None, save_credentials=None, save_relations=None, sync_strategy=None):  # noqa: E501
        """EntityTypeVersionCreateConfig - a model defined in Swagger"""  # noqa: E501
        self._all_entities = None
        self._entity_ids = None
        self._save_attributes = None
        self._save_credentials = None
        self._save_relations = None
        self._sync_strategy = None
        self.discriminator = None
        if all_entities is not None:
            self.all_entities = all_entities
        if entity_ids is not None:
            self.entity_ids = entity_ids
        if save_attributes is not None:
            self.save_attributes = save_attributes
        if save_credentials is not None:
            self.save_credentials = save_credentials
        if save_relations is not None:
            self.save_relations = save_relations
        if sync_strategy is not None:
            self.sync_strategy = sync_strategy

    @property
    def all_entities(self):
        """Gets the all_entities of this EntityTypeVersionCreateConfig.  # noqa: E501


        :return: The all_entities of this EntityTypeVersionCreateConfig.  # noqa: E501
        :rtype: bool
        """
        return self._all_entities

    @all_entities.setter
    def all_entities(self, all_entities):
        """Sets the all_entities of this EntityTypeVersionCreateConfig.


        :param all_entities: The all_entities of this EntityTypeVersionCreateConfig.  # noqa: E501
        :type: bool
        """

        self._all_entities = all_entities

    @property
    def entity_ids(self):
        """Gets the entity_ids of this EntityTypeVersionCreateConfig.  # noqa: E501


        :return: The entity_ids of this EntityTypeVersionCreateConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._entity_ids

    @entity_ids.setter
    def entity_ids(self, entity_ids):
        """Sets the entity_ids of this EntityTypeVersionCreateConfig.


        :param entity_ids: The entity_ids of this EntityTypeVersionCreateConfig.  # noqa: E501
        :type: list[str]
        """

        self._entity_ids = entity_ids

    @property
    def save_attributes(self):
        """Gets the save_attributes of this EntityTypeVersionCreateConfig.  # noqa: E501


        :return: The save_attributes of this EntityTypeVersionCreateConfig.  # noqa: E501
        :rtype: bool
        """
        return self._save_attributes

    @save_attributes.setter
    def save_attributes(self, save_attributes):
        """Sets the save_attributes of this EntityTypeVersionCreateConfig.


        :param save_attributes: The save_attributes of this EntityTypeVersionCreateConfig.  # noqa: E501
        :type: bool
        """

        self._save_attributes = save_attributes

    @property
    def save_credentials(self):
        """Gets the save_credentials of this EntityTypeVersionCreateConfig.  # noqa: E501


        :return: The save_credentials of this EntityTypeVersionCreateConfig.  # noqa: E501
        :rtype: bool
        """
        return self._save_credentials

    @save_credentials.setter
    def save_credentials(self, save_credentials):
        """Sets the save_credentials of this EntityTypeVersionCreateConfig.


        :param save_credentials: The save_credentials of this EntityTypeVersionCreateConfig.  # noqa: E501
        :type: bool
        """

        self._save_credentials = save_credentials

    @property
    def save_relations(self):
        """Gets the save_relations of this EntityTypeVersionCreateConfig.  # noqa: E501


        :return: The save_relations of this EntityTypeVersionCreateConfig.  # noqa: E501
        :rtype: bool
        """
        return self._save_relations

    @save_relations.setter
    def save_relations(self, save_relations):
        """Sets the save_relations of this EntityTypeVersionCreateConfig.


        :param save_relations: The save_relations of this EntityTypeVersionCreateConfig.  # noqa: E501
        :type: bool
        """

        self._save_relations = save_relations

    @property
    def sync_strategy(self):
        """Gets the sync_strategy of this EntityTypeVersionCreateConfig.  # noqa: E501


        :return: The sync_strategy of this EntityTypeVersionCreateConfig.  # noqa: E501
        :rtype: str
        """
        return self._sync_strategy

    @sync_strategy.setter
    def sync_strategy(self, sync_strategy):
        """Sets the sync_strategy of this EntityTypeVersionCreateConfig.


        :param sync_strategy: The sync_strategy of this EntityTypeVersionCreateConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["MERGE", "OVERWRITE"]  # noqa: E501
        if sync_strategy not in allowed_values:
            raise ValueError(
                "Invalid value for `sync_strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(sync_strategy, allowed_values)
            )

        self._sync_strategy = sync_strategy

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
        if issubclass(EntityTypeVersionCreateConfig, dict):
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
        if not isinstance(other, EntityTypeVersionCreateConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
