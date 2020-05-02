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

"""Accesses the google.monitoring.v3 ServiceMonitoringService API."""

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
from google.cloud.monitoring_v3.gapic import service_monitoring_service_client_config
from google.cloud.monitoring_v3.gapic.transports import (
    service_monitoring_service_grpc_transport,
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
from google.cloud.monitoring_v3.proto import service_pb2
from google.cloud.monitoring_v3.proto import service_service_pb2
from google.cloud.monitoring_v3.proto import service_service_pb2_grpc
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import timestamp_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-monitoring"
).version


class ServiceMonitoringServiceClient(object):
    """
    Protocol Buffers - Google's data interchange format Copyright 2008
    Google Inc. All rights reserved.
    https://developers.google.com/protocol-buffers/

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are
    met:

    ::

        * Redistributions of source code must retain the above copyright

    notice, this list of conditions and the following disclaimer. \*
    Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution. \*
    Neither the name of Google Inc. nor the names of its contributors may be
    used to endorse or promote products derived from this software without
    specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
    IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
    TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
    PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
    OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
    EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
    PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
    LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
    NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    """

    SERVICE_ADDRESS = "monitoring.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.monitoring.v3.ServiceMonitoringService"

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
            ServiceMonitoringServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def project_path(cls, project):
        """Return a fully-qualified project string."""
        return google.api_core.path_template.expand(
            "projects/{project}", project=project
        )

    @classmethod
    def service_path(cls, project, service):
        """Return a fully-qualified service string."""
        return google.api_core.path_template.expand(
            "projects/{project}/services/{service}", project=project, service=service
        )

    @classmethod
    def service_level_objective_path(cls, project, service, service_level_objective):
        """Return a fully-qualified service_level_objective string."""
        return google.api_core.path_template.expand(
            "projects/{project}/services/{service}/serviceLevelObjectives/{service_level_objective}",
            project=project,
            service=service,
            service_level_objective=service_level_objective,
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
            transport (Union[~.ServiceMonitoringServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.ServiceMonitoringServiceGrpcTransport]): A transport
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
            client_config = service_monitoring_service_client_config.config

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
                    default_class=service_monitoring_service_grpc_transport.ServiceMonitoringServiceGrpcTransport,
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
            self.transport = service_monitoring_service_grpc_transport.ServiceMonitoringServiceGrpcTransport(
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
    def create_service(
        self,
        parent,
        service,
        service_id=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a new metric descriptor. User-created metric descriptors
        define `custom
        metrics <https://cloud.google.com/monitoring/custom-metrics>`__.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.ServiceMonitoringServiceClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> # TODO: Initialize `service`:
            >>> service = {}
            >>>
            >>> response = client.create_service(parent, service)

        Args:
            parent (str): The `monitored
                resource <https://cloud.google.com/monitoring/api/resources>`__
                associated with the configuration. The following monitored resource
                types are supported for Uptime checks: ``uptime_url``, ``gce_instance``,
                ``gae_app``, ``aws_ec2_instance``, ``aws_elb_load_balancer``
            service (Union[dict, ~google.cloud.monitoring_v3.types.Service]): ``FieldMask`` represents a set of symbolic field paths, for example:

                ::

                    paths: "f.a"
                    paths: "f.b.d"

                Here ``f`` represents a field in some root message, ``a`` and ``b``
                fields in the message found in ``f``, and ``d`` a field found in the
                message in ``f.b``.

                Field masks are used to specify a subset of fields that should be
                returned by a get operation or modified by an update operation. Field
                masks also have a custom JSON encoding (see below).

                # Field Masks in Projections

                When used in the context of a projection, a response message or
                sub-message is filtered by the API to only contain those fields as
                specified in the mask. For example, if the mask in the previous example
                is applied to a response message as follows:

                ::

                    f {
                      a : 22
                      b {
                        d : 1
                        x : 2
                      }
                      y : 13
                    }
                    z: 8

                The result will not contain specific values for fields x,y and z (their
                value will be set to the default, and omitted in proto text output):

                ::

                    f {
                      a : 22
                      b {
                        d : 1
                      }
                    }

                A repeated field is not allowed except at the last position of a paths
                string.

                If a FieldMask object is not present in a get operation, the operation
                applies to all fields (as if a FieldMask of all fields had been
                specified).

                Note that a field mask does not necessarily apply to the top-level
                response message. In case of a REST get operation, the field mask
                applies directly to the response, but in case of a REST list operation,
                the mask instead applies to each individual message in the returned
                resource list. In case of a REST custom method, other definitions may be
                used. Where the mask applies will be clearly documented together with
                its declaration in the API. In any case, the effect on the returned
                resource/resources is required behavior for APIs.

                # Field Masks in Update Operations

                A field mask in update operations specifies which fields of the targeted
                resource are going to be updated. The API is required to only change the
                values of the fields as specified in the mask and leave the others
                untouched. If a resource is passed in to describe the updated values,
                the API ignores the values of all fields not covered by the mask.

                If a repeated field is specified for an update operation, new values
                will be appended to the existing repeated field in the target resource.
                Note that a repeated field is only allowed in the last position of a
                ``paths`` string.

                If a sub-message is specified in the last position of the field mask for
                an update operation, then new value will be merged into the existing
                sub-message in the target resource.

                For example, given the target message:

                ::

                    f {
                      b {
                        d: 1
                        x: 2
                      }
                      c: [1]
                    }

                And an update message:

                ::

                    f {
                      b {
                        d: 10
                      }
                      c: [2]
                    }

                then if the field mask is:

                paths: ["f.b", "f.c"]

                then the result will be:

                ::

                    f {
                      b {
                        d: 10
                        x: 2
                      }
                      c: [1, 2]
                    }

                An implementation may provide options to override this default behavior
                for repeated and message fields.

                In order to reset a field's value to the default, the field must be in
                the mask and set to the default value in the provided resource. Hence,
                in order to reset all fields of a resource, provide a default instance
                of the resource and set all fields in the mask, or do not provide a mask
                as described below.

                If a field mask is not present on update, the operation applies to all
                fields (as if a field mask of all fields has been specified). Note that
                in the presence of schema evolution, this may mean that fields the
                client does not know and has therefore not filled into the request will
                be reset to their default. If this is unwanted behavior, a specific
                service may require a client to always specify a field mask, producing
                an error if not.

                As with get operations, the location of the resource which describes the
                updated values in the request message depends on the operation kind. In
                any case, the effect of the field mask is required to be honored by the
                API.

                ## Considerations for HTTP REST

                The HTTP kind of an update operation which uses a field mask must be set
                to PATCH instead of PUT in order to satisfy HTTP semantics (PUT must
                only be used for full updates).

                # JSON Encoding of Field Masks

                In JSON, a field mask is encoded as a single string where paths are
                separated by a comma. Fields name in each path are converted to/from
                lower-camel naming conventions.

                As an example, consider the following message declarations:

                ::

                    message Profile {
                      User user = 1;
                      Photo photo = 2;
                    }
                    message User {
                      string display_name = 1;
                      string address = 2;
                    }

                In proto a field mask for ``Profile`` may look as such:

                ::

                    mask {
                      paths: "user.display_name"
                      paths: "photo"
                    }

                In JSON, the same mask is represented as below:

                ::

                    {
                      mask: "user.displayName,photo"
                    }

                # Field Masks and Oneof Fields

                Field masks treat fields in oneofs just as regular fields. Consider the
                following message:

                ::

                    message SampleMessage {
                      oneof test_oneof {
                        string name = 4;
                        SubMessage sub_message = 9;
                      }
                    }

                The field mask can be:

                ::

                    mask {
                      paths: "name"
                    }

                Or:

                ::

                    mask {
                      paths: "sub_message"
                    }

                Note that oneof type names ("test_oneof" in this case) cannot be used in
                paths.

                ## Field Mask Verification

                The implementation of any API method which has a FieldMask type field in
                the request should verify the included field paths, and return an
                ``INVALID_ARGUMENT`` error if any path is unmappable.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.monitoring_v3.types.Service`
            service_id (str): If set, all the classes from the .proto file are wrapped in a single
                outer class with the given name. This applies to both Proto1 (equivalent
                to the old "--one_java_file" option) and Proto2 (where a .proto always
                translates to a single class, but you may want to explicitly choose the
                class name).
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.monitoring_v3.types.Service` instance.

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
        if "create_service" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_service"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_service,
                default_retry=self._method_configs["CreateService"].retry,
                default_timeout=self._method_configs["CreateService"].timeout,
                client_info=self._client_info,
            )

        request = service_service_pb2.CreateServiceRequest(
            parent=parent, service=service, service_id=service_id
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_service"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_service(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        A unique resource name for this Uptime check configuration. The
        format is:

        ::

             projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID]

        This field should be omitted when creating the Uptime check
        configuration; on create, the resource name is assigned by the server
        and included in the response.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.ServiceMonitoringServiceClient()
            >>>
            >>> name = client.service_path('[PROJECT]', '[SERVICE]')
            >>>
            >>> response = client.get_service(name)

        Args:
            name (str): An annotation that describes a resource definition without a
                corresponding message; see ``ResourceDescriptor``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.monitoring_v3.types.Service` instance.

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
        if "get_service" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_service"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_service,
                default_retry=self._method_configs["GetService"].retry,
                default_timeout=self._method_configs["GetService"].timeout,
                client_info=self._client_info,
            )

        request = service_service_pb2.GetServiceRequest(name=name)
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

        return self._inner_api_calls["get_service"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_services(
        self,
        parent,
        filter_=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Delete the given ``ServiceLevelObjective``.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.ServiceMonitoringServiceClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_services(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_services(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Selects a method to which this rule applies.

                Refer to ``selector`` for syntax details.
            filter_ (str): If set true, then the Java code generator will generate a separate
                .java file for each top-level message, enum, and service defined in the
                .proto file. Thus, these types will *not* be nested inside the outer
                class named by java_outer_classname. However, the outer class will still
                be generated to contain the file's getDescriptor() method as well as any
                top-level extensions defined in the file.
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
            An iterable of :class:`~google.cloud.monitoring_v3.types.Service` instances.
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
        if "list_services" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_services"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_services,
                default_retry=self._method_configs["ListServices"].retry,
                default_timeout=self._method_configs["ListServices"].timeout,
                client_info=self._client_info,
            )

        request = service_service_pb2.ListServicesRequest(
            parent=parent, filter=filter_, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
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
                self._inner_api_calls["list_services"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="services",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def update_service(
        self,
        service,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Required. The monitored resource type. This field must match the
        ``type`` field of a ``MonitoredResourceDescriptor`` object. For example,
        the type of a Compute Engine VM instance is ``gce_instance``.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.ServiceMonitoringServiceClient()
            >>>
            >>> # TODO: Initialize `service`:
            >>> service = {}
            >>>
            >>> response = client.update_service(service)

        Args:
            service (Union[dict, ~google.cloud.monitoring_v3.types.Service]): Wrapper message for ``double``.

                The JSON representation for ``DoubleValue`` is JSON number.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.monitoring_v3.types.Service`
            update_mask (Union[dict, ~google.cloud.monitoring_v3.types.FieldMask]): A set of field paths defining which fields to use for the update.

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
            A :class:`~google.cloud.monitoring_v3.types.Service` instance.

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
        if "update_service" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_service"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_service,
                default_retry=self._method_configs["UpdateService"].retry,
                default_timeout=self._method_configs["UpdateService"].timeout,
                client_info=self._client_info,
            )

        request = service_service_pb2.UpdateServiceRequest(
            service=service, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("service.name", service.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_service"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_service(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Each of the definitions above may have "options" attached. These are
        just annotations which may cause code to be generated slightly
        differently or may contain hints for code that manipulates protocol
        messages.

        Clients may define custom options as extensions of the \*Options
        messages. These extensions may not yet be known at parsing time, so the
        parser cannot store the values in them. Instead it stores them in a
        field in the \*Options message called uninterpreted_option. This field
        must have the same name across all \*Options messages. We then use this
        field to populate the extensions when we build a descriptor, at which
        point all protos have been parsed and so all extensions are known.

        Extension numbers for custom options may be chosen as follows:

        -  For options which will only be used within a single application or
           organization, or for experimental options, use field numbers 50000
           through 99999. It is up to you to ensure that you do not use the same
           number for multiple options.
        -  For options which will be published and used publicly by multiple
           independent entities, e-mail
           protobuf-global-extension-registry@google.com to reserve extension
           numbers. Simply provide your project name (e.g. Objective-C plugin)
           and your project website (if available) -- there's no need to explain
           how you intend to use them. Usually you only need one extension
           number. You can declare multiple options with only one extension
           number by putting them in a sub-message. See the Custom Options
           section of the docs for examples:
           https://developers.google.com/protocol-buffers/docs/proto#options If
           this turns out to be popular, a web service will be set up to
           automatically assign option numbers.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.ServiceMonitoringServiceClient()
            >>>
            >>> name = client.service_path('[PROJECT]', '[SERVICE]')
            >>>
            >>> client.delete_service(name)

        Args:
            name (str): If non-empty, ``page_token`` must contain a value returned as the
                ``next_page_token`` in a previous response to request the next set of
                results.
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
        if "delete_service" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_service"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_service,
                default_retry=self._method_configs["DeleteService"].retry,
                default_timeout=self._method_configs["DeleteService"].timeout,
                client_info=self._client_info,
            )

        request = service_service_pb2.DeleteServiceRequest(name=name)
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

        self._inner_api_calls["delete_service"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_service_level_objective(
        self,
        parent,
        service_level_objective,
        service_level_objective_id=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Protocol Buffers - Google's data interchange format Copyright 2008
        Google Inc. All rights reserved.
        https://developers.google.com/protocol-buffers/

        Redistribution and use in source and binary forms, with or without
        modification, are permitted provided that the following conditions are
        met:

        ::

            * Redistributions of source code must retain the above copyright

        notice, this list of conditions and the following disclaimer. \*
        Redistributions in binary form must reproduce the above copyright
        notice, this list of conditions and the following disclaimer in the
        documentation and/or other materials provided with the distribution. \*
        Neither the name of Google Inc. nor the names of its contributors may be
        used to endorse or promote products derived from this software without
        specific prior written permission.

        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
        IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
        TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
        PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
        OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
        EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
        PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
        PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
        LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
        NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
        SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.ServiceMonitoringServiceClient()
            >>>
            >>> parent = client.service_path('[PROJECT]', '[SERVICE]')
            >>>
            >>> # TODO: Initialize `service_level_objective`:
            >>> service_level_objective = {}
            >>>
            >>> response = client.create_service_level_objective(parent, service_level_objective)

        Args:
            parent (str): The ``ListNotificationChannelDescriptors`` response.
            service_level_objective (Union[dict, ~google.cloud.monitoring_v3.types.ServiceLevelObjective]): Required. The project on which to execute the request. The format
                is:

                ::

                    projects/[PROJECT_ID_OR_NUMBER]

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.monitoring_v3.types.ServiceLevelObjective`
            service_level_objective_id (str): Wrapper message for ``float``.

                The JSON representation for ``FloatValue`` is JSON number.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.monitoring_v3.types.ServiceLevelObjective` instance.

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
        if "create_service_level_objective" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_service_level_objective"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_service_level_objective,
                default_retry=self._method_configs["CreateServiceLevelObjective"].retry,
                default_timeout=self._method_configs[
                    "CreateServiceLevelObjective"
                ].timeout,
                client_info=self._client_info,
            )

        request = service_service_pb2.CreateServiceLevelObjectiveRequest(
            parent=parent,
            service_level_objective=service_level_objective,
            service_level_objective_id=service_level_objective_id,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_service_level_objective"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_service_level_objective(
        self,
        name,
        view=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        An annotation that describes a resource reference, see
        ``ResourceReference``.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.ServiceMonitoringServiceClient()
            >>>
            >>> name = client.service_level_objective_path('[PROJECT]', '[SERVICE]', '[SERVICE_LEVEL_OBJECTIVE]')
            >>>
            >>> response = client.get_service_level_objective(name)

        Args:
            name (str): The resource has one pattern, but the API owner expects to add more
                later. (This is the inverse of ORIGINALLY_SINGLE_PATTERN, and prevents
                that from being necessary once there are multiple patterns.)
            view (~google.cloud.monitoring_v3.types.View): Wrapper message for ``int64``.

                The JSON representation for ``Int64Value`` is JSON string.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.monitoring_v3.types.ServiceLevelObjective` instance.

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
        if "get_service_level_objective" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_service_level_objective"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_service_level_objective,
                default_retry=self._method_configs["GetServiceLevelObjective"].retry,
                default_timeout=self._method_configs[
                    "GetServiceLevelObjective"
                ].timeout,
                client_info=self._client_info,
            )

        request = service_service_pb2.GetServiceLevelObjectiveRequest(
            name=name, view=view
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

        return self._inner_api_calls["get_service_level_objective"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_service_level_objectives(
        self,
        parent,
        filter_=None,
        page_size=None,
        view=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Protocol Buffers - Google's data interchange format Copyright 2008
        Google Inc. All rights reserved.
        https://developers.google.com/protocol-buffers/

        Redistribution and use in source and binary forms, with or without
        modification, are permitted provided that the following conditions are
        met:

        ::

            * Redistributions of source code must retain the above copyright

        notice, this list of conditions and the following disclaimer. \*
        Redistributions in binary form must reproduce the above copyright
        notice, this list of conditions and the following disclaimer in the
        documentation and/or other materials provided with the distribution. \*
        Neither the name of Google Inc. nor the names of its contributors may be
        used to endorse or promote products derived from this software without
        specific prior written permission.

        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
        IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
        TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
        PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
        OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
        EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
        PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
        PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
        LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
        NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
        SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.ServiceMonitoringServiceClient()
            >>>
            >>> parent = client.service_path('[PROJECT]', '[SERVICE]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_service_level_objectives(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_service_level_objectives(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): The resource type. It must be in the format of
                {service_name}/{resource_type_kind}. The ``resource_type_kind`` must be
                singular and must not include version numbers.

                Example: ``storage.googleapis.com/Bucket``

                The value of the resource_type_kind must follow the regular expression
                /[A-Za-z][a-zA-Z0-9]+/. It should start with an upper case character and
                should use PascalCase (UpperCamelCase). The maximum number of characters
                allowed for the ``resource_type_kind`` is 100.
            filter_ (str): An optional
                `filter <https://cloud.google.com/monitoring/api/v3/filters>`__
                describing the descriptors to be returned. The filter can reference the
                descriptor's type and labels. For example, the following filter returns
                only Google Compute Engine descriptors that have an ``id`` label:

                ::

                    resource.type = starts_with("gce_") AND resource.label:id
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            view (~google.cloud.monitoring_v3.types.View): The ``GetNotificationChannelDescriptor`` response.
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
            An iterable of :class:`~google.cloud.monitoring_v3.types.ServiceLevelObjective` instances.
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
        if "list_service_level_objectives" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_service_level_objectives"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_service_level_objectives,
                default_retry=self._method_configs["ListServiceLevelObjectives"].retry,
                default_timeout=self._method_configs[
                    "ListServiceLevelObjectives"
                ].timeout,
                client_info=self._client_info,
            )

        request = service_service_pb2.ListServiceLevelObjectivesRequest(
            parent=parent, filter=filter_, page_size=page_size, view=view
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
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
                self._inner_api_calls["list_service_level_objectives"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="service_level_objectives",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def update_service_level_objective(
        self,
        service_level_objective,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Wrappers for primitive (non-message) types. These types are useful
        for embedding primitives in the ``google.protobuf.Any`` type and for
        places where we need to distinguish between the absence of a primitive
        typed field and its default value.

        These wrappers have no meaningful use within repeated fields as they
        lack the ability to detect presence on individual elements. These
        wrappers have no meaningful use within a map or a oneof since individual
        entries of a map or fields of a oneof can already detect presence.

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.ServiceMonitoringServiceClient()
            >>>
            >>> # TODO: Initialize `service_level_objective`:
            >>> service_level_objective = {}
            >>>
            >>> response = client.update_service_level_objective(service_level_objective)

        Args:
            service_level_objective (Union[dict, ~google.cloud.monitoring_v3.types.ServiceLevelObjective]): The ``ListGroups`` response.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.monitoring_v3.types.ServiceLevelObjective`
            update_mask (Union[dict, ~google.cloud.monitoring_v3.types.FieldMask]): A set of field paths defining which fields to use for the update.

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
            A :class:`~google.cloud.monitoring_v3.types.ServiceLevelObjective` instance.

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
        if "update_service_level_objective" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_service_level_objective"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_service_level_objective,
                default_retry=self._method_configs["UpdateServiceLevelObjective"].retry,
                default_timeout=self._method_configs[
                    "UpdateServiceLevelObjective"
                ].timeout,
                client_info=self._client_info,
            )

        request = service_service_pb2.UpdateServiceLevelObjectiveRequest(
            service_level_objective=service_level_objective, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [
                ("service_level_objective.name", service_level_objective.name)
            ]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_service_level_objective"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_service_level_objective(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Required. The project whose groups are to be listed. The format is:

        ::

            projects/[PROJECT_ID_OR_NUMBER]

        Example:
            >>> from google.cloud import monitoring_v3
            >>>
            >>> client = monitoring_v3.ServiceMonitoringServiceClient()
            >>>
            >>> name = client.service_level_objective_path('[PROJECT]', '[SERVICE]', '[SERVICE_LEVEL_OBJECTIVE]')
            >>>
            >>> client.delete_service_level_objective(name)

        Args:
            name (str): If this is ``true``, then checks are made only from the
                'internal_checkers'. If it is ``false``, then checks are made only from
                the 'selected_regions'. It is an error to provide 'selected_regions'
                when is_internal is ``true``, or to provide 'internal_checkers' when
                is_internal is ``false``.
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
        if "delete_service_level_objective" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_service_level_objective"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_service_level_objective,
                default_retry=self._method_configs["DeleteServiceLevelObjective"].retry,
                default_timeout=self._method_configs[
                    "DeleteServiceLevelObjective"
                ].timeout,
                client_info=self._client_info,
            )

        request = service_service_pb2.DeleteServiceLevelObjectiveRequest(name=name)
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

        self._inner_api_calls["delete_service_level_objective"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
