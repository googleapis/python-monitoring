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

"""Accesses the google.monitoring.v3 GroupService API."""

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
import google.api_core.protobuf_helpers
import grpc

from google.cloud.monitoring_v3.gapic import enums
from google.cloud.monitoring_v3.gapic import group_service_client_config
from google.cloud.monitoring_v3.gapic.transports import group_service_grpc_transport
from google.cloud.monitoring_v3.proto import alert_pb2
from google.cloud.monitoring_v3.proto import alert_service_pb2
from google.cloud.monitoring_v3.proto import alert_service_pb2_grpc
from google.cloud.monitoring_v3.proto import common_pb2
from google.cloud.monitoring_v3.proto import group_pb2
from google.cloud.monitoring_v3.proto import group_service_pb2
from google.cloud.monitoring_v3.proto import group_service_pb2_grpc
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-monitoring"
).version


class GroupServiceClient(object):
    """Create a ``Service``."""

    SERVICE_ADDRESS = "monitoring.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.monitoring.v3.GroupService"

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
            GroupServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def group_path(cls, project, group):
        """Return a fully-qualified group string."""
        return google.api_core.path_template.expand(
            "projects/{project}/groups/{group}", project=project, group=group
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
            transport (Union[~.GroupServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.GroupServiceGrpcTransport]): A transport
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
            client_config = group_service_client_config.config

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
                    default_class=group_service_grpc_transport.GroupServiceGrpcTransport,
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
            self.transport = group_service_grpc_transport.GroupServiceGrpcTransport(
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
    def list_groups(
        self,
        name,
        children_of_group=None,
        ancestors_of_group=None,
        descendants_of_group=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists the existing groups.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.GroupServiceClient()
            >>>
            >>> name = client.project_path('[PROJECT]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_groups(name):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_groups(name).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            name (str): Boolean specifying whether to include SSL certificate validation as
                a part of the Uptime check. Only applies to checks where
                ``monitored_resource`` is set to ``uptime_url``. If ``use_ssl`` is
                ``false``, setting ``validate_ssl`` to ``true`` has no effect.
            children_of_group (str): A Boolean value: ``true`` or ``false``.
            ancestors_of_group (str): Resource name for this Service. The format is:

                ::

                    projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]
            descendants_of_group (str): Deprecated features are scheduled to be shut down and removed. For
                more information, see the “Deprecation Policy” section of our `Terms of
                Service <https://cloud.google.com/terms/>`__ and the `Google Cloud
                Platform Subject to the Deprecation
                Policy <https://cloud.google.com/terms/deprecation>`__ documentation.
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
            An iterable of :class:`~google.cloud.monitoring_v3.types.Group` instances.
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
        if "list_groups" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_groups"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_groups,
                default_retry=self._method_configs["ListGroups"].retry,
                default_timeout=self._method_configs["ListGroups"].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            children_of_group=children_of_group,
            ancestors_of_group=ancestors_of_group,
            descendants_of_group=descendants_of_group,
        )

        request = group_service_pb2.ListGroupsRequest(
            name=name,
            children_of_group=children_of_group,
            ancestors_of_group=ancestors_of_group,
            descendants_of_group=descendants_of_group,
            page_size=page_size,
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
                self._inner_api_calls["list_groups"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="group",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def get_group(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a single group.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.GroupServiceClient()
            >>>
            >>> name = client.group_path('[PROJECT]', '[GROUP]')
            >>>
            >>> response = client.get_group(name)

        Args:
            name (str): Optional. The Service id to use for this Service. If omitted, an id
                will be generated instead. Must match the pattern ``[a-z0-9\-]+``
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.monitoring_v3.types.Group` instance.

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
        if "get_group" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_group"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_group,
                default_retry=self._method_configs["GetGroup"].retry,
                default_timeout=self._method_configs["GetGroup"].timeout,
                client_info=self._client_info,
            )

        request = group_service_pb2.GetGroupRequest(name=name)
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

        return self._inner_api_calls["get_group"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_group(
        self,
        name,
        group,
        validate_only=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a new group.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.GroupServiceClient()
            >>>
            >>> name = client.project_path('[PROJECT]')
            >>>
            >>> # TODO: Initialize `group`:
            >>> group = {}
            >>>
            >>> response = client.create_group(name, group)

        Args:
            name (str): The metric kind of the time series. When listing time series, this
                metric kind might be different from the metric kind of the associated
                metric if this time series is an alignment or reduction of other time
                series.

                When creating a time series, this field is optional. If present, it must
                be the same as the metric kind of the associated metric. If the
                associated metric's descriptor must be auto-created, then this field
                specifies the metric kind of the new descriptor and must be either
                ``GAUGE`` (the default) or ``CUMULATIVE``.
            group (Union[dict, ~google.cloud.monitoring_v3.types.Group]): The ``ListGroupMembers`` response.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.monitoring_v3.types.Group`
            validate_only (bool): If true, validate this request but do not create the group.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.monitoring_v3.types.Group` instance.

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
        if "create_group" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_group"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_group,
                default_retry=self._method_configs["CreateGroup"].retry,
                default_timeout=self._method_configs["CreateGroup"].timeout,
                client_info=self._client_info,
            )

        request = group_service_pb2.CreateGroupRequest(
            name=name, group=group, validate_only=validate_only
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

        return self._inner_api_calls["create_group"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_group(
        self,
        group,
        validate_only=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Identifies the notification channels to which notifications should
        be sent when incidents are opened or closed or when new violations occur
        on an already opened incident. Each element of this array corresponds to
        the ``name`` field in each of the ``NotificationChannel`` objects that
        are returned from the [``ListNotificationChannels``]
        [google.monitoring.v3.NotificationChannelService.ListNotificationChannels]
        method. The format of the entries in this field is:

        ::

            projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.GroupServiceClient()
            >>>
            >>> # TODO: Initialize `group`:
            >>> group = {}
            >>>
            >>> response = client.update_group(group)

        Args:
            group (Union[dict, ~google.cloud.monitoring_v3.types.Group]): A closed time interval. It extends from the start time to the end
                time, and includes both: ``[startTime, endTime]``. Valid time intervals
                depend on the
                ```MetricKind`` <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind>`__
                of the metric value. In no case can the end time be earlier than the
                start time.

                -  For a ``GAUGE`` metric, the ``startTime`` value is technically
                   optional; if no value is specified, the start time defaults to the
                   value of the end time, and the interval represents a single point in
                   time. If both start and end times are specified, they must be
                   identical. Such an interval is valid only for ``GAUGE`` metrics,
                   which are point-in-time measurements.

                -  For ``DELTA`` and ``CUMULATIVE`` metrics, the start time must be
                   earlier than the end time.

                -  In all cases, the start time of the next interval must be at least a
                   millisecond after the end time of the previous interval. Because the
                   interval is closed, if the start time of a new interval is the same
                   as the end time of the previous interval, data written at the new
                   start time could overwrite data written at the previous end time.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.monitoring_v3.types.Group`
            validate_only (bool): If true, validate this request but do not update the existing group.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.monitoring_v3.types.Group` instance.

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
        if "update_group" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_group"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_group,
                default_retry=self._method_configs["UpdateGroup"].retry,
                default_timeout=self._method_configs["UpdateGroup"].timeout,
                client_info=self._client_info,
            )

        request = group_service_pb2.UpdateGroupRequest(
            group=group, validate_only=validate_only
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("group.name", group.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_group"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_group(
        self,
        name,
        recursive=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes an existing group.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.GroupServiceClient()
            >>>
            >>> name = client.group_path('[PROJECT]', '[GROUP]')
            >>>
            >>> client.delete_group(name)

        Args:
            name (str): The request body associated with the HTTP request. If
                ``content_type`` is ``URL_ENCODED``, the body passed in must be
                URL-encoded. Users can provide a ``Content-Length`` header via the
                ``headers`` field or the API will do so. The maximum byte size is 1
                megabyte. Note: As with all ``bytes`` fields JSON representations are
                base64 encoded.
            recursive (bool): If this field is true, then the request means to delete a group with all
                its descendants. Otherwise, the request means to delete a group only when
                it has no descendants. The default value is false.
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
        if "delete_group" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_group"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_group,
                default_retry=self._method_configs["DeleteGroup"].retry,
                default_timeout=self._method_configs["DeleteGroup"].timeout,
                client_info=self._client_info,
            )

        request = group_service_pb2.DeleteGroupRequest(name=name, recursive=recursive)
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

        self._inner_api_calls["delete_group"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_group_members(
        self,
        name,
        page_size=None,
        filter_=None,
        interval=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists the monitored resources that are members of a group.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.GroupServiceClient()
            >>>
            >>> name = client.group_path('[PROJECT]', '[GROUP]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_group_members(name):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_group_members(name).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            name (str): The data points of this time series. When listing time series,
                points are returned in reverse time order.

                When creating a time series, this field must contain exactly one point
                and the point's type must be the same as the value type of the
                associated metric. If the associated metric's descriptor must be
                auto-created, then the value type of the descriptor is determined by the
                point's type, which must be ``BOOL``, ``INT64``, ``DOUBLE``, or
                ``DISTRIBUTION``.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            filter_ (str): ``Struct`` represents a structured data value, consisting of fields
                which map to dynamically typed values. In some languages, ``Struct``
                might be supported by a native representation. For example, in scripting
                languages like JS a struct is represented as an object. The details of
                that representation are described together with the proto support for
                the language.

                The JSON representation for ``Struct`` is JSON object.
            interval (Union[dict, ~google.cloud.monitoring_v3.types.TimeInterval]): An optional time interval for which results should be returned. Only
                members that were part of the group during the specified interval are
                included in the response.  If no interval is provided then the group
                membership over the last minute is returned.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.monitoring_v3.types.TimeInterval`
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
            An iterable of :class:`~google.cloud.monitoring_v3.types.MonitoredResource` instances.
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
        if "list_group_members" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_group_members"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_group_members,
                default_retry=self._method_configs["ListGroupMembers"].retry,
                default_timeout=self._method_configs["ListGroupMembers"].timeout,
                client_info=self._client_info,
            )

        request = group_service_pb2.ListGroupMembersRequest(
            name=name, page_size=page_size, filter=filter_, interval=interval
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
                self._inner_api_calls["list_group_members"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="members",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator
