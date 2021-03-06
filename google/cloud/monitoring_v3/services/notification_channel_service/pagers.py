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

from typing import Any, AsyncIterable, Awaitable, Callable, Iterable, Sequence, Tuple

from google.cloud.monitoring_v3.types import notification
from google.cloud.monitoring_v3.types import notification_service


class ListNotificationChannelDescriptorsPager:
    """A pager for iterating through ``list_notification_channel_descriptors`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.monitoring_v3.types.ListNotificationChannelDescriptorsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``channel_descriptors`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListNotificationChannelDescriptors`` requests and continue to iterate
    through the ``channel_descriptors`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.monitoring_v3.types.ListNotificationChannelDescriptorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., notification_service.ListNotificationChannelDescriptorsResponse
        ],
        request: notification_service.ListNotificationChannelDescriptorsRequest,
        response: notification_service.ListNotificationChannelDescriptorsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.monitoring_v3.types.ListNotificationChannelDescriptorsRequest):
                The initial request object.
            response (google.cloud.monitoring_v3.types.ListNotificationChannelDescriptorsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = notification_service.ListNotificationChannelDescriptorsRequest(
            request
        )
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterable[notification_service.ListNotificationChannelDescriptorsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[notification.NotificationChannelDescriptor]:
        for page in self.pages:
            yield from page.channel_descriptors

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNotificationChannelDescriptorsAsyncPager:
    """A pager for iterating through ``list_notification_channel_descriptors`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.monitoring_v3.types.ListNotificationChannelDescriptorsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``channel_descriptors`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListNotificationChannelDescriptors`` requests and continue to iterate
    through the ``channel_descriptors`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.monitoring_v3.types.ListNotificationChannelDescriptorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[notification_service.ListNotificationChannelDescriptorsResponse],
        ],
        request: notification_service.ListNotificationChannelDescriptorsRequest,
        response: notification_service.ListNotificationChannelDescriptorsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.monitoring_v3.types.ListNotificationChannelDescriptorsRequest):
                The initial request object.
            response (google.cloud.monitoring_v3.types.ListNotificationChannelDescriptorsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = notification_service.ListNotificationChannelDescriptorsRequest(
            request
        )
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterable[notification_service.ListNotificationChannelDescriptorsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[notification.NotificationChannelDescriptor]:
        async def async_generator():
            async for page in self.pages:
                for response in page.channel_descriptors:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNotificationChannelsPager:
    """A pager for iterating through ``list_notification_channels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.monitoring_v3.types.ListNotificationChannelsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``notification_channels`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListNotificationChannels`` requests and continue to iterate
    through the ``notification_channels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.monitoring_v3.types.ListNotificationChannelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., notification_service.ListNotificationChannelsResponse],
        request: notification_service.ListNotificationChannelsRequest,
        response: notification_service.ListNotificationChannelsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.monitoring_v3.types.ListNotificationChannelsRequest):
                The initial request object.
            response (google.cloud.monitoring_v3.types.ListNotificationChannelsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = notification_service.ListNotificationChannelsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[notification_service.ListNotificationChannelsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[notification.NotificationChannel]:
        for page in self.pages:
            yield from page.notification_channels

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNotificationChannelsAsyncPager:
    """A pager for iterating through ``list_notification_channels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.monitoring_v3.types.ListNotificationChannelsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``notification_channels`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListNotificationChannels`` requests and continue to iterate
    through the ``notification_channels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.monitoring_v3.types.ListNotificationChannelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[notification_service.ListNotificationChannelsResponse]
        ],
        request: notification_service.ListNotificationChannelsRequest,
        response: notification_service.ListNotificationChannelsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.monitoring_v3.types.ListNotificationChannelsRequest):
                The initial request object.
            response (google.cloud.monitoring_v3.types.ListNotificationChannelsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = notification_service.ListNotificationChannelsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterable[notification_service.ListNotificationChannelsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[notification.NotificationChannel]:
        async def async_generator():
            async for page in self.pages:
                for response in page.notification_channels:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
