# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CapabilitiesInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, action: str=None, version: str=None):  # noqa: E501
        """CapabilitiesInner - a model defined in Swagger

        :param action: The action of this CapabilitiesInner.  # noqa: E501
        :type action: str
        :param version: The version of this CapabilitiesInner.  # noqa: E501
        :type version: str
        """
        self.swagger_types = {
            'action': str,
            'version': str
        }

        self.attribute_map = {
            'action': 'action',
            'version': 'version'
        }
        self._action = action
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'CapabilitiesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The capabilities_inner of this CapabilitiesInner.  # noqa: E501
        :rtype: CapabilitiesInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action(self) -> str:
        """Gets the action of this CapabilitiesInner.


        :return: The action of this CapabilitiesInner.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action: str):
        """Sets the action of this CapabilitiesInner.


        :param action: The action of this CapabilitiesInner.
        :type action: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def version(self) -> str:
        """Gets the version of this CapabilitiesInner.


        :return: The version of this CapabilitiesInner.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this CapabilitiesInner.


        :param version: The version of this CapabilitiesInner.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version
