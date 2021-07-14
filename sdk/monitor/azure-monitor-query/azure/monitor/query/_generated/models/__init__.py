# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import BatchQueryRequest
    from ._models_py3 import BatchQueryResponse
    from ._models_py3 import BatchQueryResults
    from ._models_py3 import BatchRequest
    from ._models_py3 import BatchResponse
    from ._models_py3 import Column
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorInfo
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ErrorResponseAutoGenerated
    from ._models_py3 import LocalizableString
    from ._models_py3 import MetadataApplication
    from ._models_py3 import MetadataApplicationRelated
    from ._models_py3 import MetadataCategory
    from ._models_py3 import MetadataCategoryRelated
    from ._models_py3 import MetadataFunction
    from ._models_py3 import MetadataFunctionRelated
    from ._models_py3 import MetadataPermissions
    from ._models_py3 import MetadataPermissionsApplicationsItem
    from ._models_py3 import MetadataPermissionsResourcesItem
    from ._models_py3 import MetadataPermissionsWorkspacesItem
    from ._models_py3 import MetadataQuery
    from ._models_py3 import MetadataQueryRelated
    from ._models_py3 import MetadataResourceType
    from ._models_py3 import MetadataResourceTypeRelated
    from ._models_py3 import MetadataResults
    from ._models_py3 import MetadataSolution
    from ._models_py3 import MetadataSolutionRelated
    from ._models_py3 import MetadataTable
    from ._models_py3 import MetadataTableColumnsItem
    from ._models_py3 import MetadataTableRelated
    from ._models_py3 import MetadataValue
    from ._models_py3 import MetadataWorkspace
    from ._models_py3 import MetadataWorkspaceRelated
    from ._models_py3 import Metric
    from ._models_py3 import MetricAvailability
    from ._models_py3 import MetricDefinition
    from ._models_py3 import MetricDefinitionCollection
    from ._models_py3 import MetricNamespace
    from ._models_py3 import MetricNamespaceCollection
    from ._models_py3 import MetricNamespaceName
    from ._models_py3 import MetricValue
    from ._models_py3 import QueryBody
    from ._models_py3 import QueryResults
    from ._models_py3 import Response
    from ._models_py3 import Table
    from ._models_py3 import TimeSeriesElement
except (SyntaxError, ImportError):
    from ._models import BatchQueryRequest  # type: ignore
    from ._models import BatchQueryResponse  # type: ignore
    from ._models import BatchQueryResults  # type: ignore
    from ._models import BatchRequest  # type: ignore
    from ._models import BatchResponse  # type: ignore
    from ._models import Column  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorInfo  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ErrorResponseAutoGenerated  # type: ignore
    from ._models import LocalizableString  # type: ignore
    from ._models import MetadataApplication  # type: ignore
    from ._models import MetadataApplicationRelated  # type: ignore
    from ._models import MetadataCategory  # type: ignore
    from ._models import MetadataCategoryRelated  # type: ignore
    from ._models import MetadataFunction  # type: ignore
    from ._models import MetadataFunctionRelated  # type: ignore
    from ._models import MetadataPermissions  # type: ignore
    from ._models import MetadataPermissionsApplicationsItem  # type: ignore
    from ._models import MetadataPermissionsResourcesItem  # type: ignore
    from ._models import MetadataPermissionsWorkspacesItem  # type: ignore
    from ._models import MetadataQuery  # type: ignore
    from ._models import MetadataQueryRelated  # type: ignore
    from ._models import MetadataResourceType  # type: ignore
    from ._models import MetadataResourceTypeRelated  # type: ignore
    from ._models import MetadataResults  # type: ignore
    from ._models import MetadataSolution  # type: ignore
    from ._models import MetadataSolutionRelated  # type: ignore
    from ._models import MetadataTable  # type: ignore
    from ._models import MetadataTableColumnsItem  # type: ignore
    from ._models import MetadataTableRelated  # type: ignore
    from ._models import MetadataValue  # type: ignore
    from ._models import MetadataWorkspace  # type: ignore
    from ._models import MetadataWorkspaceRelated  # type: ignore
    from ._models import Metric  # type: ignore
    from ._models import MetricAvailability  # type: ignore
    from ._models import MetricDefinition  # type: ignore
    from ._models import MetricDefinitionCollection  # type: ignore
    from ._models import MetricNamespace  # type: ignore
    from ._models import MetricNamespaceCollection  # type: ignore
    from ._models import MetricNamespaceName  # type: ignore
    from ._models import MetricValue  # type: ignore
    from ._models import QueryBody  # type: ignore
    from ._models import QueryResults  # type: ignore
    from ._models import Response  # type: ignore
    from ._models import Table  # type: ignore
    from ._models import TimeSeriesElement  # type: ignore

from ._monitor_query_client_enums import (
    AggregationType,
    LogsColumnType,
    MetadataColumnDataType,
    MetricClass,
    MetricUnit,
    NamespaceClassification,
    ResultType,
)

__all__ = [
    'BatchQueryRequest',
    'BatchQueryResponse',
    'BatchQueryResults',
    'BatchRequest',
    'BatchResponse',
    'Column',
    'ErrorDetail',
    'ErrorInfo',
    'ErrorResponse',
    'ErrorResponseAutoGenerated',
    'LocalizableString',
    'MetadataApplication',
    'MetadataApplicationRelated',
    'MetadataCategory',
    'MetadataCategoryRelated',
    'MetadataFunction',
    'MetadataFunctionRelated',
    'MetadataPermissions',
    'MetadataPermissionsApplicationsItem',
    'MetadataPermissionsResourcesItem',
    'MetadataPermissionsWorkspacesItem',
    'MetadataQuery',
    'MetadataQueryRelated',
    'MetadataResourceType',
    'MetadataResourceTypeRelated',
    'MetadataResults',
    'MetadataSolution',
    'MetadataSolutionRelated',
    'MetadataTable',
    'MetadataTableColumnsItem',
    'MetadataTableRelated',
    'MetadataValue',
    'MetadataWorkspace',
    'MetadataWorkspaceRelated',
    'Metric',
    'MetricAvailability',
    'MetricDefinition',
    'MetricDefinitionCollection',
    'MetricNamespace',
    'MetricNamespaceCollection',
    'MetricNamespaceName',
    'MetricValue',
    'QueryBody',
    'QueryResults',
    'Response',
    'Table',
    'TimeSeriesElement',
    'AggregationType',
    'LogsColumnType',
    'MetadataColumnDataType',
    'MetricClass',
    'MetricUnit',
    'NamespaceClassification',
    'ResultType',
]