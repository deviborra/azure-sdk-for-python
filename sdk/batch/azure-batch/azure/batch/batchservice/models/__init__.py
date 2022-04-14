# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import AccountListSupportedImagesResult
from ._models import AffinityInformation
from ._models import Application
from ._models import ApplicationListResult
from ._models import ApplicationPackageReference
from ._models import AuthenticationTokenSettings
from ._models import AutoPoolSpecification
from ._models import AutoScaleRun
from ._models import AutoScaleRunError
from ._models import AutoUserSpecification
from ._models import AzureBlobFileSystemConfiguration
from ._models import AzureFileShareConfiguration
from ._models import BatchError
from ._models import BatchErrorDetail
from ._models import BatchPoolIdentity
from ._models import CIFSMountConfiguration
from ._models import Certificate
from ._models import CertificateAddParameter
from ._models import CertificateListResult
from ._models import CertificateReference
from ._models import CloudServiceConfiguration
from ._models import ComputeNode
from ._models import ComputeNodeEndpointConfiguration
from ._models import ComputeNodeError
from ._models import ComputeNodeGetRemoteLoginSettingsResult
from ._models import ComputeNodeIdentityReference
from ._models import ComputeNodeInformation
from ._models import ComputeNodeListResult
from ._models import ComputeNodeUser
from ._models import ContainerConfiguration
from ._models import ContainerRegistry
from ._models import DataDisk
from ._models import DeleteCertificateError
from ._models import DiffDiskSettings
from ._models import DiskEncryptionConfiguration
from ._models import EnvironmentSetting
from ._models import ErrorMessage
from ._models import ExitCodeMapping
from ._models import ExitCodeRangeMapping
from ._models import ExitConditions
from ._models import ExitOptions
from ._models import FileProperties
from ._models import HttpHeader
from ._models import ImageInformation
from ._models import ImageReference
from ._models import InboundEndpoint
from ._models import InboundNATPool
from ._models import InstanceViewStatus
from ._models import Job
from ._models import JobConstraints
from ._models import JobDisableParameter
from ._models import JobExecutionInformation
from ._models import JobListPreparationAndReleaseTaskStatusResult
from ._models import JobListResult
from ._models import JobManagerTask
from ._models import JobNetworkConfiguration
from ._models import JobPreparationAndReleaseTaskExecutionInformation
from ._models import JobPreparationTask
from ._models import JobPreparationTaskExecutionInformation
from ._models import JobReleaseTask
from ._models import JobReleaseTaskExecutionInformation
from ._models import JobSchedule
from ._models import JobScheduleExecutionInformation
from ._models import JobScheduleListResult
from ._models import JobScheduleStatistics
from ._models import JobScheduleUpdate
from ._models import JobSchedulingError
from ._models import JobSpecification
from ._models import JobStatistics
from ._models import JobTerminateParameter
from ._models import JobUpdate
from ._models import LinuxUserConfiguration
from ._models import MetadataItem
from ._models import MountConfiguration
from ._models import MultiInstanceSettings
from ._models import NFSMountConfiguration
from ._models import NameValuePair
from ._models import NetworkConfiguration
from ._models import NetworkSecurityGroupRule
from ._models import NodeAgentInformation
from ._models import NodeCounts
from ._models import NodeDisableSchedulingParameter
from ._models import NodeFile
from ._models import NodeFileListResult
from ._models import NodePlacementConfiguration
from ._models import NodeRebootParameter
from ._models import NodeReimageParameter
from ._models import NodeRemoveParameter
from ._models import NodeUpdateUserParameter
from ._models import NodeVMExtension
from ._models import NodeVMExtensionList
from ._models import OSDisk
from ._models import OutputFile
from ._models import OutputFileBlobContainerDestination
from ._models import OutputFileDestination
from ._models import OutputFileUploadOptions
from ._models import Pool
from ._models import PoolEnableAutoScaleParameter
from ._models import PoolEndpointConfiguration
from ._models import PoolEvaluateAutoScaleParameter
from ._models import PoolInformation
from ._models import PoolListResult
from ._models import PoolListUsageMetricsResult
from ._models import PoolNodeCounts
from ._models import PoolNodeCountsListResult
from ._models import PoolResizeParameter
from ._models import PoolSpecification
from ._models import PoolStatistics
from ._models import PoolUpdate
from ._models import PoolUsageMetrics
from ._models import PublicIPAddressConfiguration
from ._models import RecentJob
from ._models import ResizeError
from ._models import ResourceFile
from ._models import ResourceStatistics
from ._models import Schedule
from ._models import StartTask
from ._models import StartTaskInformation
from ._models import SubtaskInformation
from ._models import Task
from ._models import TaskAddCollectionParameter
from ._models import TaskAddCollectionResult
from ._models import TaskAddResult
from ._models import TaskConstraints
from ._models import TaskContainerExecutionInformation
from ._models import TaskContainerSettings
from ._models import TaskCounts
from ._models import TaskCountsResult
from ._models import TaskDependencies
from ._models import TaskExecutionInformation
from ._models import TaskFailureInformation
from ._models import TaskIdRange
from ._models import TaskInformation
from ._models import TaskListResult
from ._models import TaskListSubtasksResult
from ._models import TaskSchedulingPolicy
from ._models import TaskSlotCounts
from ._models import TaskStatistics
from ._models import UploadBatchServiceLogsConfiguration
from ._models import UploadBatchServiceLogsResult
from ._models import UsageStatistics
from ._models import UserAccount
from ._models import UserAssignedIdentity
from ._models import UserIdentity
from ._models import VMExtension
from ._models import VMExtensionInstanceView
from ._models import VirtualMachineConfiguration
from ._models import VirtualMachineInfo
from ._models import WindowsConfiguration
from ._models import WindowsUserConfiguration


from ._enums import (
    AllocationState,
    AutoUserScope,
    CachingType,
    CertificateFormat,
    CertificateState,
    CertificateStoreLocation,
    CertificateVisibility,
    ComputeNodeDeallocationOption,
    ComputeNodeFillType,
    ComputeNodeRebootOption,
    ComputeNodeReimageOption,
    ComputeNodeState,
    ContainerWorkingDirectory,
    DependencyAction,
    DisableComputeNodeSchedulingOption,
    DisableJobOption,
    DiskEncryptionTarget,
    DynamicVNetAssignmentScope,
    ElevationLevel,
    ErrorCategory,
    IPAddressProvisioningType,
    InboundEndpointProtocol,
    JobAction,
    JobPreparationTaskState,
    JobReleaseTaskState,
    JobScheduleState,
    JobState,
    LoginMode,
    NetworkSecurityGroupRuleAccess,
    NodePlacementPolicyType,
    OSType,
    OnAllTasksComplete,
    OnTaskFailure,
    OutputFileUploadCondition,
    PoolIdentityType,
    PoolLifetimeOption,
    PoolState,
    SchedulingState,
    StartTaskState,
    StatusLevelTypes,
    StorageAccountType,
    SubtaskState,
    TaskAddStatus,
    TaskExecutionResult,
    TaskState,
    VerificationType,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AccountListSupportedImagesResult',
    'AffinityInformation',
    'Application',
    'ApplicationListResult',
    'ApplicationPackageReference',
    'AuthenticationTokenSettings',
    'AutoPoolSpecification',
    'AutoScaleRun',
    'AutoScaleRunError',
    'AutoUserSpecification',
    'AzureBlobFileSystemConfiguration',
    'AzureFileShareConfiguration',
    'BatchError',
    'BatchErrorDetail',
    'BatchPoolIdentity',
    'CIFSMountConfiguration',
    'Certificate',
    'CertificateAddParameter',
    'CertificateListResult',
    'CertificateReference',
    'CloudServiceConfiguration',
    'ComputeNode',
    'ComputeNodeEndpointConfiguration',
    'ComputeNodeError',
    'ComputeNodeGetRemoteLoginSettingsResult',
    'ComputeNodeIdentityReference',
    'ComputeNodeInformation',
    'ComputeNodeListResult',
    'ComputeNodeUser',
    'ContainerConfiguration',
    'ContainerRegistry',
    'DataDisk',
    'DeleteCertificateError',
    'DiffDiskSettings',
    'DiskEncryptionConfiguration',
    'EnvironmentSetting',
    'ErrorMessage',
    'ExitCodeMapping',
    'ExitCodeRangeMapping',
    'ExitConditions',
    'ExitOptions',
    'FileProperties',
    'HttpHeader',
    'ImageInformation',
    'ImageReference',
    'InboundEndpoint',
    'InboundNATPool',
    'InstanceViewStatus',
    'Job',
    'JobConstraints',
    'JobDisableParameter',
    'JobExecutionInformation',
    'JobListPreparationAndReleaseTaskStatusResult',
    'JobListResult',
    'JobManagerTask',
    'JobNetworkConfiguration',
    'JobPreparationAndReleaseTaskExecutionInformation',
    'JobPreparationTask',
    'JobPreparationTaskExecutionInformation',
    'JobReleaseTask',
    'JobReleaseTaskExecutionInformation',
    'JobSchedule',
    'JobScheduleExecutionInformation',
    'JobScheduleListResult',
    'JobScheduleStatistics',
    'JobScheduleUpdate',
    'JobSchedulingError',
    'JobSpecification',
    'JobStatistics',
    'JobTerminateParameter',
    'JobUpdate',
    'LinuxUserConfiguration',
    'MetadataItem',
    'MountConfiguration',
    'MultiInstanceSettings',
    'NFSMountConfiguration',
    'NameValuePair',
    'NetworkConfiguration',
    'NetworkSecurityGroupRule',
    'NodeAgentInformation',
    'NodeCounts',
    'NodeDisableSchedulingParameter',
    'NodeFile',
    'NodeFileListResult',
    'NodePlacementConfiguration',
    'NodeRebootParameter',
    'NodeReimageParameter',
    'NodeRemoveParameter',
    'NodeUpdateUserParameter',
    'NodeVMExtension',
    'NodeVMExtensionList',
    'OSDisk',
    'OutputFile',
    'OutputFileBlobContainerDestination',
    'OutputFileDestination',
    'OutputFileUploadOptions',
    'Pool',
    'PoolEnableAutoScaleParameter',
    'PoolEndpointConfiguration',
    'PoolEvaluateAutoScaleParameter',
    'PoolInformation',
    'PoolListResult',
    'PoolListUsageMetricsResult',
    'PoolNodeCounts',
    'PoolNodeCountsListResult',
    'PoolResizeParameter',
    'PoolSpecification',
    'PoolStatistics',
    'PoolUpdate',
    'PoolUsageMetrics',
    'PublicIPAddressConfiguration',
    'RecentJob',
    'ResizeError',
    'ResourceFile',
    'ResourceStatistics',
    'Schedule',
    'StartTask',
    'StartTaskInformation',
    'SubtaskInformation',
    'Task',
    'TaskAddCollectionParameter',
    'TaskAddCollectionResult',
    'TaskAddResult',
    'TaskConstraints',
    'TaskContainerExecutionInformation',
    'TaskContainerSettings',
    'TaskCounts',
    'TaskCountsResult',
    'TaskDependencies',
    'TaskExecutionInformation',
    'TaskFailureInformation',
    'TaskIdRange',
    'TaskInformation',
    'TaskListResult',
    'TaskListSubtasksResult',
    'TaskSchedulingPolicy',
    'TaskSlotCounts',
    'TaskStatistics',
    'UploadBatchServiceLogsConfiguration',
    'UploadBatchServiceLogsResult',
    'UsageStatistics',
    'UserAccount',
    'UserAssignedIdentity',
    'UserIdentity',
    'VMExtension',
    'VMExtensionInstanceView',
    'VirtualMachineConfiguration',
    'VirtualMachineInfo',
    'WindowsConfiguration',
    'WindowsUserConfiguration',
    'AllocationState',
    'AutoUserScope',
    'CachingType',
    'CertificateFormat',
    'CertificateState',
    'CertificateStoreLocation',
    'CertificateVisibility',
    'ComputeNodeDeallocationOption',
    'ComputeNodeFillType',
    'ComputeNodeRebootOption',
    'ComputeNodeReimageOption',
    'ComputeNodeState',
    'ContainerWorkingDirectory',
    'DependencyAction',
    'DisableComputeNodeSchedulingOption',
    'DisableJobOption',
    'DiskEncryptionTarget',
    'DynamicVNetAssignmentScope',
    'ElevationLevel',
    'ErrorCategory',
    'IPAddressProvisioningType',
    'InboundEndpointProtocol',
    'JobAction',
    'JobPreparationTaskState',
    'JobReleaseTaskState',
    'JobScheduleState',
    'JobState',
    'LoginMode',
    'NetworkSecurityGroupRuleAccess',
    'NodePlacementPolicyType',
    'OSType',
    'OnAllTasksComplete',
    'OnTaskFailure',
    'OutputFileUploadCondition',
    'PoolIdentityType',
    'PoolLifetimeOption',
    'PoolState',
    'SchedulingState',
    'StartTaskState',
    'StatusLevelTypes',
    'StorageAccountType',
    'SubtaskState',
    'TaskAddStatus',
    'TaskExecutionResult',
    'TaskState',
    'VerificationType',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()