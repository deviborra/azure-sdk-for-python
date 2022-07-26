# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_metrics_request(
    subscription_id: str,
    resource_group_name: str,
    account_name: str,
    database_rid: str,
    collection_rid: str,
    *,
    filter: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-05-15"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/metrics")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "accountName": _SERIALIZER.url("account_name", account_name, 'str', max_length=50, min_length=3, pattern=r'^[a-z0-9]+(-[a-z0-9]+)*'),
        "databaseRid": _SERIALIZER.url("database_rid", database_rid, 'str'),
        "collectionRid": _SERIALIZER.url("collection_rid", collection_rid, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    _params['$filter'] = _SERIALIZER.query("filter", filter, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_list_usages_request(
    subscription_id: str,
    resource_group_name: str,
    account_name: str,
    database_rid: str,
    collection_rid: str,
    *,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-05-15"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/usages")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "accountName": _SERIALIZER.url("account_name", account_name, 'str', max_length=50, min_length=3, pattern=r'^[a-z0-9]+(-[a-z0-9]+)*'),
        "databaseRid": _SERIALIZER.url("database_rid", database_rid, 'str'),
        "collectionRid": _SERIALIZER.url("collection_rid", collection_rid, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if filter is not None:
        _params['$filter'] = _SERIALIZER.query("filter", filter, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_list_metric_definitions_request(
    subscription_id: str,
    resource_group_name: str,
    account_name: str,
    database_rid: str,
    collection_rid: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-05-15"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/metricDefinitions")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "accountName": _SERIALIZER.url("account_name", account_name, 'str', max_length=50, min_length=3, pattern=r'^[a-z0-9]+(-[a-z0-9]+)*'),
        "databaseRid": _SERIALIZER.url("database_rid", database_rid, 'str'),
        "collectionRid": _SERIALIZER.url("collection_rid", collection_rid, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )

class CollectionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.cosmosdb.CosmosDBManagementClient`'s
        :attr:`collection` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def list_metrics(
        self,
        resource_group_name: str,
        account_name: str,
        database_rid: str,
        collection_rid: str,
        filter: str,
        **kwargs: Any
    ) -> Iterable[_models.MetricListResult]:
        """Retrieves the metrics determined by the given filter for the given database account and
        collection.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: Cosmos DB database account name.
        :type account_name: str
        :param database_rid: Cosmos DB database rid.
        :type database_rid: str
        :param collection_rid: Cosmos DB collection rid.
        :type collection_rid: str
        :param filter: An OData filter expression that describes a subset of metrics to return. The
         parameters that can be filtered are name.value (name of the metric, can have an or of multiple
         names), startTime, endTime, and timeGrain. The supported operator is eq.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either MetricListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.cosmosdb.models.MetricListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-05-15"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.MetricListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_metrics_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    database_rid=database_rid,
                    collection_rid=collection_rid,
                    api_version=api_version,
                    filter=filter,
                    template_url=self.list_metrics.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_metrics_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    database_rid=database_rid,
                    collection_rid=collection_rid,
                    api_version=api_version,
                    filter=filter,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("MetricListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_metrics.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/metrics"}  # type: ignore

    @distributed_trace
    def list_usages(
        self,
        resource_group_name: str,
        account_name: str,
        database_rid: str,
        collection_rid: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable[_models.UsagesResult]:
        """Retrieves the usages (most recent storage data) for the given collection.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: Cosmos DB database account name.
        :type account_name: str
        :param database_rid: Cosmos DB database rid.
        :type database_rid: str
        :param collection_rid: Cosmos DB collection rid.
        :type collection_rid: str
        :param filter: An OData filter expression that describes a subset of usages to return. The
         supported parameter is name.value (name of the metric, can have an or of multiple names).
         Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either UsagesResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.cosmosdb.models.UsagesResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-05-15"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.UsagesResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_usages_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    database_rid=database_rid,
                    collection_rid=collection_rid,
                    api_version=api_version,
                    filter=filter,
                    template_url=self.list_usages.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_usages_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    database_rid=database_rid,
                    collection_rid=collection_rid,
                    api_version=api_version,
                    filter=filter,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("UsagesResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_usages.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/usages"}  # type: ignore

    @distributed_trace
    def list_metric_definitions(
        self,
        resource_group_name: str,
        account_name: str,
        database_rid: str,
        collection_rid: str,
        **kwargs: Any
    ) -> Iterable[_models.MetricDefinitionsListResult]:
        """Retrieves metric definitions for the given collection.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: Cosmos DB database account name.
        :type account_name: str
        :param database_rid: Cosmos DB database rid.
        :type database_rid: str
        :param collection_rid: Cosmos DB collection rid.
        :type collection_rid: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either MetricDefinitionsListResult or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.cosmosdb.models.MetricDefinitionsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-05-15"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.MetricDefinitionsListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_metric_definitions_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    database_rid=database_rid,
                    collection_rid=collection_rid,
                    api_version=api_version,
                    template_url=self.list_metric_definitions.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_metric_definitions_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    database_rid=database_rid,
                    collection_rid=collection_rid,
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("MetricDefinitionsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_metric_definitions.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/metricDefinitions"}  # type: ignore
