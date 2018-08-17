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


class SlotDifference(ProxyOnlyResource):
    """A setting difference between two deployment slots of an app.

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
    :ivar level: Level of the difference: Information, Warning or Error.
    :vartype level: str
    :ivar setting_type: The type of the setting: General, AppSetting or
     ConnectionString.
    :vartype setting_type: str
    :ivar diff_rule: Rule that describes how to process the setting difference
     during a slot swap.
    :vartype diff_rule: str
    :ivar setting_name: Name of the setting.
    :vartype setting_name: str
    :ivar value_in_current_slot: Value of the setting in the current slot.
    :vartype value_in_current_slot: str
    :ivar value_in_target_slot: Value of the setting in the target slot.
    :vartype value_in_target_slot: str
    :ivar description: Description of the setting difference.
    :vartype description: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'level': {'readonly': True},
        'setting_type': {'readonly': True},
        'diff_rule': {'readonly': True},
        'setting_name': {'readonly': True},
        'value_in_current_slot': {'readonly': True},
        'value_in_target_slot': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'level': {'key': 'properties.level', 'type': 'str'},
        'setting_type': {'key': 'properties.settingType', 'type': 'str'},
        'diff_rule': {'key': 'properties.diffRule', 'type': 'str'},
        'setting_name': {'key': 'properties.settingName', 'type': 'str'},
        'value_in_current_slot': {'key': 'properties.valueInCurrentSlot', 'type': 'str'},
        'value_in_target_slot': {'key': 'properties.valueInTargetSlot', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
    }

    def __init__(self, kind=None):
        super(SlotDifference, self).__init__(kind=kind)
        self.level = None
        self.setting_type = None
        self.diff_rule = None
        self.setting_name = None
        self.value_in_current_slot = None
        self.value_in_target_slot = None
        self.description = None
