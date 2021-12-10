# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.19.15
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1ServerAddressByClientCIDR(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'client_cidr': 'str',
        'server_address': 'str'
    }

    attribute_map = {
        'client_cidr': 'clientCIDR',
        'server_address': 'serverAddress'
    }

    def __init__(self, client_cidr=None, server_address=None, local_vars_configuration=None):  # noqa: E501
        """V1ServerAddressByClientCIDR - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_cidr = None
        self._server_address = None
        self.discriminator = None

        self.client_cidr = client_cidr
        self.server_address = server_address

    @property
    def client_cidr(self):
        """Gets the client_cidr of this V1ServerAddressByClientCIDR.  # noqa: E501

        The CIDR with which clients can match their IP to figure out the server address that they should use.  # noqa: E501

        :return: The client_cidr of this V1ServerAddressByClientCIDR.  # noqa: E501
        :rtype: str
        """
        return self._client_cidr

    @client_cidr.setter
    def client_cidr(self, client_cidr):
        """Sets the client_cidr of this V1ServerAddressByClientCIDR.

        The CIDR with which clients can match their IP to figure out the server address that they should use.  # noqa: E501

        :param client_cidr: The client_cidr of this V1ServerAddressByClientCIDR.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and client_cidr is None:  # noqa: E501
            raise ValueError("Invalid value for `client_cidr`, must not be `None`")  # noqa: E501

        self._client_cidr = client_cidr

    @property
    def server_address(self):
        """Gets the server_address of this V1ServerAddressByClientCIDR.  # noqa: E501

        Address of this server, suitable for a client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port.  # noqa: E501

        :return: The server_address of this V1ServerAddressByClientCIDR.  # noqa: E501
        :rtype: str
        """
        return self._server_address

    @server_address.setter
    def server_address(self, server_address):
        """Sets the server_address of this V1ServerAddressByClientCIDR.

        Address of this server, suitable for a client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port.  # noqa: E501

        :param server_address: The server_address of this V1ServerAddressByClientCIDR.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and server_address is None:  # noqa: E501
            raise ValueError("Invalid value for `server_address`, must not be `None`")  # noqa: E501

        self._server_address = server_address

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ServerAddressByClientCIDR):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ServerAddressByClientCIDR):
            return True

        return self.to_dict() != other.to_dict()
