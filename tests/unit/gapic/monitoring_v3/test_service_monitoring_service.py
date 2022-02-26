# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import mock

import grpc
from grpc.experimental import aio
import math
import pytest
from proto.marshal.rules.dates import DurationRule, TimestampRule


from google.api_core import client_options
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.api_core import path_template
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.monitoring_v3.services.service_monitoring_service import (
    ServiceMonitoringServiceAsyncClient,
)
from google.cloud.monitoring_v3.services.service_monitoring_service import (
    ServiceMonitoringServiceClient,
)
from google.cloud.monitoring_v3.services.service_monitoring_service import pagers
from google.cloud.monitoring_v3.services.service_monitoring_service import transports
from google.cloud.monitoring_v3.types import service
from google.cloud.monitoring_v3.types import service as gm_service
from google.cloud.monitoring_v3.types import service_service
from google.oauth2 import service_account
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.type import calendar_period_pb2  # type: ignore
import google.auth


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return (
        "foo.googleapis.com"
        if ("localhost" in client.DEFAULT_ENDPOINT)
        else client.DEFAULT_ENDPOINT
    )


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert ServiceMonitoringServiceClient._get_default_mtls_endpoint(None) is None
    assert (
        ServiceMonitoringServiceClient._get_default_mtls_endpoint(api_endpoint)
        == api_mtls_endpoint
    )
    assert (
        ServiceMonitoringServiceClient._get_default_mtls_endpoint(api_mtls_endpoint)
        == api_mtls_endpoint
    )
    assert (
        ServiceMonitoringServiceClient._get_default_mtls_endpoint(sandbox_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        ServiceMonitoringServiceClient._get_default_mtls_endpoint(sandbox_mtls_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        ServiceMonitoringServiceClient._get_default_mtls_endpoint(non_googleapi)
        == non_googleapi
    )


@pytest.mark.parametrize(
    "client_class",
    [ServiceMonitoringServiceClient, ServiceMonitoringServiceAsyncClient,],
)
def test_service_monitoring_service_client_from_service_account_info(client_class):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_info"
    ) as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == "monitoring.googleapis.com:443"


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.ServiceMonitoringServiceGrpcTransport, "grpc"),
        (transports.ServiceMonitoringServiceGrpcAsyncIOTransport, "grpc_asyncio"),
    ],
)
def test_service_monitoring_service_client_service_account_always_use_jwt(
    transport_class, transport_name
):
    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize(
    "client_class",
    [ServiceMonitoringServiceClient, ServiceMonitoringServiceAsyncClient,],
)
def test_service_monitoring_service_client_from_service_account_file(client_class):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json")
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json("dummy/file/path.json")
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == "monitoring.googleapis.com:443"


def test_service_monitoring_service_client_get_transport_class():
    transport = ServiceMonitoringServiceClient.get_transport_class()
    available_transports = [
        transports.ServiceMonitoringServiceGrpcTransport,
    ]
    assert transport in available_transports

    transport = ServiceMonitoringServiceClient.get_transport_class("grpc")
    assert transport == transports.ServiceMonitoringServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            ServiceMonitoringServiceClient,
            transports.ServiceMonitoringServiceGrpcTransport,
            "grpc",
        ),
        (
            ServiceMonitoringServiceAsyncClient,
            transports.ServiceMonitoringServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
    ],
)
@mock.patch.object(
    ServiceMonitoringServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(ServiceMonitoringServiceClient),
)
@mock.patch.object(
    ServiceMonitoringServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(ServiceMonitoringServiceAsyncClient),
)
def test_service_monitoring_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(
        ServiceMonitoringServiceClient, "get_transport_class"
    ) as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(
        ServiceMonitoringServiceClient, "get_transport_class"
    ) as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class(transport=transport_name)

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}
    ):
        with pytest.raises(ValueError):
            client = client_class(transport=transport_name)

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,use_client_cert_env",
    [
        (
            ServiceMonitoringServiceClient,
            transports.ServiceMonitoringServiceGrpcTransport,
            "grpc",
            "true",
        ),
        (
            ServiceMonitoringServiceAsyncClient,
            transports.ServiceMonitoringServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            ServiceMonitoringServiceClient,
            transports.ServiceMonitoringServiceGrpcTransport,
            "grpc",
            "false",
        ),
        (
            ServiceMonitoringServiceAsyncClient,
            transports.ServiceMonitoringServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
    ],
)
@mock.patch.object(
    ServiceMonitoringServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(ServiceMonitoringServiceClient),
)
@mock.patch.object(
    ServiceMonitoringServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(ServiceMonitoringServiceAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_service_monitoring_service_client_mtls_env_auto(
    client_class, transport_class, transport_name, use_client_cert_env
):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        options = client_options.ClientOptions(
            client_cert_source=client_cert_source_callback
        )
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client.DEFAULT_ENDPOINT
            else:
                expected_client_cert_source = client_cert_source_callback
                expected_host = client.DEFAULT_MTLS_ENDPOINT

            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=expected_host,
                scopes=None,
                client_cert_source_for_mtls=expected_client_cert_source,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=True,
            ):
                with mock.patch(
                    "google.auth.transport.mtls.default_client_cert_source",
                    return_value=client_cert_source_callback,
                ):
                    if use_client_cert_env == "false":
                        expected_host = client.DEFAULT_ENDPOINT
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class(transport=transport_name)
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                        always_use_jwt_access=True,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=False,
            ):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_ENDPOINT,
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                )


@pytest.mark.parametrize(
    "client_class",
    [ServiceMonitoringServiceClient, ServiceMonitoringServiceAsyncClient],
)
@mock.patch.object(
    ServiceMonitoringServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(ServiceMonitoringServiceClient),
)
@mock.patch.object(
    ServiceMonitoringServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(ServiceMonitoringServiceAsyncClient),
)
def test_service_monitoring_service_client_get_mtls_endpoint_and_cert_source(
    client_class,
):
    mock_client_cert_source = mock.Mock()

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "true".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(
            client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
        )
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
            options
        )
        assert api_endpoint == mock_api_endpoint
        assert cert_source == mock_client_cert_source

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "false".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}):
        mock_client_cert_source = mock.Mock()
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(
            client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
        )
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
            options
        )
        assert api_endpoint == mock_api_endpoint
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert doesn't exist.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=False,
        ):
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
            assert api_endpoint == client_class.DEFAULT_ENDPOINT
            assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert exists.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=True,
        ):
            with mock.patch(
                "google.auth.transport.mtls.default_client_cert_source",
                return_value=mock_client_cert_source,
            ):
                (
                    api_endpoint,
                    cert_source,
                ) = client_class.get_mtls_endpoint_and_cert_source()
                assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
                assert cert_source == mock_client_cert_source


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            ServiceMonitoringServiceClient,
            transports.ServiceMonitoringServiceGrpcTransport,
            "grpc",
        ),
        (
            ServiceMonitoringServiceAsyncClient,
            transports.ServiceMonitoringServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
    ],
)
def test_service_monitoring_service_client_client_options_scopes(
    client_class, transport_class, transport_name
):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(scopes=["1", "2"],)
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,grpc_helpers",
    [
        (
            ServiceMonitoringServiceClient,
            transports.ServiceMonitoringServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            ServiceMonitoringServiceAsyncClient,
            transports.ServiceMonitoringServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_service_monitoring_service_client_client_options_credentials_file(
    client_class, transport_class, transport_name, grpc_helpers
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")

    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


def test_service_monitoring_service_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.monitoring_v3.services.service_monitoring_service.transports.ServiceMonitoringServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = ServiceMonitoringServiceClient(
            client_options={"api_endpoint": "squid.clam.whelk"}
        )
        grpc_transport.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,grpc_helpers",
    [
        (
            ServiceMonitoringServiceClient,
            transports.ServiceMonitoringServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            ServiceMonitoringServiceAsyncClient,
            transports.ServiceMonitoringServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_service_monitoring_service_client_create_channel_credentials_file(
    client_class, transport_class, transport_name, grpc_helpers
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")

    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

    # test that the credentials from file are saved and used as the credentials.
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel"
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        file_creds = ga_credentials.AnonymousCredentials()
        load_creds.return_value = (file_creds, None)
        adc.return_value = (creds, None)
        client = client_class(client_options=options, transport=transport_name)
        create_channel.assert_called_with(
            "monitoring.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/monitoring",
                "https://www.googleapis.com/auth/monitoring.read",
            ),
            scopes=None,
            default_host="monitoring.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize("request_type", [service_service.CreateServiceRequest, dict,])
def test_create_service(request_type, transport: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gm_service.Service(
            name="name_value", display_name="display_name_value", custom=None,
        )
        response = client.create_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.CreateServiceRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, gm_service.Service)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"


def test_create_service_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_service), "__call__") as call:
        client.create_service()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.CreateServiceRequest()


@pytest.mark.asyncio
async def test_create_service_async(
    transport: str = "grpc_asyncio", request_type=service_service.CreateServiceRequest
):
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gm_service.Service(name="name_value", display_name="display_name_value",)
        )
        response = await client.create_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.CreateServiceRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, gm_service.Service)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"


@pytest.mark.asyncio
async def test_create_service_async_from_dict():
    await test_create_service_async(request_type=dict)


def test_create_service_field_headers():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.CreateServiceRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_service), "__call__") as call:
        call.return_value = gm_service.Service()
        client.create_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_service_field_headers_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.CreateServiceRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_service), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gm_service.Service())
        await client.create_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_create_service_flattened():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gm_service.Service()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_service(
            parent="parent_value", service=gm_service.Service(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].service
        mock_val = gm_service.Service(name="name_value")
        assert arg == mock_val


def test_create_service_flattened_error():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_service(
            service_service.CreateServiceRequest(),
            parent="parent_value",
            service=gm_service.Service(name="name_value"),
        )


@pytest.mark.asyncio
async def test_create_service_flattened_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gm_service.Service()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gm_service.Service())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_service(
            parent="parent_value", service=gm_service.Service(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].service
        mock_val = gm_service.Service(name="name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_service_flattened_error_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_service(
            service_service.CreateServiceRequest(),
            parent="parent_value",
            service=gm_service.Service(name="name_value"),
        )


@pytest.mark.parametrize("request_type", [service_service.GetServiceRequest, dict,])
def test_get_service(request_type, transport: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Service(
            name="name_value", display_name="display_name_value", custom=None,
        )
        response = client.get_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.GetServiceRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Service)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"


def test_get_service_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_service), "__call__") as call:
        client.get_service()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.GetServiceRequest()


@pytest.mark.asyncio
async def test_get_service_async(
    transport: str = "grpc_asyncio", request_type=service_service.GetServiceRequest
):
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.Service(name="name_value", display_name="display_name_value",)
        )
        response = await client.get_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.GetServiceRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.Service)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"


@pytest.mark.asyncio
async def test_get_service_async_from_dict():
    await test_get_service_async(request_type=dict)


def test_get_service_field_headers():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.GetServiceRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_service), "__call__") as call:
        call.return_value = service.Service()
        client.get_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_service_field_headers_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.GetServiceRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_service), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.Service())
        await client.get_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_get_service_flattened():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Service()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_service(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_service_flattened_error():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_service(
            service_service.GetServiceRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_get_service_flattened_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.Service()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(service.Service())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_service(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_service_flattened_error_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_service(
            service_service.GetServiceRequest(), name="name_value",
        )


@pytest.mark.parametrize("request_type", [service_service.ListServicesRequest, dict,])
def test_list_services(request_type, transport: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_services), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service_service.ListServicesResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_services(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.ListServicesRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListServicesPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_services_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_services), "__call__") as call:
        client.list_services()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.ListServicesRequest()


@pytest.mark.asyncio
async def test_list_services_async(
    transport: str = "grpc_asyncio", request_type=service_service.ListServicesRequest
):
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_services), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service_service.ListServicesResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_services(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.ListServicesRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListServicesAsyncPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.asyncio
async def test_list_services_async_from_dict():
    await test_list_services_async(request_type=dict)


def test_list_services_field_headers():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.ListServicesRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_services), "__call__") as call:
        call.return_value = service_service.ListServicesResponse()
        client.list_services(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_services_field_headers_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.ListServicesRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_services), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service_service.ListServicesResponse()
        )
        await client.list_services(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_list_services_flattened():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_services), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service_service.ListServicesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_services(parent="parent_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_services_flattened_error():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_services(
            service_service.ListServicesRequest(), parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_services_flattened_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_services), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = service_service.ListServicesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service_service.ListServicesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_services(parent="parent_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_services_flattened_error_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_services(
            service_service.ListServicesRequest(), parent="parent_value",
        )


def test_list_services_pager(transport_name: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials, transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_services), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service_service.ListServicesResponse(
                services=[service.Service(), service.Service(), service.Service(),],
                next_page_token="abc",
            ),
            service_service.ListServicesResponse(services=[], next_page_token="def",),
            service_service.ListServicesResponse(
                services=[service.Service(),], next_page_token="ghi",
            ),
            service_service.ListServicesResponse(
                services=[service.Service(), service.Service(),],
            ),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_services(request={})

        assert pager._metadata == metadata

        results = [i for i in pager]
        assert len(results) == 6
        assert all(isinstance(i, service.Service) for i in results)


def test_list_services_pages(transport_name: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials, transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_services), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service_service.ListServicesResponse(
                services=[service.Service(), service.Service(), service.Service(),],
                next_page_token="abc",
            ),
            service_service.ListServicesResponse(services=[], next_page_token="def",),
            service_service.ListServicesResponse(
                services=[service.Service(),], next_page_token="ghi",
            ),
            service_service.ListServicesResponse(
                services=[service.Service(), service.Service(),],
            ),
            RuntimeError,
        )
        pages = list(client.list_services(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_services_async_pager():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_services), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service_service.ListServicesResponse(
                services=[service.Service(), service.Service(), service.Service(),],
                next_page_token="abc",
            ),
            service_service.ListServicesResponse(services=[], next_page_token="def",),
            service_service.ListServicesResponse(
                services=[service.Service(),], next_page_token="ghi",
            ),
            service_service.ListServicesResponse(
                services=[service.Service(), service.Service(),],
            ),
            RuntimeError,
        )
        async_pager = await client.list_services(request={},)
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, service.Service) for i in responses)


@pytest.mark.asyncio
async def test_list_services_async_pages():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_services), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service_service.ListServicesResponse(
                services=[service.Service(), service.Service(), service.Service(),],
                next_page_token="abc",
            ),
            service_service.ListServicesResponse(services=[], next_page_token="def",),
            service_service.ListServicesResponse(
                services=[service.Service(),], next_page_token="ghi",
            ),
            service_service.ListServicesResponse(
                services=[service.Service(), service.Service(),],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_services(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize("request_type", [service_service.UpdateServiceRequest, dict,])
def test_update_service(request_type, transport: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gm_service.Service(
            name="name_value", display_name="display_name_value", custom=None,
        )
        response = client.update_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.UpdateServiceRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, gm_service.Service)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"


def test_update_service_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_service), "__call__") as call:
        client.update_service()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.UpdateServiceRequest()


@pytest.mark.asyncio
async def test_update_service_async(
    transport: str = "grpc_asyncio", request_type=service_service.UpdateServiceRequest
):
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gm_service.Service(name="name_value", display_name="display_name_value",)
        )
        response = await client.update_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.UpdateServiceRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, gm_service.Service)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"


@pytest.mark.asyncio
async def test_update_service_async_from_dict():
    await test_update_service_async(request_type=dict)


def test_update_service_field_headers():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.UpdateServiceRequest()

    request.service.name = "service.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_service), "__call__") as call:
        call.return_value = gm_service.Service()
        client.update_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "service.name=service.name/value",) in kw[
        "metadata"
    ]


@pytest.mark.asyncio
async def test_update_service_field_headers_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.UpdateServiceRequest()

    request.service.name = "service.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_service), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gm_service.Service())
        await client.update_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "service.name=service.name/value",) in kw[
        "metadata"
    ]


def test_update_service_flattened():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gm_service.Service()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_service(service=gm_service.Service(name="name_value"),)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].service
        mock_val = gm_service.Service(name="name_value")
        assert arg == mock_val


def test_update_service_flattened_error():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_service(
            service_service.UpdateServiceRequest(),
            service=gm_service.Service(name="name_value"),
        )


@pytest.mark.asyncio
async def test_update_service_flattened_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gm_service.Service()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gm_service.Service())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_service(
            service=gm_service.Service(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].service
        mock_val = gm_service.Service(name="name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_service_flattened_error_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_service(
            service_service.UpdateServiceRequest(),
            service=gm_service.Service(name="name_value"),
        )


@pytest.mark.parametrize("request_type", [service_service.DeleteServiceRequest, dict,])
def test_delete_service(request_type, transport: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.DeleteServiceRequest()

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_service_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_service), "__call__") as call:
        client.delete_service()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.DeleteServiceRequest()


@pytest.mark.asyncio
async def test_delete_service_async(
    transport: str = "grpc_asyncio", request_type=service_service.DeleteServiceRequest
):
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.DeleteServiceRequest()

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.asyncio
async def test_delete_service_async_from_dict():
    await test_delete_service_async(request_type=dict)


def test_delete_service_field_headers():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.DeleteServiceRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_service), "__call__") as call:
        call.return_value = None
        client.delete_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_service_field_headers_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.DeleteServiceRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_service), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_service(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_delete_service_flattened():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_service(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_service_flattened_error():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_service(
            service_service.DeleteServiceRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_service_flattened_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_service), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_service(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_delete_service_flattened_error_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_service(
            service_service.DeleteServiceRequest(), name="name_value",
        )


@pytest.mark.parametrize(
    "request_type", [service_service.CreateServiceLevelObjectiveRequest, dict,]
)
def test_create_service_level_objective(request_type, transport: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ServiceLevelObjective(
            name="name_value",
            display_name="display_name_value",
            goal=0.419,
            rolling_period=duration_pb2.Duration(seconds=751),
        )
        response = client.create_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.CreateServiceLevelObjectiveRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ServiceLevelObjective)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert math.isclose(response.goal, 0.419, rel_tol=1e-6)


def test_create_service_level_objective_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_service_level_objective), "__call__"
    ) as call:
        client.create_service_level_objective()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.CreateServiceLevelObjectiveRequest()


@pytest.mark.asyncio
async def test_create_service_level_objective_async(
    transport: str = "grpc_asyncio",
    request_type=service_service.CreateServiceLevelObjectiveRequest,
):
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ServiceLevelObjective(
                name="name_value", display_name="display_name_value", goal=0.419,
            )
        )
        response = await client.create_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.CreateServiceLevelObjectiveRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ServiceLevelObjective)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert math.isclose(response.goal, 0.419, rel_tol=1e-6)


@pytest.mark.asyncio
async def test_create_service_level_objective_async_from_dict():
    await test_create_service_level_objective_async(request_type=dict)


def test_create_service_level_objective_field_headers():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.CreateServiceLevelObjectiveRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_service_level_objective), "__call__"
    ) as call:
        call.return_value = service.ServiceLevelObjective()
        client.create_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_service_level_objective_field_headers_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.CreateServiceLevelObjectiveRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_service_level_objective), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ServiceLevelObjective()
        )
        await client.create_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_create_service_level_objective_flattened():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ServiceLevelObjective()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_service_level_objective(
            parent="parent_value",
            service_level_objective=service.ServiceLevelObjective(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].service_level_objective
        mock_val = service.ServiceLevelObjective(name="name_value")
        assert arg == mock_val


def test_create_service_level_objective_flattened_error():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_service_level_objective(
            service_service.CreateServiceLevelObjectiveRequest(),
            parent="parent_value",
            service_level_objective=service.ServiceLevelObjective(name="name_value"),
        )


@pytest.mark.asyncio
async def test_create_service_level_objective_flattened_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ServiceLevelObjective()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ServiceLevelObjective()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_service_level_objective(
            parent="parent_value",
            service_level_objective=service.ServiceLevelObjective(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].service_level_objective
        mock_val = service.ServiceLevelObjective(name="name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_service_level_objective_flattened_error_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_service_level_objective(
            service_service.CreateServiceLevelObjectiveRequest(),
            parent="parent_value",
            service_level_objective=service.ServiceLevelObjective(name="name_value"),
        )


@pytest.mark.parametrize(
    "request_type", [service_service.GetServiceLevelObjectiveRequest, dict,]
)
def test_get_service_level_objective(request_type, transport: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ServiceLevelObjective(
            name="name_value",
            display_name="display_name_value",
            goal=0.419,
            rolling_period=duration_pb2.Duration(seconds=751),
        )
        response = client.get_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.GetServiceLevelObjectiveRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ServiceLevelObjective)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert math.isclose(response.goal, 0.419, rel_tol=1e-6)


def test_get_service_level_objective_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_service_level_objective), "__call__"
    ) as call:
        client.get_service_level_objective()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.GetServiceLevelObjectiveRequest()


@pytest.mark.asyncio
async def test_get_service_level_objective_async(
    transport: str = "grpc_asyncio",
    request_type=service_service.GetServiceLevelObjectiveRequest,
):
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ServiceLevelObjective(
                name="name_value", display_name="display_name_value", goal=0.419,
            )
        )
        response = await client.get_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.GetServiceLevelObjectiveRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ServiceLevelObjective)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert math.isclose(response.goal, 0.419, rel_tol=1e-6)


@pytest.mark.asyncio
async def test_get_service_level_objective_async_from_dict():
    await test_get_service_level_objective_async(request_type=dict)


def test_get_service_level_objective_field_headers():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.GetServiceLevelObjectiveRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_service_level_objective), "__call__"
    ) as call:
        call.return_value = service.ServiceLevelObjective()
        client.get_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_service_level_objective_field_headers_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.GetServiceLevelObjectiveRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_service_level_objective), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ServiceLevelObjective()
        )
        await client.get_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_get_service_level_objective_flattened():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ServiceLevelObjective()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_service_level_objective(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_service_level_objective_flattened_error():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_service_level_objective(
            service_service.GetServiceLevelObjectiveRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_get_service_level_objective_flattened_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ServiceLevelObjective()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ServiceLevelObjective()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_service_level_objective(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_service_level_objective_flattened_error_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_service_level_objective(
            service_service.GetServiceLevelObjectiveRequest(), name="name_value",
        )


@pytest.mark.parametrize(
    "request_type", [service_service.ListServiceLevelObjectivesRequest, dict,]
)
def test_list_service_level_objectives(request_type, transport: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_service_level_objectives), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service_service.ListServiceLevelObjectivesResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_service_level_objectives(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.ListServiceLevelObjectivesRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListServiceLevelObjectivesPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_service_level_objectives_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_service_level_objectives), "__call__"
    ) as call:
        client.list_service_level_objectives()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.ListServiceLevelObjectivesRequest()


@pytest.mark.asyncio
async def test_list_service_level_objectives_async(
    transport: str = "grpc_asyncio",
    request_type=service_service.ListServiceLevelObjectivesRequest,
):
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_service_level_objectives), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service_service.ListServiceLevelObjectivesResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_service_level_objectives(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.ListServiceLevelObjectivesRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListServiceLevelObjectivesAsyncPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.asyncio
async def test_list_service_level_objectives_async_from_dict():
    await test_list_service_level_objectives_async(request_type=dict)


def test_list_service_level_objectives_field_headers():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.ListServiceLevelObjectivesRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_service_level_objectives), "__call__"
    ) as call:
        call.return_value = service_service.ListServiceLevelObjectivesResponse()
        client.list_service_level_objectives(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_service_level_objectives_field_headers_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.ListServiceLevelObjectivesRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_service_level_objectives), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service_service.ListServiceLevelObjectivesResponse()
        )
        await client.list_service_level_objectives(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_list_service_level_objectives_flattened():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_service_level_objectives), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service_service.ListServiceLevelObjectivesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_service_level_objectives(parent="parent_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_service_level_objectives_flattened_error():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_service_level_objectives(
            service_service.ListServiceLevelObjectivesRequest(), parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_service_level_objectives_flattened_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_service_level_objectives), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service_service.ListServiceLevelObjectivesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service_service.ListServiceLevelObjectivesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_service_level_objectives(parent="parent_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_service_level_objectives_flattened_error_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_service_level_objectives(
            service_service.ListServiceLevelObjectivesRequest(), parent="parent_value",
        )


def test_list_service_level_objectives_pager(transport_name: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials, transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_service_level_objectives), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[
                    service.ServiceLevelObjective(),
                    service.ServiceLevelObjective(),
                    service.ServiceLevelObjective(),
                ],
                next_page_token="abc",
            ),
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[], next_page_token="def",
            ),
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[service.ServiceLevelObjective(),],
                next_page_token="ghi",
            ),
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[
                    service.ServiceLevelObjective(),
                    service.ServiceLevelObjective(),
                ],
            ),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_service_level_objectives(request={})

        assert pager._metadata == metadata

        results = [i for i in pager]
        assert len(results) == 6
        assert all(isinstance(i, service.ServiceLevelObjective) for i in results)


def test_list_service_level_objectives_pages(transport_name: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials, transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_service_level_objectives), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[
                    service.ServiceLevelObjective(),
                    service.ServiceLevelObjective(),
                    service.ServiceLevelObjective(),
                ],
                next_page_token="abc",
            ),
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[], next_page_token="def",
            ),
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[service.ServiceLevelObjective(),],
                next_page_token="ghi",
            ),
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[
                    service.ServiceLevelObjective(),
                    service.ServiceLevelObjective(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_service_level_objectives(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_service_level_objectives_async_pager():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_service_level_objectives),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[
                    service.ServiceLevelObjective(),
                    service.ServiceLevelObjective(),
                    service.ServiceLevelObjective(),
                ],
                next_page_token="abc",
            ),
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[], next_page_token="def",
            ),
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[service.ServiceLevelObjective(),],
                next_page_token="ghi",
            ),
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[
                    service.ServiceLevelObjective(),
                    service.ServiceLevelObjective(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_service_level_objectives(request={},)
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, service.ServiceLevelObjective) for i in responses)


@pytest.mark.asyncio
async def test_list_service_level_objectives_async_pages():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_service_level_objectives),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[
                    service.ServiceLevelObjective(),
                    service.ServiceLevelObjective(),
                    service.ServiceLevelObjective(),
                ],
                next_page_token="abc",
            ),
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[], next_page_token="def",
            ),
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[service.ServiceLevelObjective(),],
                next_page_token="ghi",
            ),
            service_service.ListServiceLevelObjectivesResponse(
                service_level_objectives=[
                    service.ServiceLevelObjective(),
                    service.ServiceLevelObjective(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.list_service_level_objectives(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type", [service_service.UpdateServiceLevelObjectiveRequest, dict,]
)
def test_update_service_level_objective(request_type, transport: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ServiceLevelObjective(
            name="name_value",
            display_name="display_name_value",
            goal=0.419,
            rolling_period=duration_pb2.Duration(seconds=751),
        )
        response = client.update_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.UpdateServiceLevelObjectiveRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ServiceLevelObjective)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert math.isclose(response.goal, 0.419, rel_tol=1e-6)


def test_update_service_level_objective_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_service_level_objective), "__call__"
    ) as call:
        client.update_service_level_objective()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.UpdateServiceLevelObjectiveRequest()


@pytest.mark.asyncio
async def test_update_service_level_objective_async(
    transport: str = "grpc_asyncio",
    request_type=service_service.UpdateServiceLevelObjectiveRequest,
):
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ServiceLevelObjective(
                name="name_value", display_name="display_name_value", goal=0.419,
            )
        )
        response = await client.update_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.UpdateServiceLevelObjectiveRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, service.ServiceLevelObjective)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert math.isclose(response.goal, 0.419, rel_tol=1e-6)


@pytest.mark.asyncio
async def test_update_service_level_objective_async_from_dict():
    await test_update_service_level_objective_async(request_type=dict)


def test_update_service_level_objective_field_headers():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.UpdateServiceLevelObjectiveRequest()

    request.service_level_objective.name = "service_level_objective.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_service_level_objective), "__call__"
    ) as call:
        call.return_value = service.ServiceLevelObjective()
        client.update_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "service_level_objective.name=service_level_objective.name/value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_service_level_objective_field_headers_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.UpdateServiceLevelObjectiveRequest()

    request.service_level_objective.name = "service_level_objective.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_service_level_objective), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ServiceLevelObjective()
        )
        await client.update_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "service_level_objective.name=service_level_objective.name/value",
    ) in kw["metadata"]


def test_update_service_level_objective_flattened():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ServiceLevelObjective()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_service_level_objective(
            service_level_objective=service.ServiceLevelObjective(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].service_level_objective
        mock_val = service.ServiceLevelObjective(name="name_value")
        assert arg == mock_val


def test_update_service_level_objective_flattened_error():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_service_level_objective(
            service_service.UpdateServiceLevelObjectiveRequest(),
            service_level_objective=service.ServiceLevelObjective(name="name_value"),
        )


@pytest.mark.asyncio
async def test_update_service_level_objective_flattened_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = service.ServiceLevelObjective()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            service.ServiceLevelObjective()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_service_level_objective(
            service_level_objective=service.ServiceLevelObjective(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].service_level_objective
        mock_val = service.ServiceLevelObjective(name="name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_service_level_objective_flattened_error_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_service_level_objective(
            service_service.UpdateServiceLevelObjectiveRequest(),
            service_level_objective=service.ServiceLevelObjective(name="name_value"),
        )


@pytest.mark.parametrize(
    "request_type", [service_service.DeleteServiceLevelObjectiveRequest, dict,]
)
def test_delete_service_level_objective(request_type, transport: str = "grpc"):
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.DeleteServiceLevelObjectiveRequest()

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_service_level_objective_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_service_level_objective), "__call__"
    ) as call:
        client.delete_service_level_objective()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.DeleteServiceLevelObjectiveRequest()


@pytest.mark.asyncio
async def test_delete_service_level_objective_async(
    transport: str = "grpc_asyncio",
    request_type=service_service.DeleteServiceLevelObjectiveRequest,
):
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == service_service.DeleteServiceLevelObjectiveRequest()

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.asyncio
async def test_delete_service_level_objective_async_from_dict():
    await test_delete_service_level_objective_async(request_type=dict)


def test_delete_service_level_objective_field_headers():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.DeleteServiceLevelObjectiveRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_service_level_objective), "__call__"
    ) as call:
        call.return_value = None
        client.delete_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_service_level_objective_field_headers_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = service_service.DeleteServiceLevelObjectiveRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_service_level_objective), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_service_level_objective(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_delete_service_level_objective_flattened():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_service_level_objective(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_service_level_objective_flattened_error():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_service_level_objective(
            service_service.DeleteServiceLevelObjectiveRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_service_level_objective_flattened_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_service_level_objective), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_service_level_objective(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_delete_service_level_objective_flattened_error_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_service_level_objective(
            service_service.DeleteServiceLevelObjectiveRequest(), name="name_value",
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.ServiceMonitoringServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ServiceMonitoringServiceClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.ServiceMonitoringServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ServiceMonitoringServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.ServiceMonitoringServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = ServiceMonitoringServiceClient(
            client_options=options, transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = mock.Mock()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = ServiceMonitoringServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.ServiceMonitoringServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ServiceMonitoringServiceClient(
            client_options={"scopes": ["1", "2"]}, transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.ServiceMonitoringServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = ServiceMonitoringServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.ServiceMonitoringServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.ServiceMonitoringServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.ServiceMonitoringServiceGrpcTransport,
        transports.ServiceMonitoringServiceGrpcAsyncIOTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport, transports.ServiceMonitoringServiceGrpcTransport,
    )


def test_service_monitoring_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.ServiceMonitoringServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_service_monitoring_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.monitoring_v3.services.service_monitoring_service.transports.ServiceMonitoringServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.ServiceMonitoringServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "create_service",
        "get_service",
        "list_services",
        "update_service",
        "delete_service",
        "create_service_level_objective",
        "get_service_level_objective",
        "list_service_level_objectives",
        "update_service_level_objective",
        "delete_service_level_objective",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()


def test_service_monitoring_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch(
        "google.cloud.monitoring_v3.services.service_monitoring_service.transports.ServiceMonitoringServiceTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.ServiceMonitoringServiceTransport(
            credentials_file="credentials.json", quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/monitoring",
                "https://www.googleapis.com/auth/monitoring.read",
            ),
            quota_project_id="octopus",
        )


def test_service_monitoring_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch(
        "google.cloud.monitoring_v3.services.service_monitoring_service.transports.ServiceMonitoringServiceTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.ServiceMonitoringServiceTransport()
        adc.assert_called_once()


def test_service_monitoring_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        ServiceMonitoringServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/monitoring",
                "https://www.googleapis.com/auth/monitoring.read",
            ),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.ServiceMonitoringServiceGrpcTransport,
        transports.ServiceMonitoringServiceGrpcAsyncIOTransport,
    ],
)
def test_service_monitoring_service_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/monitoring",
                "https://www.googleapis.com/auth/monitoring.read",
            ),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.ServiceMonitoringServiceGrpcTransport, grpc_helpers),
        (transports.ServiceMonitoringServiceGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_service_monitoring_service_transport_create_channel(
    transport_class, grpc_helpers
):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel", autospec=True
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        adc.return_value = (creds, None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])

        create_channel.assert_called_with(
            "monitoring.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/monitoring",
                "https://www.googleapis.com/auth/monitoring.read",
            ),
            scopes=["1", "2"],
            default_host="monitoring.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.ServiceMonitoringServiceGrpcTransport,
        transports.ServiceMonitoringServiceGrpcAsyncIOTransport,
    ],
)
def test_service_monitoring_service_grpc_transport_client_cert_source_for_mtls(
    transport_class,
):
    cred = ga_credentials.AnonymousCredentials()

    # Check ssl_channel_credentials is used if provided.
    with mock.patch.object(transport_class, "create_channel") as mock_create_channel:
        mock_ssl_channel_creds = mock.Mock()
        transport_class(
            host="squid.clam.whelk",
            credentials=cred,
            ssl_channel_credentials=mock_ssl_channel_creds,
        )
        mock_create_channel.assert_called_once_with(
            "squid.clam.whelk:443",
            credentials=cred,
            credentials_file=None,
            scopes=None,
            ssl_credentials=mock_ssl_channel_creds,
            quota_project_id=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )

    # Check if ssl_channel_credentials is not provided, then client_cert_source_for_mtls
    # is used.
    with mock.patch.object(transport_class, "create_channel", return_value=mock.Mock()):
        with mock.patch("grpc.ssl_channel_credentials") as mock_ssl_cred:
            transport_class(
                credentials=cred,
                client_cert_source_for_mtls=client_cert_source_callback,
            )
            expected_cert, expected_key = client_cert_source_callback()
            mock_ssl_cred.assert_called_once_with(
                certificate_chain=expected_cert, private_key=expected_key
            )


def test_service_monitoring_service_host_no_port():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="monitoring.googleapis.com"
        ),
    )
    assert client.transport._host == "monitoring.googleapis.com:443"


def test_service_monitoring_service_host_with_port():
    client = ServiceMonitoringServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="monitoring.googleapis.com:8000"
        ),
    )
    assert client.transport._host == "monitoring.googleapis.com:8000"


def test_service_monitoring_service_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.ServiceMonitoringServiceGrpcTransport(
        host="squid.clam.whelk", channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_service_monitoring_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.ServiceMonitoringServiceGrpcAsyncIOTransport(
        host="squid.clam.whelk", channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize(
    "transport_class",
    [
        transports.ServiceMonitoringServiceGrpcTransport,
        transports.ServiceMonitoringServiceGrpcAsyncIOTransport,
    ],
)
def test_service_monitoring_service_transport_channel_mtls_with_client_cert_source(
    transport_class,
):
    with mock.patch(
        "grpc.ssl_channel_credentials", autospec=True
    ) as grpc_ssl_channel_cred:
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = ga_credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(google.auth, "default") as adc:
                    adc.return_value = (cred, None)
                    transport = transport_class(
                        host="squid.clam.whelk",
                        api_mtls_endpoint="mtls.squid.clam.whelk",
                        client_cert_source=client_cert_source_callback,
                    )
                    adc.assert_called_once()

            grpc_ssl_channel_cred.assert_called_once_with(
                certificate_chain=b"cert bytes", private_key=b"key bytes"
            )
            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel
            assert transport._ssl_channel_credentials == mock_ssl_cred


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize(
    "transport_class",
    [
        transports.ServiceMonitoringServiceGrpcTransport,
        transports.ServiceMonitoringServiceGrpcAsyncIOTransport,
    ],
)
def test_service_monitoring_service_transport_channel_mtls_with_adc(transport_class):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel
            mock_cred = mock.Mock()

            with pytest.warns(DeprecationWarning):
                transport = transport_class(
                    host="squid.clam.whelk",
                    credentials=mock_cred,
                    api_mtls_endpoint="mtls.squid.clam.whelk",
                    client_cert_source=None,
                )

            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=mock_cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel


def test_service_path():
    project = "squid"
    service = "clam"
    expected = "projects/{project}/services/{service}".format(
        project=project, service=service,
    )
    actual = ServiceMonitoringServiceClient.service_path(project, service)
    assert expected == actual


def test_parse_service_path():
    expected = {
        "project": "whelk",
        "service": "octopus",
    }
    path = ServiceMonitoringServiceClient.service_path(**expected)

    # Check that the path construction is reversible.
    actual = ServiceMonitoringServiceClient.parse_service_path(path)
    assert expected == actual


def test_service_level_objective_path():
    project = "oyster"
    service = "nudibranch"
    service_level_objective = "cuttlefish"
    expected = "projects/{project}/services/{service}/serviceLevelObjectives/{service_level_objective}".format(
        project=project,
        service=service,
        service_level_objective=service_level_objective,
    )
    actual = ServiceMonitoringServiceClient.service_level_objective_path(
        project, service, service_level_objective
    )
    assert expected == actual


def test_parse_service_level_objective_path():
    expected = {
        "project": "mussel",
        "service": "winkle",
        "service_level_objective": "nautilus",
    }
    path = ServiceMonitoringServiceClient.service_level_objective_path(**expected)

    # Check that the path construction is reversible.
    actual = ServiceMonitoringServiceClient.parse_service_level_objective_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "scallop"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = ServiceMonitoringServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "abalone",
    }
    path = ServiceMonitoringServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = ServiceMonitoringServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "squid"
    expected = "folders/{folder}".format(folder=folder,)
    actual = ServiceMonitoringServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "clam",
    }
    path = ServiceMonitoringServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = ServiceMonitoringServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "whelk"
    expected = "organizations/{organization}".format(organization=organization,)
    actual = ServiceMonitoringServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "octopus",
    }
    path = ServiceMonitoringServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = ServiceMonitoringServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "oyster"
    expected = "projects/{project}".format(project=project,)
    actual = ServiceMonitoringServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "nudibranch",
    }
    path = ServiceMonitoringServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = ServiceMonitoringServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "cuttlefish"
    location = "mussel"
    expected = "projects/{project}/locations/{location}".format(
        project=project, location=location,
    )
    actual = ServiceMonitoringServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "winkle",
        "location": "nautilus",
    }
    path = ServiceMonitoringServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = ServiceMonitoringServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.ServiceMonitoringServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = ServiceMonitoringServiceClient(
            credentials=ga_credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.ServiceMonitoringServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = ServiceMonitoringServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


@pytest.mark.asyncio
async def test_transport_close_async():
    client = ServiceMonitoringServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc_asyncio",
    )
    with mock.patch.object(
        type(getattr(client.transport, "grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close():
    transports = {
        "grpc": "_grpc_channel",
    }

    for transport, close_name in transports.items():
        client = ServiceMonitoringServiceClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        with mock.patch.object(
            type(getattr(client.transport, close_name)), "close"
        ) as close:
            with client:
                close.assert_not_called()
            close.assert_called_once()


def test_client_ctx():
    transports = [
        "grpc",
    ]
    for transport in transports:
        client = ServiceMonitoringServiceClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()


@pytest.mark.parametrize(
    "client_class,transport_class",
    [
        (
            ServiceMonitoringServiceClient,
            transports.ServiceMonitoringServiceGrpcTransport,
        ),
        (
            ServiceMonitoringServiceAsyncClient,
            transports.ServiceMonitoringServiceGrpcAsyncIOTransport,
        ),
    ],
)
def test_api_key_credentials(client_class, transport_class):
    with mock.patch.object(
        google.auth._default, "get_api_key_credentials", create=True
    ) as get_api_key_credentials:
        mock_cred = mock.Mock()
        get_api_key_credentials.return_value = mock_cred
        options = client_options.ClientOptions()
        options.api_key = "api_key"
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options)
            patched.assert_called_once_with(
                credentials=mock_cred,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )
