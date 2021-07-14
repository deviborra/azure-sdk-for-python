# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
import platform

from devtools_testutils import AzureTestCase

from azure.data.tables import TableServiceClient, TableClient
from azure.data.tables import __version__ as VERSION
from azure.core.credentials import AzureNamedKeyCredential, AzureSasCredential

from _shared.testcase import (
    TableTestCase
)

from preparers import tables_decorator

# ------------------------------------------------------------------------------

SERVICES = {
    TableServiceClient: 'table',
    TableClient: 'table',
}

_CONNECTION_ENDPOINTS = {'table': 'TableEndpoint', 'cosmos': 'TableEndpoint'}

_CONNECTION_ENDPOINTS_SECONDARY = {'table': 'TableSecondaryEndpoint', 'cosmos': 'TableSecondaryEndpoint'}

class TestTableClient(AzureTestCase, TableTestCase):

    @tables_decorator
    def test_user_agent_custom(self, tables_storage_account_name, tables_primary_storage_account_key):
        custom_app = "TestApp/v1.0"
        service = TableServiceClient(
            self.account_url(tables_storage_account_name, "table"), credential=tables_primary_storage_account_key, user_agent=custom_app)

        def callback(response):
            assert 'User-Agent' in response.http_request.headers
            assert "TestApp/v1.0 azsdk-python-data-tables/{} Python/{} ({})".format(
                    VERSION,
                    platform.python_version(),
                    platform.platform()) in response.http_request.headers['User-Agent']

        tables = list(service.list_tables(raw_response_hook=callback))
        assert isinstance(tables,  list)

        # The count doesn't matter, going through the PagedItem calls `callback`
        count = 0
        for table in tables:
            count += 1

        def callback(response):
            assert 'User-Agent' in response.http_request.headers
            assert "TestApp/v2.0 TestApp/v1.0 azsdk-python-data-tables/{} Python/{} ({})".format(
                    VERSION,
                    platform.python_version(),
                    platform.platform()) in response.http_request.headers['User-Agent']

        tables = list(service.list_tables(raw_response_hook=callback, user_agent="TestApp/v2.0"))
        assert isinstance(tables,  list)

        # The count doesn't matter, going through the PagedItem calls `callback`
        count = 0
        for table in tables:
            count += 1

    @tables_decorator
    def test_user_agent_append(self, tables_storage_account_name, tables_primary_storage_account_key):
        service = TableServiceClient(self.account_url(tables_storage_account_name, "table"), credential=tables_primary_storage_account_key)

        def callback(response):
            assert 'User-Agent' in response.http_request.headers
            assert response.http_request.headers['User-Agent'] == 'customer_user_agent'

        custom_headers = {'User-Agent': 'customer_user_agent'}
        tables = service.list_tables(raw_response_hook=callback, headers=custom_headers)

        # The count doesn't matter, going through the PagedItem calls `callback`
        count = 0
        for table in tables:
            count += 1

    @tables_decorator
    def test_user_agent_default(self, tables_storage_account_name, tables_primary_storage_account_key):
        service = TableServiceClient(self.account_url(tables_storage_account_name, "table"), credential=tables_primary_storage_account_key)

        def callback(response):
            assert 'User-Agent' in response.http_request.headers
            assert "azsdk-python-data-tables/{} Python/{} ({})".format(
                    VERSION,
                    platform.python_version(),
                    platform.platform()) in response.http_request.headers['User-Agent']

        tables = list(service.list_tables(raw_response_hook=callback))
        assert isinstance(tables,  list)

        # The count doesn't matter, going through the PagedItem calls `callback`
        count = 0
        for table in tables:
            count += 1


class TestTableUnitTests(TableTestCase):
    tables_storage_account_name = "fake_storage_account"
    tables_primary_storage_account_key = "fakeXMZjnGsZGvd4bVr3Il5SeHA"
    credential = AzureNamedKeyCredential(name=tables_storage_account_name, key=tables_primary_storage_account_key)

    # --Helpers-----------------------------------------------------------------
    def validate_standard_account_endpoints(self, service, account_name, account_key):
        assert service is not None
        assert service.account_name == account_name
        assert service.credential.named_key.name == account_name
        assert service.credential.named_key.key == account_key
        assert ('{}.{}'.format(account_name, 'table.core.windows.net') in service.url) or ('{}.{}'.format(account_name, 'table.cosmos.azure.com') in service.url)

    # --Direct Parameters Test Cases --------------------------------------------
    def test_create_service_with_key(self):
        # Arrange

        for client, url in SERVICES.items():
            # Act
            service = client(
                self.account_url(self.tables_storage_account_name, url), credential=self.credential, table_name='foo')

            # Assert
            self.validate_standard_account_endpoints(service, self.tables_storage_account_name, self.tables_primary_storage_account_key)
            assert service.scheme == 'https'

    def test_create_service_with_connection_string(self):

        for service_type in SERVICES.items():
            # Act
            service = service_type[0].from_connection_string(
                self.connection_string(self.tables_storage_account_name, self.tables_primary_storage_account_key), table_name="test")

            # Assert
            self.validate_standard_account_endpoints(service, self.tables_storage_account_name, self.tables_primary_storage_account_key)
            assert service.scheme == 'https'

    def test_create_service_with_sas(self):
        # Arrange
        url = self.account_url(self.tables_storage_account_name, "table")
        suffix = '.table.core.windows.net'
        token = AzureSasCredential(self.generate_sas_token())
        for service_type in SERVICES:
            # Act
            service = service_type(
                self.account_url(self.tables_storage_account_name, "table"), credential=token, table_name='foo')

            # Assert
            assert service is not None
            assert service.account_name == self.tables_storage_account_name
            assert service.url.startswith('https://' + self.tables_storage_account_name + suffix)
            assert isinstance(service.credential, AzureSasCredential)

    def test_create_service_china(self):
        # Arrange
        for service_type in SERVICES.items():
            # Act
            url = self.account_url(self.tables_storage_account_name, "table").replace('core.windows.net', 'core.chinacloudapi.cn')
            service = service_type[0](
                url, credential=self.credential, table_name='foo')

            # Assert
            assert service is not None
            assert service.account_name == self.tables_storage_account_name
            assert service.credential.named_key.name == self.tables_storage_account_name
            assert service.credential.named_key.key == self.tables_primary_storage_account_key
            assert service._primary_endpoint.startswith('https://{}.{}.core.chinacloudapi.cn'.format(self.tables_storage_account_name, "table"))

    def test_create_service_protocol(self):
        # Arrange

        for service_type in SERVICES.items():
            # Act
            url = self.account_url(self.tables_storage_account_name, "table").replace('https', 'http')
            service = service_type[0](
                url, credential=self.credential, table_name='foo')

            # Assert
            self.validate_standard_account_endpoints(service, self.tables_storage_account_name, self.tables_primary_storage_account_key)
            assert service.scheme == 'http'

    def test_create_service_empty_key(self):
        # Arrange
        TABLE_SERVICES = [TableServiceClient, TableClient]

        for service_type in TABLE_SERVICES:
            # Act
            with pytest.raises(ValueError) as e:
                test_service = service_type('testaccount', credential='', table_name='foo')

            # test non-string account URL
            with pytest.raises(ValueError):
                test_service = service_type(endpoint=123456, credential=self.credential, table_name='foo')

            assert str(e.value) == "You need to provide either an AzureSasCredential or AzureNamedKeyCredential"

    def test_create_service_with_socket_timeout(self):
        # Arrange

        for service_type in SERVICES.items():
            # Act
            default_service = service_type[0](
                self.account_url(self.tables_storage_account_name, "table"), credential=self.credential, table_name='foo')
            service = service_type[0](
                self.account_url(self.tables_storage_account_name, "table"), credential=self.credential,
                table_name='foo', connection_timeout=22)

            # Assert
            self.validate_standard_account_endpoints(service, self.tables_storage_account_name, self.tables_primary_storage_account_key)
            assert service._client._client._pipeline._transport.connection_config.timeout == 22
            assert default_service._client._client._pipeline._transport.connection_config.timeout == 300

        # Assert Parent transport is shared with child client
        service = TableServiceClient(
            self.account_url(self.tables_storage_account_name, "table"),
            credential=self.credential,
            connection_timeout=22)
        assert service._client._client._pipeline._transport.connection_config.timeout == 22
        table = service.get_table_client('tablename')
        assert table._client._client._pipeline._transport._transport.connection_config.timeout == 22



    # --Connection String Test Cases --------------------------------------------
    def test_create_service_with_connection_string_key(self):
        # Arrange
        conn_string = 'AccountName={};AccountKey={};'.format(self.tables_storage_account_name, self.tables_primary_storage_account_key)

        for service_type in SERVICES.items():
            # Act
            service = service_type[0].from_connection_string(conn_string, table_name='foo')

            # Assert
            self.validate_standard_account_endpoints(service, self.tables_storage_account_name, self.tables_primary_storage_account_key)
            assert service.scheme == 'https'

    def test_create_service_with_connection_string_sas(self):
        # Arrange
        token = AzureSasCredential(self.generate_sas_token())
        conn_string = 'AccountName={};SharedAccessSignature={};'.format(self.tables_storage_account_name, token.signature)

        for service_type in SERVICES:
            # Act
            service = service_type.from_connection_string(conn_string, table_name='foo')

            # Assert
            assert service is not None
            assert service.account_name == self.tables_storage_account_name
            assert service.url.startswith('https://' + self.tables_storage_account_name + '.table.core.windows.net')
            assert isinstance(service.credential , AzureSasCredential)

    def test_create_service_with_connection_string_cosmos(self):
        # Arrange
        conn_string = 'DefaultEndpointsProtocol=https;AccountName={0};AccountKey={1};TableEndpoint=https://{0}.table.cosmos.azure.com:443/;'.format(
            self.tables_storage_account_name, self.tables_primary_storage_account_key)

        for service_type in SERVICES:
            # Act
            service = service_type.from_connection_string(conn_string, table_name='foo')

            # Assert
            assert service is not None
            assert service.account_name == self.tables_storage_account_name
            assert service.url.startswith('https://' + self.tables_storage_account_name + '.table.cosmos.azure.com')
            assert service.credential.named_key.name == self.tables_storage_account_name
            assert service.credential.named_key.key == self.tables_primary_storage_account_key
            assert service._primary_endpoint.startswith('https://' + self.tables_storage_account_name + '.table.cosmos.azure.com')
            assert service.scheme == 'https'

    def test_create_service_with_connection_string_endpoint_protocol(self):
        # Arrange
        conn_string = 'AccountName={};AccountKey={};DefaultEndpointsProtocol=http;EndpointSuffix=core.chinacloudapi.cn;'.format(
            self.tables_storage_account_name, self.tables_primary_storage_account_key)

        for service_type in SERVICES.items():
            # Act
            service = service_type[0].from_connection_string(conn_string, table_name="foo")

            # Assert
            assert service is not None
            assert service.account_name == self.tables_storage_account_name
            assert service.credential.named_key.name == self.tables_storage_account_name
            assert service.credential.named_key.key == self.tables_primary_storage_account_key
            assert service._primary_endpoint.startswith('http://{}.{}.core.chinacloudapi.cn'.format(self.tables_storage_account_name, "table"))
            assert service.scheme == 'http'

    def test_create_service_with_connection_string_emulated(self):
        # Arrange
        for service_type in SERVICES.items():
            conn_string = 'UseDevelopmentStorage=true;'.format(self.tables_storage_account_name, self.tables_primary_storage_account_key)

            # Act
            with pytest.raises(ValueError):
                service = service_type[0].from_connection_string(conn_string, table_name="foo")

    def test_create_service_with_connection_string_custom_domain(self):
        # Arrange
        for service_type in SERVICES.items():
            conn_string = 'AccountName={};AccountKey={};TableEndpoint=www.mydomain.com;'.format(
                self.tables_storage_account_name, self.tables_primary_storage_account_key)

            # Act
            service = service_type[0].from_connection_string(conn_string, table_name="foo")

            # Assert
            assert service is not None
            assert service.credential.named_key.name == self.tables_storage_account_name
            assert service.credential.named_key.key == self.tables_primary_storage_account_key
            assert service._primary_endpoint.startswith('https://www.mydomain.com')

    def test_create_service_with_conn_str_custom_domain_trailing_slash(self):
        # Arrange
        for service_type in SERVICES.items():
            conn_string = 'AccountName={};AccountKey={};TableEndpoint=www.mydomain.com/;'.format(
                self.tables_storage_account_name, self.tables_primary_storage_account_key)

            # Act
            service = service_type[0].from_connection_string(conn_string, table_name="foo")

            # Assert
            assert service is not None
            assert service.credential.named_key.name == self.tables_storage_account_name
            assert service.credential.named_key.key == self.tables_primary_storage_account_key
            assert service._primary_endpoint.startswith('https://www.mydomain.com')

    def test_create_service_with_conn_str_custom_domain_sec_override(self):
        # Arrange
        for service_type in SERVICES.items():
            conn_string = 'AccountName={};AccountKey={};TableEndpoint=www.mydomain.com/;'.format(
                self.tables_storage_account_name, self.tables_primary_storage_account_key)

            # Act
            service = service_type[0].from_connection_string(
                conn_string, secondary_hostname="www-sec.mydomain.com", table_name="foo")

            # Assert
            assert service is not None
            assert service.credential.named_key.name == self.tables_storage_account_name
            assert service.credential.named_key.key == self.tables_primary_storage_account_key
            assert service._primary_endpoint.startswith('https://www.mydomain.com')

    def test_create_service_with_conn_str_fails_if_sec_without_primary(self):
        for service_type in SERVICES.items():
            # Arrange
            conn_string = 'AccountName={};AccountKey={};{}=www.mydomain.com;'.format(
                self.tables_storage_account_name, self.tables_primary_storage_account_key,
                _CONNECTION_ENDPOINTS_SECONDARY.get(service_type[1]))

            # Act

            # Fails if primary excluded
            with pytest.raises(ValueError):
                service = service_type[0].from_connection_string(conn_string, table_name="foo")

    def test_create_service_with_conn_str_succeeds_if_sec_with_primary(self):
        for service_type in SERVICES.items():
            # Arrange
            conn_string = 'AccountName={};AccountKey={};{}=www.mydomain.com;{}=www-sec.mydomain.com;'.format(
                self.tables_storage_account_name,
                self.tables_primary_storage_account_key,
                _CONNECTION_ENDPOINTS.get(service_type[1]),
                _CONNECTION_ENDPOINTS_SECONDARY.get(service_type[1]))

            # Act
            service = service_type[0].from_connection_string(conn_string, table_name="foo")

            # Assert
            assert service is not None
            assert service.credential.named_key.name == self.tables_storage_account_name
            assert service.credential.named_key.key == self.tables_primary_storage_account_key
            assert service._primary_endpoint.startswith('https://www.mydomain.com')

    def test_create_service_with_custom_account_endpoint_path(self):
        token = AzureSasCredential(self.generate_sas_token())
        custom_account_url = "http://local-machine:11002/custom/account/path/" + token.signature
        for service_type in SERVICES.items():
            conn_string = 'DefaultEndpointsProtocol=http;AccountName={};AccountKey={};TableEndpoint={};'.format(
                self.tables_storage_account_name, self.tables_primary_storage_account_key, custom_account_url)

            # Act
            service = service_type[0].from_connection_string(conn_string, table_name="foo")

            # Assert
            assert service.account_name == self.tables_storage_account_name
            assert service.credential.named_key.name == self.tables_storage_account_name
            assert service.credential.named_key.key == self.tables_primary_storage_account_key
            assert service._primary_hostname == 'local-machine:11002/custom/account/path'

        service = TableServiceClient(endpoint=custom_account_url)
        assert service.account_name == "custom"
        assert service.credential == None
        assert service._primary_hostname == 'local-machine:11002/custom/account/path'
        assert service.url.startswith('http://local-machine:11002/custom/account/path')

        service = TableClient(endpoint=custom_account_url, table_name="foo")
        assert service.account_name == "custom"
        assert service.table_name == "foo"
        assert service.credential == None
        assert service._primary_hostname == 'local-machine:11002/custom/account/path'
        assert service.url.startswith('http://local-machine:11002/custom/account/path')

        service = TableClient.from_table_url("http://local-machine:11002/custom/account/path/foo" + token.signature)
        assert service.account_name == "custom"
        assert service.table_name == "foo"
        assert service.credential == None
        assert service._primary_hostname == 'local-machine:11002/custom/account/path'
        assert service.url.startswith('http://local-machine:11002/custom/account/path')

    def test_create_table_client_with_complete_table_url(self):
        # Arrange
        table_url = self.account_url(self.tables_storage_account_name, "table") + "/foo"
        service = TableClient(table_url, table_name='bar', credential=self.credential)

        # Assert
        assert service.scheme == 'https'
        assert service.table_name == 'bar'
        assert service.account_name == self.tables_storage_account_name

    def test_create_table_client_with_complete_url(self):
        # Arrange
        table_url = "https://{}.table.core.windows.net:443/foo".format(self.tables_storage_account_name)
        service = TableClient(endpoint=table_url, table_name='bar', credential=self.credential)

        # Assert
        assert service.scheme == 'https'
        assert service.table_name == 'bar'
        assert service.account_name == self.tables_storage_account_name

    def test_create_table_client_with_invalid_name(self):
        # Arrange
        table_url = "https://{}.table.core.windows.net:443/foo".format("test")
        invalid_table_name = "my_table"

        # Assert
        with pytest.raises(ValueError) as excinfo:
            service = TableClient(endpoint=table_url, table_name=invalid_table_name, credential="self.tables_primary_storage_account_key")

        assert "Table names must be alphanumeric, cannot begin with a number, and must be between 3-63 characters long." in str(excinfo)

    def test_error_with_malformed_conn_str(self):
        # Arrange

        for conn_str in ["", "foobar", "foobar=baz=foo", "foo;bar;baz", "foo=;bar=;", "=", ";", "=;=="]:
            for service_type in SERVICES.items():
                # Act
                with pytest.raises(ValueError) as e:
                    service = service_type[0].from_connection_string(conn_str, table_name="test")

                if conn_str in("", "foobar", "foo;bar;baz", ";", "foo=;bar=;", "=", "=;=="):
                    assert str(e.value) == "Connection string is either blank or malformed."
                elif conn_str in ("foobar=baz=foo"):
                   assert str(e.value) == "Connection string missing required connection details."

    def test_closing_pipeline_client(self):
        # Arrange
        for client, url in SERVICES.items():
            # Act
            service = client(
                self.account_url(self.tables_storage_account_name, "table"), credential=self.credential, table_name='table')

            # Assert
            with service:
                assert hasattr(service, 'close')
                service.close()

    def test_closing_pipeline_client_simple(self):
        # Arrange
        for client, url in SERVICES.items():
            # Act
            service = client(
                self.account_url(self.tables_storage_account_name, "table"), credential=self.credential, table_name='table')
            service.close()

    @pytest.mark.skip("HTTP prefix does not raise an error")
    def test_create_service_with_token_and_http(self):
        for service_type in SERVICES:

            with pytest.raises(ValueError):
                url = self.account_url(self.tables_storage_account_name, "table").replace('https', 'http')
                service_type(url, credential=AzureSasCredential("fake_sas_credential"), table_name='foo')

    def test_create_service_with_token(self):
        url = self.account_url(self.tables_storage_account_name, "table")
        suffix = '.table.core.windows.net'
        self.token_credential = AzureSasCredential("fake_sas_credential")

        service = TableClient(url, credential=self.token_credential, table_name='foo')

        # Assert
        assert service is not None
        assert service.account_name == self.tables_storage_account_name
        assert service.url.startswith('https://' + self.tables_storage_account_name + suffix)
        assert service.credential == self.token_credential
        assert not hasattr(service.credential, 'account_key')

        service = TableServiceClient(url, credential=self.token_credential, table_name='foo')

        # Assert
        assert service is not None
        assert service.account_name == self.tables_storage_account_name
        assert service.url.startswith('https://' + self.tables_storage_account_name + suffix)
        assert service.credential == self.token_credential
        assert not hasattr(service.credential, 'account_key')

    def test_create_client_with_api_version(self):
        url = self.account_url(self.tables_storage_account_name, "table")
        client = TableServiceClient(url, credential=self.credential)
        assert client._client._config.version == "2019-02-02"
        table = client.get_table_client('tablename')
        assert table._client._config.version == "2019-02-02"

        client = TableServiceClient(url, credential=self.credential, api_version="2019-07-07")
        assert client._client._config.version == "2019-07-07"
        table = client.get_table_client('tablename')
        assert table._client._config.version == "2019-07-07"

        with pytest.raises(ValueError):
            TableServiceClient(url, credential=self.credential, api_version="foo")

    def test_create_client_for_azurite(self):
        azurite_credential = AzureNamedKeyCredential("myaccount", self.tables_primary_storage_account_key)
        http_connstr = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey={};TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;".format(
            self.tables_primary_storage_account_key
        )
        https_connstr = "DefaultEndpointsProtocol=https;AccountName=devstoreaccount1;AccountKey={};TableEndpoint=https://127.0.0.1:10002/devstoreaccount1;".format(
            self.tables_primary_storage_account_key
        )
        account_url = "https://127.0.0.1:10002/myaccount"
        client = TableServiceClient(account_url, credential=azurite_credential)
        assert client.account_name == "myaccount"
        assert client.url == "https://127.0.0.1:10002/myaccount"
        assert client._location_mode == "primary"
        assert client._secondary_endpoint == "https://127.0.0.1:10002/myaccount-secondary"
        assert client.credential.named_key.key == azurite_credential.named_key.key
        assert client.credential.named_key.name == azurite_credential.named_key.name
        assert not client._cosmos_endpoint

        client = TableServiceClient.from_connection_string(http_connstr)
        assert client.account_name == "devstoreaccount1"
        assert client.url == "http://127.0.0.1:10002/devstoreaccount1"
        assert client._location_mode == "primary"
        assert client._secondary_endpoint == "http://127.0.0.1:10002/devstoreaccount1-secondary"
        assert client.credential.named_key.key == self.tables_primary_storage_account_key
        assert client.credential.named_key.name == "devstoreaccount1"
        assert not client._cosmos_endpoint

        client = TableServiceClient.from_connection_string(https_connstr)
        assert client.account_name == "devstoreaccount1"
        assert client.url == "https://127.0.0.1:10002/devstoreaccount1"
        assert client._location_mode == "primary"
        assert client._secondary_endpoint == "https://127.0.0.1:10002/devstoreaccount1-secondary"
        assert client.credential.named_key.key == self.tables_primary_storage_account_key
        assert client.credential.named_key.name == "devstoreaccount1"
        assert not client._cosmos_endpoint

        table = TableClient(account_url, "tablename", credential=azurite_credential)
        assert table.account_name == "myaccount"
        assert table.table_name == "tablename"
        assert table.url == "https://127.0.0.1:10002/myaccount"
        assert table._location_mode == "primary"
        assert table._secondary_endpoint == "https://127.0.0.1:10002/myaccount-secondary"
        assert table.credential.named_key.key == azurite_credential.named_key.key
        assert table.credential.named_key.name == azurite_credential.named_key.name
        assert not table._cosmos_endpoint

        table = TableClient.from_connection_string(http_connstr, "tablename")
        assert table.account_name == "devstoreaccount1"
        assert table.table_name == "tablename"
        assert table.url == "http://127.0.0.1:10002/devstoreaccount1"
        assert table._location_mode == "primary"
        assert table._secondary_endpoint == "http://127.0.0.1:10002/devstoreaccount1-secondary"
        assert table.credential.named_key.key == self.tables_primary_storage_account_key
        assert table.credential.named_key.name == "devstoreaccount1"
        assert not table._cosmos_endpoint

        table = TableClient.from_connection_string(https_connstr, "tablename")
        assert table.account_name == "devstoreaccount1"
        assert table.table_name == "tablename"
        assert table.url == "https://127.0.0.1:10002/devstoreaccount1"
        assert table._location_mode == "primary"
        assert table._secondary_endpoint == "https://127.0.0.1:10002/devstoreaccount1-secondary"
        assert table.credential.named_key.key == self.tables_primary_storage_account_key
        assert table.credential.named_key.name == "devstoreaccount1"
        assert not table._cosmos_endpoint

        table_url = "https://127.0.0.1:10002/myaccount/Tables('tablename')"
        table = TableClient.from_table_url(table_url, credential=azurite_credential)
        assert table.account_name == "myaccount"
        assert table.table_name == "tablename"
        assert table.url == "https://127.0.0.1:10002/myaccount"
        assert table._location_mode == "primary"
        assert table._secondary_endpoint == "https://127.0.0.1:10002/myaccount-secondary"
        assert table.credential.named_key.key == azurite_credential.named_key.key
        assert table.credential.named_key.name == azurite_credential.named_key.name
        assert not table._cosmos_endpoint