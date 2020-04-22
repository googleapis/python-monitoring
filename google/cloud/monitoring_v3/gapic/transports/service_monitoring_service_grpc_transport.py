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


import google.api_core.grpc_helpers

from google.cloud.monitoring_v3.proto import service_service_pb2_grpc


class ServiceMonitoringServiceGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.monitoring.v3 ServiceMonitoringService API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/monitoring",
        "https://www.googleapis.com/auth/monitoring.read",
        "https://www.googleapis.com/auth/monitoring.write",
    )

    def __init__(
        self, channel=None, credentials=None, address="monitoring.googleapis.com:443"
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive."
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "service_monitoring_service_stub": service_service_pb2_grpc.ServiceMonitoringServiceStub(
                channel
            )
        }

    @classmethod
    def create_channel(
        cls, address="monitoring.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def create_service(self):
        """Return the gRPC stub for :meth:`ServiceMonitoringServiceClient.create_service`.

        Creates a new metric descriptor. User-created metric descriptors
        define `custom
        metrics <https://cloud.google.com/monitoring/custom-metrics>`__.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["service_monitoring_service_stub"].CreateService

    @property
    def get_service(self):
        """Return the gRPC stub for :meth:`ServiceMonitoringServiceClient.get_service`.

        A unique resource name for this Uptime check configuration. The
        format is:

        ::

             projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID]

        This field should be omitted when creating the Uptime check
        configuration; on create, the resource name is assigned by the server
        and included in the response.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["service_monitoring_service_stub"].GetService

    @property
    def list_services(self):
        """Return the gRPC stub for :meth:`ServiceMonitoringServiceClient.list_services`.

        Delete the given ``ServiceLevelObjective``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["service_monitoring_service_stub"].ListServices

    @property
    def update_service(self):
        """Return the gRPC stub for :meth:`ServiceMonitoringServiceClient.update_service`.

        Required. The monitored resource type. This field must match the
        ``type`` field of a ``MonitoredResourceDescriptor`` object. For example,
        the type of a Compute Engine VM instance is ``gce_instance``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["service_monitoring_service_stub"].UpdateService

    @property
    def delete_service(self):
        """Return the gRPC stub for :meth:`ServiceMonitoringServiceClient.delete_service`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["service_monitoring_service_stub"].DeleteService

    @property
    def create_service_level_objective(self):
        """Return the gRPC stub for :meth:`ServiceMonitoringServiceClient.create_service_level_objective`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs[
            "service_monitoring_service_stub"
        ].CreateServiceLevelObjective

    @property
    def get_service_level_objective(self):
        """Return the gRPC stub for :meth:`ServiceMonitoringServiceClient.get_service_level_objective`.

        An annotation that describes a resource reference, see
        ``ResourceReference``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["service_monitoring_service_stub"].GetServiceLevelObjective

    @property
    def list_service_level_objectives(self):
        """Return the gRPC stub for :meth:`ServiceMonitoringServiceClient.list_service_level_objectives`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["service_monitoring_service_stub"].ListServiceLevelObjectives

    @property
    def update_service_level_objective(self):
        """Return the gRPC stub for :meth:`ServiceMonitoringServiceClient.update_service_level_objective`.

        Wrappers for primitive (non-message) types. These types are useful
        for embedding primitives in the ``google.protobuf.Any`` type and for
        places where we need to distinguish between the absence of a primitive
        typed field and its default value.

        These wrappers have no meaningful use within repeated fields as they
        lack the ability to detect presence on individual elements. These
        wrappers have no meaningful use within a map or a oneof since individual
        entries of a map or fields of a oneof can already detect presence.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs[
            "service_monitoring_service_stub"
        ].UpdateServiceLevelObjective

    @property
    def delete_service_level_objective(self):
        """Return the gRPC stub for :meth:`ServiceMonitoringServiceClient.delete_service_level_objective`.

        Required. The project whose groups are to be listed. The format is:

        ::

            projects/[PROJECT_ID_OR_NUMBER]

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs[
            "service_monitoring_service_stub"
        ].DeleteServiceLevelObjective
