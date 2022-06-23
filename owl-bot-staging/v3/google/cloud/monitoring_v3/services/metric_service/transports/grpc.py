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
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers
from google.api_core import gapic_v1
import google.auth                         # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.api import metric_pb2  # type: ignore
from google.api import monitored_resource_pb2  # type: ignore
from google.cloud.monitoring_v3.types import metric_service
from google.protobuf import empty_pb2  # type: ignore
from .base import MetricServiceTransport, DEFAULT_CLIENT_INFO


class MetricServiceGrpcTransport(MetricServiceTransport):
    """gRPC backend transport for MetricService.

    Manages metric descriptors, monitored resource descriptors,
    and time series data.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    _stubs: Dict[str, Callable]

    def __init__(self, *,
            host: str = 'monitoring.googleapis.com',
            credentials: ga_credentials.Credentials = None,
            credentials_file: str = None,
            scopes: Sequence[str] = None,
            channel: grpc.Channel = None,
            api_mtls_endpoint: str = None,
            client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
            ssl_channel_credentials: grpc.ChannelCredentials = None,
            client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(cls,
                       host: str = 'monitoring.googleapis.com',
                       credentials: ga_credentials.Credentials = None,
                       credentials_file: str = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def list_monitored_resource_descriptors(self) -> Callable[
            [metric_service.ListMonitoredResourceDescriptorsRequest],
            metric_service.ListMonitoredResourceDescriptorsResponse]:
        r"""Return a callable for the list monitored resource
        descriptors method over gRPC.

        Lists monitored resource descriptors that match a
        filter. This method does not require a Workspace.

        Returns:
            Callable[[~.ListMonitoredResourceDescriptorsRequest],
                    ~.ListMonitoredResourceDescriptorsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_monitored_resource_descriptors' not in self._stubs:
            self._stubs['list_monitored_resource_descriptors'] = self.grpc_channel.unary_unary(
                '/google.monitoring.v3.MetricService/ListMonitoredResourceDescriptors',
                request_serializer=metric_service.ListMonitoredResourceDescriptorsRequest.serialize,
                response_deserializer=metric_service.ListMonitoredResourceDescriptorsResponse.deserialize,
            )
        return self._stubs['list_monitored_resource_descriptors']

    @property
    def get_monitored_resource_descriptor(self) -> Callable[
            [metric_service.GetMonitoredResourceDescriptorRequest],
            monitored_resource_pb2.MonitoredResourceDescriptor]:
        r"""Return a callable for the get monitored resource
        descriptor method over gRPC.

        Gets a single monitored resource descriptor. This
        method does not require a Workspace.

        Returns:
            Callable[[~.GetMonitoredResourceDescriptorRequest],
                    ~.MonitoredResourceDescriptor]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_monitored_resource_descriptor' not in self._stubs:
            self._stubs['get_monitored_resource_descriptor'] = self.grpc_channel.unary_unary(
                '/google.monitoring.v3.MetricService/GetMonitoredResourceDescriptor',
                request_serializer=metric_service.GetMonitoredResourceDescriptorRequest.serialize,
                response_deserializer=monitored_resource_pb2.MonitoredResourceDescriptor.FromString,
            )
        return self._stubs['get_monitored_resource_descriptor']

    @property
    def list_metric_descriptors(self) -> Callable[
            [metric_service.ListMetricDescriptorsRequest],
            metric_service.ListMetricDescriptorsResponse]:
        r"""Return a callable for the list metric descriptors method over gRPC.

        Lists metric descriptors that match a filter. This
        method does not require a Workspace.

        Returns:
            Callable[[~.ListMetricDescriptorsRequest],
                    ~.ListMetricDescriptorsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_metric_descriptors' not in self._stubs:
            self._stubs['list_metric_descriptors'] = self.grpc_channel.unary_unary(
                '/google.monitoring.v3.MetricService/ListMetricDescriptors',
                request_serializer=metric_service.ListMetricDescriptorsRequest.serialize,
                response_deserializer=metric_service.ListMetricDescriptorsResponse.deserialize,
            )
        return self._stubs['list_metric_descriptors']

    @property
    def get_metric_descriptor(self) -> Callable[
            [metric_service.GetMetricDescriptorRequest],
            metric_pb2.MetricDescriptor]:
        r"""Return a callable for the get metric descriptor method over gRPC.

        Gets a single metric descriptor. This method does not
        require a Workspace.

        Returns:
            Callable[[~.GetMetricDescriptorRequest],
                    ~.MetricDescriptor]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_metric_descriptor' not in self._stubs:
            self._stubs['get_metric_descriptor'] = self.grpc_channel.unary_unary(
                '/google.monitoring.v3.MetricService/GetMetricDescriptor',
                request_serializer=metric_service.GetMetricDescriptorRequest.serialize,
                response_deserializer=metric_pb2.MetricDescriptor.FromString,
            )
        return self._stubs['get_metric_descriptor']

    @property
    def create_metric_descriptor(self) -> Callable[
            [metric_service.CreateMetricDescriptorRequest],
            metric_pb2.MetricDescriptor]:
        r"""Return a callable for the create metric descriptor method over gRPC.

        Creates a new metric descriptor. The creation is executed
        asynchronously and callers may check the returned operation to
        track its progress. User-created metric descriptors define
        `custom
        metrics <https://cloud.google.com/monitoring/custom-metrics>`__.

        Returns:
            Callable[[~.CreateMetricDescriptorRequest],
                    ~.MetricDescriptor]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_metric_descriptor' not in self._stubs:
            self._stubs['create_metric_descriptor'] = self.grpc_channel.unary_unary(
                '/google.monitoring.v3.MetricService/CreateMetricDescriptor',
                request_serializer=metric_service.CreateMetricDescriptorRequest.serialize,
                response_deserializer=metric_pb2.MetricDescriptor.FromString,
            )
        return self._stubs['create_metric_descriptor']

    @property
    def delete_metric_descriptor(self) -> Callable[
            [metric_service.DeleteMetricDescriptorRequest],
            empty_pb2.Empty]:
        r"""Return a callable for the delete metric descriptor method over gRPC.

        Deletes a metric descriptor. Only user-created `custom
        metrics <https://cloud.google.com/monitoring/custom-metrics>`__
        can be deleted.

        Returns:
            Callable[[~.DeleteMetricDescriptorRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_metric_descriptor' not in self._stubs:
            self._stubs['delete_metric_descriptor'] = self.grpc_channel.unary_unary(
                '/google.monitoring.v3.MetricService/DeleteMetricDescriptor',
                request_serializer=metric_service.DeleteMetricDescriptorRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['delete_metric_descriptor']

    @property
    def list_time_series(self) -> Callable[
            [metric_service.ListTimeSeriesRequest],
            metric_service.ListTimeSeriesResponse]:
        r"""Return a callable for the list time series method over gRPC.

        Lists time series that match a filter. This method
        does not require a Workspace.

        Returns:
            Callable[[~.ListTimeSeriesRequest],
                    ~.ListTimeSeriesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_time_series' not in self._stubs:
            self._stubs['list_time_series'] = self.grpc_channel.unary_unary(
                '/google.monitoring.v3.MetricService/ListTimeSeries',
                request_serializer=metric_service.ListTimeSeriesRequest.serialize,
                response_deserializer=metric_service.ListTimeSeriesResponse.deserialize,
            )
        return self._stubs['list_time_series']

    @property
    def create_time_series(self) -> Callable[
            [metric_service.CreateTimeSeriesRequest],
            empty_pb2.Empty]:
        r"""Return a callable for the create time series method over gRPC.

        Creates or adds data to one or more time series.
        The response is empty if all time series in the request
        were written. If any time series could not be written, a
        corresponding failure message is included in the error
        response.

        Returns:
            Callable[[~.CreateTimeSeriesRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_time_series' not in self._stubs:
            self._stubs['create_time_series'] = self.grpc_channel.unary_unary(
                '/google.monitoring.v3.MetricService/CreateTimeSeries',
                request_serializer=metric_service.CreateTimeSeriesRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['create_time_series']

    @property
    def create_service_time_series(self) -> Callable[
            [metric_service.CreateTimeSeriesRequest],
            empty_pb2.Empty]:
        r"""Return a callable for the create service time series method over gRPC.

        Creates or adds data to one or more service time series. A
        service time series is a time series for a metric from a Google
        Cloud service. The response is empty if all time series in the
        request were written. If any time series could not be written, a
        corresponding failure message is included in the error response.
        This endpoint rejects writes to user-defined metrics. This
        method is only for use by Google Cloud services. Use
        [projects.timeSeries.create][google.monitoring.v3.MetricService.CreateTimeSeries]
        instead.

        Returns:
            Callable[[~.CreateTimeSeriesRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_service_time_series' not in self._stubs:
            self._stubs['create_service_time_series'] = self.grpc_channel.unary_unary(
                '/google.monitoring.v3.MetricService/CreateServiceTimeSeries',
                request_serializer=metric_service.CreateTimeSeriesRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['create_service_time_series']

    def close(self):
        self.grpc_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = (
    'MetricServiceGrpcTransport',
)
