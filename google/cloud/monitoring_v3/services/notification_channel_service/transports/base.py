# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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

import abc
import typing
import pkg_resources

from google import auth  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore

from google.cloud.monitoring_v3.types import notification
from google.cloud.monitoring_v3.types import notification_service
from google.protobuf import empty_pb2 as empty  # type: ignore


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-monitoring",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class NotificationChannelServiceTransport(abc.ABC):
    """Abstract transport class for NotificationChannelService."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/monitoring",
        "https://www.googleapis.com/auth/monitoring.read",
    )

    def __init__(
        self,
        *,
        host: str = "monitoring.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: typing.Optional[str] = None,
        scopes: typing.Optional[typing.Sequence[str]] = AUTH_SCOPES,
        quota_project_id: typing.Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scope (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        # Save the scopes.
        self._scopes = scopes or self.AUTH_SCOPES

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = auth.load_credentials_from_file(
                credentials_file, scopes=self._scopes, quota_project_id=quota_project_id
            )

        elif credentials is None:
            credentials, _ = auth.default(
                scopes=self._scopes, quota_project_id=quota_project_id
            )

        # Save the credentials.
        self._credentials = credentials

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_notification_channel_descriptors: gapic_v1.method.wrap_method(
                self.list_notification_channel_descriptors,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_notification_channel_descriptor: gapic_v1.method.wrap_method(
                self.get_notification_channel_descriptor,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.list_notification_channels: gapic_v1.method.wrap_method(
                self.list_notification_channels,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_notification_channel: gapic_v1.method.wrap_method(
                self.get_notification_channel,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.create_notification_channel: gapic_v1.method.wrap_method(
                self.create_notification_channel,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.update_notification_channel: gapic_v1.method.wrap_method(
                self.update_notification_channel,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.delete_notification_channel: gapic_v1.method.wrap_method(
                self.delete_notification_channel,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.send_notification_channel_verification_code: gapic_v1.method.wrap_method(
                self.send_notification_channel_verification_code,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_notification_channel_verification_code: gapic_v1.method.wrap_method(
                self.get_notification_channel_verification_code,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.verify_notification_channel: gapic_v1.method.wrap_method(
                self.verify_notification_channel,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
        }

    @property
    def list_notification_channel_descriptors(
        self,
    ) -> typing.Callable[
        [notification_service.ListNotificationChannelDescriptorsRequest],
        typing.Union[
            notification_service.ListNotificationChannelDescriptorsResponse,
            typing.Awaitable[
                notification_service.ListNotificationChannelDescriptorsResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_notification_channel_descriptor(
        self,
    ) -> typing.Callable[
        [notification_service.GetNotificationChannelDescriptorRequest],
        typing.Union[
            notification.NotificationChannelDescriptor,
            typing.Awaitable[notification.NotificationChannelDescriptor],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_notification_channels(
        self,
    ) -> typing.Callable[
        [notification_service.ListNotificationChannelsRequest],
        typing.Union[
            notification_service.ListNotificationChannelsResponse,
            typing.Awaitable[notification_service.ListNotificationChannelsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_notification_channel(
        self,
    ) -> typing.Callable[
        [notification_service.GetNotificationChannelRequest],
        typing.Union[
            notification.NotificationChannel,
            typing.Awaitable[notification.NotificationChannel],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_notification_channel(
        self,
    ) -> typing.Callable[
        [notification_service.CreateNotificationChannelRequest],
        typing.Union[
            notification.NotificationChannel,
            typing.Awaitable[notification.NotificationChannel],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_notification_channel(
        self,
    ) -> typing.Callable[
        [notification_service.UpdateNotificationChannelRequest],
        typing.Union[
            notification.NotificationChannel,
            typing.Awaitable[notification.NotificationChannel],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_notification_channel(
        self,
    ) -> typing.Callable[
        [notification_service.DeleteNotificationChannelRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def send_notification_channel_verification_code(
        self,
    ) -> typing.Callable[
        [notification_service.SendNotificationChannelVerificationCodeRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_notification_channel_verification_code(
        self,
    ) -> typing.Callable[
        [notification_service.GetNotificationChannelVerificationCodeRequest],
        typing.Union[
            notification_service.GetNotificationChannelVerificationCodeResponse,
            typing.Awaitable[
                notification_service.GetNotificationChannelVerificationCodeResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def verify_notification_channel(
        self,
    ) -> typing.Callable[
        [notification_service.VerifyNotificationChannelRequest],
        typing.Union[
            notification.NotificationChannel,
            typing.Awaitable[notification.NotificationChannel],
        ],
    ]:
        raise NotImplementedError()


__all__ = ("NotificationChannelServiceTransport",)
