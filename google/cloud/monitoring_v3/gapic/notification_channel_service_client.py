# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Accesses the google.monitoring.v3 NotificationChannelService API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.api import metric_pb2 as api_metric_pb2
from google.api import monitored_resource_pb2
from google.cloud.monitoring_v3.gapic import enums
from google.cloud.monitoring_v3.gapic import notification_channel_service_client_config
from google.cloud.monitoring_v3.gapic.transports import (
    notification_channel_service_grpc_transport,
)
from google.cloud.monitoring_v3.proto import alert_pb2
from google.cloud.monitoring_v3.proto import alert_service_pb2
from google.cloud.monitoring_v3.proto import alert_service_pb2_grpc
from google.cloud.monitoring_v3.proto import common_pb2
from google.cloud.monitoring_v3.proto import group_pb2
from google.cloud.monitoring_v3.proto import group_service_pb2
from google.cloud.monitoring_v3.proto import group_service_pb2_grpc
from google.cloud.monitoring_v3.proto import metric_pb2 as proto_metric_pb2
from google.cloud.monitoring_v3.proto import metric_service_pb2
from google.cloud.monitoring_v3.proto import metric_service_pb2_grpc
from google.cloud.monitoring_v3.proto import notification_pb2
from google.cloud.monitoring_v3.proto import notification_service_pb2
from google.cloud.monitoring_v3.proto import notification_service_pb2_grpc
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import timestamp_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-monitoring"
).version


class NotificationChannelServiceClient(object):
    """
    The Notification Channel API provides access to configuration that
    controls how messages related to incidents are sent.
    """

    SERVICE_ADDRESS = "monitoring.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.monitoring.v3.NotificationChannelService"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            NotificationChannelServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def notification_channel_path(cls, project, notification_channel):
        """Return a fully-qualified notification_channel string."""
        return google.api_core.path_template.expand(
            "projects/{project}/notificationChannels/{notification_channel}",
            project=project,
            notification_channel=notification_channel,
        )

    @classmethod
    def notification_channel_descriptor_path(cls, project, channel_descriptor):
        """Return a fully-qualified notification_channel_descriptor string."""
        return google.api_core.path_template.expand(
            "projects/{project}/notificationChannelDescriptors/{channel_descriptor}",
            project=project,
            channel_descriptor=channel_descriptor,
        )

    @classmethod
    def project_path(cls, project):
        """Return a fully-qualified project string."""
        return google.api_core.path_template.expand(
            "projects/{project}", project=project
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.NotificationChannelServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.NotificationChannelServiceGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = notification_channel_service_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=notification_channel_service_grpc_transport.NotificationChannelServiceGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = notification_channel_service_grpc_transport.NotificationChannelServiceGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def list_notification_channel_descriptors(
        self,
        name,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists the descriptors for supported channel types. The use of descriptors
        makes it possible for new channel types to be dynamically added.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.NotificationChannelServiceClient()
            >>>
            >>> name = client.project_path('[PROJECT]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_notification_channel_descriptors(name):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_notification_channel_descriptors(name).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            name (str): The ``UpdateServiceLevelObjective`` request.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.monitoring_v3.types.NotificationChannelDescriptor` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        # Wrap the transport method to add retry and timeout logic.
        if "list_notification_channel_descriptors" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_notification_channel_descriptors"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_notification_channel_descriptors,
                default_retry=self._method_configs[
                    "ListNotificationChannelDescriptors"
                ].retry,
                default_timeout=self._method_configs[
                    "ListNotificationChannelDescriptors"
                ].timeout,
                client_info=self._client_info,
            )

        request = notification_service_pb2.ListNotificationChannelDescriptorsRequest(
            name=name, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_notification_channel_descriptors"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="channel_descriptors",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def get_notification_channel_descriptor(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a single channel descriptor. The descriptor indicates which fields
        are expected / permitted for a notification channel of the given type.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.NotificationChannelServiceClient()
            >>>
            >>> name = client.notification_channel_descriptor_path('[PROJECT]', '[CHANNEL_DESCRIPTOR]')
            >>>
            >>> response = client.get_notification_channel_descriptor(name)

        Args:
            name (str): Auxiliary metadata for a ``MonitoredResource`` object.
                ``MonitoredResource`` objects contain the minimum set of information to
                uniquely identify a monitored resource instance. There is some other
                useful auxiliary metadata. Monitoring and Logging use an ingestion
                pipeline to extract metadata for cloud resources of all types, and store
                the metadata in this message.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.monitoring_v3.types.NotificationChannelDescriptor` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        # Wrap the transport method to add retry and timeout logic.
        if "get_notification_channel_descriptor" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_notification_channel_descriptor"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_notification_channel_descriptor,
                default_retry=self._method_configs[
                    "GetNotificationChannelDescriptor"
                ].retry,
                default_timeout=self._method_configs[
                    "GetNotificationChannelDescriptor"
                ].timeout,
                client_info=self._client_info,
            )

        request = notification_service_pb2.GetNotificationChannelDescriptorRequest(
            name=name
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_notification_channel_descriptor"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_notification_channels(
        self,
        name,
        filter_=None,
        order_by=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists the notification channels that have been created for the project.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.NotificationChannelServiceClient()
            >>>
            >>> name = client.project_path('[PROJECT]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_notification_channels(name):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_notification_channels(name).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            name (str): The maximum number of results to return in a single response. The
                server may further constrain the maximum number of results returned in a
                single page. If the page_size is <=0, the server will decide the number
                of results to be returned.
            filter_ (str): The ``ListServices`` request.
            order_by (str): Reduce by computing the `5th
                percentile <https://en.wikipedia.org/wiki/Percentile>`__ of data points
                across time series for each alignment period. This reducer is valid for
                ``GAUGE`` and ``DELTA`` metrics of numeric and distribution type. The
                value of the output is ``DOUBLE``.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.monitoring_v3.types.NotificationChannel` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        # Wrap the transport method to add retry and timeout logic.
        if "list_notification_channels" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_notification_channels"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_notification_channels,
                default_retry=self._method_configs["ListNotificationChannels"].retry,
                default_timeout=self._method_configs[
                    "ListNotificationChannels"
                ].timeout,
                client_info=self._client_info,
            )

        request = notification_service_pb2.ListNotificationChannelsRequest(
            name=name, filter=filter_, order_by=order_by, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_notification_channels"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="notification_channels",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def get_notification_channel(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a single notification channel. The channel includes the relevant
        configuration details with which the channel was created. However, the
        response may truncate or omit passwords, API keys, or other private key
        matter and thus the response may not be 100% identical to the information
        that was supplied in the call to the create method.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.NotificationChannelServiceClient()
            >>>
            >>> name = client.notification_channel_path('[PROJECT]', '[NOTIFICATION_CHANNEL]')
            >>>
            >>> response = client.get_notification_channel(name)

        Args:
            name (str): The ``alignment_period`` specifies a time interval, in seconds, that
                is used to divide the data in all the ``time series`` into consistent
                blocks of time. This will be done before the per-series aligner can be
                applied to the data.

                The value must be at least 60 seconds. If a per-series aligner other
                than ``ALIGN_NONE`` is specified, this field is required or an error is
                returned. If no per-series aligner is specified, or the aligner
                ``ALIGN_NONE`` is specified, then this field is ignored.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.monitoring_v3.types.NotificationChannel` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        # Wrap the transport method to add retry and timeout logic.
        if "get_notification_channel" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_notification_channel"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_notification_channel,
                default_retry=self._method_configs["GetNotificationChannel"].retry,
                default_timeout=self._method_configs["GetNotificationChannel"].timeout,
                client_info=self._client_info,
            )

        request = notification_service_pb2.GetNotificationChannelRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_notification_channel"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_notification_channel(
        self,
        name,
        notification_channel,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a new notification channel, representing a single notification
        endpoint such as an email address, SMS number, or PagerDuty service.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.NotificationChannelServiceClient()
            >>>
            >>> name = client.project_path('[PROJECT]')
            >>>
            >>> # TODO: Initialize `notification_channel`:
            >>> notification_channel = {}
            >>>
            >>> response = client.create_notification_channel(name, notification_channel)

        Args:
            name (str): Reduce by computing the `50th
                percentile <https://en.wikipedia.org/wiki/Percentile>`__ of data points
                across time series for each alignment period. This reducer is valid for
                ``GAUGE`` and ``DELTA`` metrics of numeric and distribution type. The
                value of the output is ``DOUBLE``.
            notification_channel (Union[dict, ~google.cloud.monitoring_v3.types.NotificationChannel]): Header options corresponding to the Content-Type of the body in HTTP
                requests. Note that a ``Content-Type`` header cannot be present in the
                ``headers`` field if this field is specified.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.monitoring_v3.types.NotificationChannel`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.monitoring_v3.types.NotificationChannel` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        # Wrap the transport method to add retry and timeout logic.
        if "create_notification_channel" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_notification_channel"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_notification_channel,
                default_retry=self._method_configs["CreateNotificationChannel"].retry,
                default_timeout=self._method_configs[
                    "CreateNotificationChannel"
                ].timeout,
                client_info=self._client_info,
            )

        request = notification_service_pb2.CreateNotificationChannelRequest(
            name=name, notification_channel=notification_channel
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_notification_channel"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_notification_channel(
        self,
        notification_channel,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates a notification channel. Fields not specified in the field mask
        remain unchanged.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.NotificationChannelServiceClient()
            >>>
            >>> # TODO: Initialize `notification_channel`:
            >>> notification_channel = {}
            >>>
            >>> response = client.update_notification_channel(notification_channel)

        Args:
            notification_channel (Union[dict, ~google.cloud.monitoring_v3.types.NotificationChannel]): OAuth scopes needed for the client.

                Example:

                | service Foo { option (google.api.oauth_scopes) =
                | "https://www.googleapis.com/auth/cloud-platform"; ... }

                If there is more than one scope, use a comma-separated string:

                Example:

                | service Foo { option (google.api.oauth_scopes) =
                | "https://www.googleapis.com/auth/cloud-platform,"
                  "https://www.googleapis.com/auth/monitoring"; ... }

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.monitoring_v3.types.NotificationChannel`
            update_mask (Union[dict, ~google.cloud.monitoring_v3.types.FieldMask]): The fields to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.monitoring_v3.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.monitoring_v3.types.NotificationChannel` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        # Wrap the transport method to add retry and timeout logic.
        if "update_notification_channel" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_notification_channel"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_notification_channel,
                default_retry=self._method_configs["UpdateNotificationChannel"].retry,
                default_timeout=self._method_configs[
                    "UpdateNotificationChannel"
                ].timeout,
                client_info=self._client_info,
            )

        request = notification_service_pb2.UpdateNotificationChannelRequest(
            notification_channel=notification_channel, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("notification_channel.name", notification_channel.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_notification_channel"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_notification_channel(
        self,
        name,
        force=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a notification channel.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.NotificationChannelServiceClient()
            >>>
            >>> name = client.notification_channel_path('[PROJECT]', '[NOTIFICATION_CHANNEL]')
            >>>
            >>> client.delete_notification_channel(name)

        Args:
            name (str): The protocol for the ``CreateUptimeCheckConfig`` request.
            force (bool): If true, the notification channel will be deleted regardless of its
                use in alert policies (the policies will be updated to remove the
                channel). If false, channels that are still referenced by an existing
                alerting policy will fail to be deleted in a delete operation.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        # Wrap the transport method to add retry and timeout logic.
        if "delete_notification_channel" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_notification_channel"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_notification_channel,
                default_retry=self._method_configs["DeleteNotificationChannel"].retry,
                default_timeout=self._method_configs[
                    "DeleteNotificationChannel"
                ].timeout,
                client_info=self._client_info,
            )

        request = notification_service_pb2.DeleteNotificationChannelRequest(
            name=name, force=force
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_notification_channel"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def send_notification_channel_verification_code(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Reduce by computing the number of ``False``-valued data points
        across time series for each alignment period. This reducer is valid for
        ``DELTA`` and ``GAUGE`` metrics of Boolean ``value_type``. The
        ``value_type`` of the output is ``INT64``.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.NotificationChannelServiceClient()
            >>>
            >>> name = client.notification_channel_path('[PROJECT]', '[NOTIFICATION_CHANNEL]')
            >>>
            >>> client.send_notification_channel_verification_code(name)

        Args:
            name (str): Required. The notification channel to which to send a verification code.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        # Wrap the transport method to add retry and timeout logic.
        if "send_notification_channel_verification_code" not in self._inner_api_calls:
            self._inner_api_calls[
                "send_notification_channel_verification_code"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.send_notification_channel_verification_code,
                default_retry=self._method_configs[
                    "SendNotificationChannelVerificationCode"
                ].retry,
                default_timeout=self._method_configs[
                    "SendNotificationChannelVerificationCode"
                ].timeout,
                client_info=self._client_info,
            )

        request = notification_service_pb2.SendNotificationChannelVerificationCodeRequest(
            name=name
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["send_notification_channel_verification_code"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_notification_channel_verification_code(
        self,
        name,
        expire_time=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Requests a verification code for an already verified channel that can then
        be used in a call to VerifyNotificationChannel() on a different channel
        with an equivalent identity in the same or in a different project. This
        makes it possible to copy a channel between projects without requiring
        manual reverification of the channel. If the channel is not in the
        verified state, this method will fail (in other words, this may only be
        used if the SendNotificationChannelVerificationCode and
        VerifyNotificationChannel paths have already been used to put the given
        channel into the verified state).

        There is no guarantee that the verification codes returned by this method
        will be of a similar structure or form as the ones that are delivered
        to the channel via SendNotificationChannelVerificationCode; while
        VerifyNotificationChannel() will recognize both the codes delivered via
        SendNotificationChannelVerificationCode() and returned from
        GetNotificationChannelVerificationCode(), it is typically the case that
        the verification codes delivered via
        SendNotificationChannelVerificationCode() will be shorter and also
        have a shorter expiration (e.g. codes such as "G-123456") whereas
        GetVerificationCode() will typically return a much longer, websafe base
        64 encoded string that has a longer expiration time.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.NotificationChannelServiceClient()
            >>>
            >>> name = client.notification_channel_path('[PROJECT]', '[NOTIFICATION_CHANNEL]')
            >>>
            >>> response = client.get_notification_channel_verification_code(name)

        Args:
            name (str): Required. The notification channel for which a verification code is to be generated
                and retrieved. This must name a channel that is already verified; if
                the specified channel is not verified, the request will fail.
            expire_time (Union[dict, ~google.cloud.monitoring_v3.types.Timestamp]): The desired expiration time. If specified, the API will guarantee that
                the returned code will not be valid after the specified timestamp;
                however, the API cannot guarantee that the returned code will be
                valid for at least as long as the requested time (the API puts an upper
                bound on the amount of time for which a code may be valid). If omitted,
                a default expiration will be used, which may be less than the max
                permissible expiration (so specifying an expiration may extend the
                code's lifetime over omitting an expiration, even though the API does
                impose an upper limit on the maximum expiration that is permitted).

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.monitoring_v3.types.Timestamp`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.monitoring_v3.types.GetNotificationChannelVerificationCodeResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        # Wrap the transport method to add retry and timeout logic.
        if "get_notification_channel_verification_code" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_notification_channel_verification_code"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_notification_channel_verification_code,
                default_retry=self._method_configs[
                    "GetNotificationChannelVerificationCode"
                ].retry,
                default_timeout=self._method_configs[
                    "GetNotificationChannelVerificationCode"
                ].timeout,
                client_info=self._client_info,
            )

        request = notification_service_pb2.GetNotificationChannelVerificationCodeRequest(
            name=name, expire_time=expire_time
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_notification_channel_verification_code"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def verify_notification_channel(
        self,
        name,
        code,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        An object representing a resource that can be used for monitoring,
        logging, billing, or other purposes. Examples include virtual machine
        instances, databases, and storage devices such as disks. The ``type``
        field identifies a ``MonitoredResourceDescriptor`` object that describes
        the resource's schema. Information in the ``labels`` field identifies
        the actual resource and its attributes according to the schema. For
        example, a particular Compute Engine VM instance could be represented by
        the following object, because the ``MonitoredResourceDescriptor`` for
        ``"gce_instance"`` has labels ``"instance_id"`` and ``"zone"``:

        ::

            { "type": "gce_instance",
              "labels": { "instance_id": "12345678901234",
                          "zone": "us-central1-a" }}

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.NotificationChannelServiceClient()
            >>>
            >>> name = client.notification_channel_path('[PROJECT]', '[NOTIFICATION_CHANNEL]')
            >>>
            >>> # TODO: Initialize `code`:
            >>> code = ''
            >>>
            >>> response = client.verify_notification_channel(name, code)

        Args:
            name (str): Required. The notification channel to verify.
            code (str): Optional (defaults to "/"). The path to the page against which to
                run the check. Will be combined with the ``host`` (specified within the
                ``monitored_resource``) and ``port`` to construct the full URL. If the
                provided path does not begin with "/", a "/" will be prepended
                automatically.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.monitoring_v3.types.NotificationChannel` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        # Wrap the transport method to add retry and timeout logic.
        if "verify_notification_channel" not in self._inner_api_calls:
            self._inner_api_calls[
                "verify_notification_channel"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.verify_notification_channel,
                default_retry=self._method_configs["VerifyNotificationChannel"].retry,
                default_timeout=self._method_configs[
                    "VerifyNotificationChannel"
                ].timeout,
                client_info=self._client_info,
            )

        request = notification_service_pb2.VerifyNotificationChannelRequest(
            name=name, code=code
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["verify_notification_channel"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
