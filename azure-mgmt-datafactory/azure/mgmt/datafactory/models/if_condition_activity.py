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

from .control_activity import ControlActivity


class IfConditionActivity(ControlActivity):
    """This activity evaluates a boolean expression and executes either the
    activities under the ifTrueActivities property or the ifFalseActivities
    property depending on the result of the expression.

    :param name: Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list of :class:`ActivityDependency
     <azure.mgmt.datafactory.models.ActivityDependency>`
    :param type: Polymorphic Discriminator
    :type type: str
    :param expression: An expression that would evaluate to Boolean. This is
     used to determine the block of activities (ifTrueActivities or
     ifFalseActivities) that will be executed.
    :type expression: :class:`Expression
     <azure.mgmt.datafactory.models.Expression>`
    :param if_true_activities: List of activities to execute if expression is
     evaluated to true. This is an optional property and if not provided, the
     activity will exit without any action.
    :type if_true_activities: list of :class:`Activity
     <azure.mgmt.datafactory.models.Activity>`
    :param if_false_activities: List of activities to execute if expression is
     evaluated to false. This is an optional property and if not provided, the
     activity will exit without any action.
    :type if_false_activities: list of :class:`Activity
     <azure.mgmt.datafactory.models.Activity>`
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'expression': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'type': {'key': 'type', 'type': 'str'},
        'expression': {'key': 'typeProperties.expression', 'type': 'Expression'},
        'if_true_activities': {'key': 'typeProperties.ifTrueActivities', 'type': '[Activity]'},
        'if_false_activities': {'key': 'typeProperties.ifFalseActivities', 'type': '[Activity]'},
    }

    def __init__(self, name, expression, description=None, depends_on=None, if_true_activities=None, if_false_activities=None):
        super(IfConditionActivity, self).__init__(name=name, description=description, depends_on=depends_on)
        self.expression = expression
        self.if_true_activities = if_true_activities
        self.if_false_activities = if_false_activities
        self.type = 'IfCondition'