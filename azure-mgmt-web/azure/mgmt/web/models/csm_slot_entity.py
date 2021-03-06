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

from msrest.serialization import Model


class CsmSlotEntity(Model):
    """Deployment slot parameters.

    All required parameters must be populated in order to send to Azure.

    :param target_slot: Required. Destination deployment slot during swap
     operation.
    :type target_slot: str
    :param preserve_vnet: Required. <code>true</code> to preserve Virtual
     Network to the slot during swap; otherwise, <code>false</code>.
    :type preserve_vnet: bool
    """

    _validation = {
        'target_slot': {'required': True},
        'preserve_vnet': {'required': True},
    }

    _attribute_map = {
        'target_slot': {'key': 'targetSlot', 'type': 'str'},
        'preserve_vnet': {'key': 'preserveVnet', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(CsmSlotEntity, self).__init__(**kwargs)
        self.target_slot = kwargs.get('target_slot', None)
        self.preserve_vnet = kwargs.get('preserve_vnet', None)
