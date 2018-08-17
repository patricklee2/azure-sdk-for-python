# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_only_resource import ProxyOnlyResource


class BillingMeter(ProxyOnlyResource):
    """App Service billing entity that contains information about meter which the
    Azure billing system utilizes to charge users for services.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param meter_id: Meter GUID onboarded in Commerce
    :type meter_id: str
    :param billing_location: Azure Location of billable resource
    :type billing_location: str
    :param short_name: Short Name from App Service Azure pricing Page
    :type short_name: str
    :param friendly_name: Friendly name of the meter
    :type friendly_name: str
    :param resource_type: App Service ResourceType meter used for
    :type resource_type: str
    :param os_type: App Service OS type meter used for
    :type os_type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'meter_id': {'key': 'properties.meterId', 'type': 'str'},
        'billing_location': {'key': 'properties.billingLocation', 'type': 'str'},
        'short_name': {'key': 'properties.shortName', 'type': 'str'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'resource_type': {'key': 'properties.resourceType', 'type': 'str'},
        'os_type': {'key': 'properties.osType', 'type': 'str'},
    }

    def __init__(self, kind=None, meter_id=None, billing_location=None, short_name=None, friendly_name=None, resource_type=None, os_type=None):
        super(BillingMeter, self).__init__(kind=kind)
        self.meter_id = meter_id
        self.billing_location = billing_location
        self.short_name = short_name
        self.friendly_name = friendly_name
        self.resource_type = resource_type
        self.os_type = os_type
