# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._authorization_management_client_enums import *


class ErrorDefinition(msrest.serialization.Model):
    """Error description and code explaining why an operation failed.

    :param error: Error of the list gateway status.
    :type error: ~azure.mgmt.authorization.v2021_01_01_preview.models.ErrorDefinitionProperties
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinitionProperties'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDefinitionProperties"] = None,
        **kwargs
    ):
        super(ErrorDefinition, self).__init__(**kwargs)
        self.error = error


class ErrorDefinitionProperties(msrest.serialization.Model):
    """Error description and code explaining why an operation failed.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar message: Description of the error.
    :vartype message: str
    :param code: Error code of list gateway.
    :type code: str
    """

    _validation = {
        'message': {'readonly': True},
    }

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        **kwargs
    ):
        super(ErrorDefinitionProperties, self).__init__(**kwargs)
        self.message = None
        self.code = code


class Operation(msrest.serialization.Model):
    """The definition of a Microsoft.Authorization operation.

    :param name: Name of the operation.
    :type name: str
    :param is_data_action: Indicates whether the operation is a data action.
    :type is_data_action: bool
    :param display: Display of the operation.
    :type display: ~azure.mgmt.authorization.v2021_01_01_preview.models.OperationDisplay
    :param origin: Origin of the operation. Values include user|system|user,system.
    :type origin: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        is_data_action: Optional[bool] = None,
        display: Optional["OperationDisplay"] = None,
        origin: Optional[str] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.is_data_action = is_data_action
        self.display = display
        self.origin = origin


class OperationDisplay(msrest.serialization.Model):
    """The display information for a Microsoft.Authorization operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: The resource provider name: Microsoft.Authorization.
    :vartype provider: str
    :ivar resource: The resource on which the operation is performed.
    :vartype resource: str
    :ivar operation: The operation that users can perform.
    :vartype operation: str
    :ivar description: The description for the operation.
    :vartype description: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class OperationListResult(msrest.serialization.Model):
    """The result of a request to list Microsoft.Authorization operations.

    :param value: The collection value.
    :type value: list[~azure.mgmt.authorization.v2021_01_01_preview.models.Operation]
    :param next_link: The URI that can be used to request the next set of paged results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Operation"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class RoleAssignmentApproval(msrest.serialization.Model):
    """Role Assignment Approval.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The role assignment approval id.
    :vartype id: str
    :ivar name: The role assignment approval unique id.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param stages: This is the collection of stages returned when one does an expand on it.
    :type stages:
     list[~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStep]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'stages': {'key': 'properties.stages', 'type': '[RoleAssignmentApprovalStep]'},
    }

    def __init__(
        self,
        *,
        stages: Optional[List["RoleAssignmentApprovalStep"]] = None,
        **kwargs
    ):
        super(RoleAssignmentApproval, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.stages = stages


class RoleAssignmentApprovalListResult(msrest.serialization.Model):
    """List of role assignment approvals.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: Role Assignment Approval list.
    :type value: list[~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApproval]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[RoleAssignmentApproval]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["RoleAssignmentApproval"]] = None,
        **kwargs
    ):
        super(RoleAssignmentApprovalListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = None


class RoleAssignmentApprovalStep(msrest.serialization.Model):
    """Role assignment approval stage properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The role assignment approval stage id.
    :vartype id: str
    :ivar name: The role assignment approval stage name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param display_name: The display name for the approval stage.
    :type display_name: str
    :ivar status: This read-only field specifies the status of an approval. Possible values
     include: "NotStarted", "InProgress", "Completed", "Expired", "Initializing", "Escalating",
     "Completing", "Escalated".
    :vartype status: str or
     ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStepStatus
    :ivar assigned_to_me: Indicates whether the stage is assigned to me for review.
    :vartype assigned_to_me: bool
    :ivar reviewed_date_time: Date Time when a decision was taken.
    :vartype reviewed_date_time: ~datetime.datetime
    :param review_result: The decision on the approval stage. This value is initially set to
     NotReviewed. Approvers can take action of Approve/Deny. Possible values include: "Approve",
     "Deny", "NotReviewed".
    :type review_result: str or
     ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStepReviewResult
    :param justification: Justification provided by approvers for their action.
    :type justification: str
    :ivar principal_id: The identity id.
    :vartype principal_id: str
    :ivar principal_type: The identity type : user/servicePrincipal. Possible values include:
     "user", "servicePrincipal".
    :vartype principal_type: str or
     ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalActorIdentityType
    :ivar principal_name: The identity display name.
    :vartype principal_name: str
    :ivar user_principal_name: The user principal name(if valid).
    :vartype user_principal_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'status': {'readonly': True},
        'assigned_to_me': {'readonly': True},
        'reviewed_date_time': {'readonly': True},
        'principal_id': {'readonly': True},
        'principal_type': {'readonly': True},
        'principal_name': {'readonly': True},
        'user_principal_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'assigned_to_me': {'key': 'properties.assignedToMe', 'type': 'bool'},
        'reviewed_date_time': {'key': 'properties.reviewedDateTime', 'type': 'iso-8601'},
        'review_result': {'key': 'properties.reviewResult', 'type': 'str'},
        'justification': {'key': 'properties.justification', 'type': 'str'},
        'principal_id': {'key': 'properties.reviewedBy.principalId', 'type': 'str'},
        'principal_type': {'key': 'properties.reviewedBy.principalType', 'type': 'str'},
        'principal_name': {'key': 'properties.reviewedBy.principalName', 'type': 'str'},
        'user_principal_name': {'key': 'properties.reviewedBy.userPrincipalName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        display_name: Optional[str] = None,
        review_result: Optional[Union[str, "RoleAssignmentApprovalStepReviewResult"]] = None,
        justification: Optional[str] = None,
        **kwargs
    ):
        super(RoleAssignmentApprovalStep, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.display_name = display_name
        self.status = None
        self.assigned_to_me = None
        self.reviewed_date_time = None
        self.review_result = review_result
        self.justification = justification
        self.principal_id = None
        self.principal_type = None
        self.principal_name = None
        self.user_principal_name = None


class RoleAssignmentApprovalStepListResult(msrest.serialization.Model):
    """List of role assignment approval stage list.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: Role Assignment Approval Step list.
    :type value:
     list[~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStep]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[RoleAssignmentApprovalStep]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["RoleAssignmentApprovalStep"]] = None,
        **kwargs
    ):
        super(RoleAssignmentApprovalStepListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = None


class RoleAssignmentApprovalStepProperties(msrest.serialization.Model):
    """Approval Step.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param display_name: The display name for the approval stage.
    :type display_name: str
    :ivar status: This read-only field specifies the status of an approval. Possible values
     include: "NotStarted", "InProgress", "Completed", "Expired", "Initializing", "Escalating",
     "Completing", "Escalated".
    :vartype status: str or
     ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStepStatus
    :ivar assigned_to_me: Indicates whether the stage is assigned to me for review.
    :vartype assigned_to_me: bool
    :ivar reviewed_date_time: Date Time when a decision was taken.
    :vartype reviewed_date_time: ~datetime.datetime
    :param review_result: The decision on the approval stage. This value is initially set to
     NotReviewed. Approvers can take action of Approve/Deny. Possible values include: "Approve",
     "Deny", "NotReviewed".
    :type review_result: str or
     ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStepReviewResult
    :param justification: Justification provided by approvers for their action.
    :type justification: str
    :ivar principal_id: The identity id.
    :vartype principal_id: str
    :ivar principal_type: The identity type : user/servicePrincipal. Possible values include:
     "user", "servicePrincipal".
    :vartype principal_type: str or
     ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalActorIdentityType
    :ivar principal_name: The identity display name.
    :vartype principal_name: str
    :ivar user_principal_name: The user principal name(if valid).
    :vartype user_principal_name: str
    """

    _validation = {
        'status': {'readonly': True},
        'assigned_to_me': {'readonly': True},
        'reviewed_date_time': {'readonly': True},
        'principal_id': {'readonly': True},
        'principal_type': {'readonly': True},
        'principal_name': {'readonly': True},
        'user_principal_name': {'readonly': True},
    }

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'assigned_to_me': {'key': 'assignedToMe', 'type': 'bool'},
        'reviewed_date_time': {'key': 'reviewedDateTime', 'type': 'iso-8601'},
        'review_result': {'key': 'reviewResult', 'type': 'str'},
        'justification': {'key': 'justification', 'type': 'str'},
        'principal_id': {'key': 'reviewedBy.principalId', 'type': 'str'},
        'principal_type': {'key': 'reviewedBy.principalType', 'type': 'str'},
        'principal_name': {'key': 'reviewedBy.principalName', 'type': 'str'},
        'user_principal_name': {'key': 'reviewedBy.userPrincipalName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        display_name: Optional[str] = None,
        review_result: Optional[Union[str, "RoleAssignmentApprovalStepReviewResult"]] = None,
        justification: Optional[str] = None,
        **kwargs
    ):
        super(RoleAssignmentApprovalStepProperties, self).__init__(**kwargs)
        self.display_name = display_name
        self.status = None
        self.assigned_to_me = None
        self.reviewed_date_time = None
        self.review_result = review_result
        self.justification = justification
        self.principal_id = None
        self.principal_type = None
        self.principal_name = None
        self.user_principal_name = None
