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
from typing import Any, AsyncIterable, Awaitable, Callable, Iterable, Sequence, Tuple, Optional

from google.cloud.monitoring_v3.types import service
from google.cloud.monitoring_v3.types import service_service


class ListServicesPager:
    """A pager for iterating through ``list_services`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.monitoring_v3.types.ListServicesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``services`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServices`` requests and continue to iterate
    through the ``services`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.monitoring_v3.types.ListServicesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., service_service.ListServicesResponse],
            request: service_service.ListServicesRequest,
            response: service_service.ListServicesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.monitoring_v3.types.ListServicesRequest):
                The initial request object.
            response (google.cloud.monitoring_v3.types.ListServicesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service_service.ListServicesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[service_service.ListServicesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[service.Service]:
        for page in self.pages:
            yield from page.services

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListServicesAsyncPager:
    """A pager for iterating through ``list_services`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.monitoring_v3.types.ListServicesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``services`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServices`` requests and continue to iterate
    through the ``services`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.monitoring_v3.types.ListServicesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[service_service.ListServicesResponse]],
            request: service_service.ListServicesRequest,
            response: service_service.ListServicesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.monitoring_v3.types.ListServicesRequest):
                The initial request object.
            response (google.cloud.monitoring_v3.types.ListServicesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service_service.ListServicesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[service_service.ListServicesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[service.Service]:
        async def async_generator():
            async for page in self.pages:
                for response in page.services:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListServiceLevelObjectivesPager:
    """A pager for iterating through ``list_service_level_objectives`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.monitoring_v3.types.ListServiceLevelObjectivesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``service_level_objectives`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServiceLevelObjectives`` requests and continue to iterate
    through the ``service_level_objectives`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.monitoring_v3.types.ListServiceLevelObjectivesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., service_service.ListServiceLevelObjectivesResponse],
            request: service_service.ListServiceLevelObjectivesRequest,
            response: service_service.ListServiceLevelObjectivesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.monitoring_v3.types.ListServiceLevelObjectivesRequest):
                The initial request object.
            response (google.cloud.monitoring_v3.types.ListServiceLevelObjectivesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service_service.ListServiceLevelObjectivesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[service_service.ListServiceLevelObjectivesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[service.ServiceLevelObjective]:
        for page in self.pages:
            yield from page.service_level_objectives

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListServiceLevelObjectivesAsyncPager:
    """A pager for iterating through ``list_service_level_objectives`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.monitoring_v3.types.ListServiceLevelObjectivesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``service_level_objectives`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServiceLevelObjectives`` requests and continue to iterate
    through the ``service_level_objectives`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.monitoring_v3.types.ListServiceLevelObjectivesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[service_service.ListServiceLevelObjectivesResponse]],
            request: service_service.ListServiceLevelObjectivesRequest,
            response: service_service.ListServiceLevelObjectivesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.monitoring_v3.types.ListServiceLevelObjectivesRequest):
                The initial request object.
            response (google.cloud.monitoring_v3.types.ListServiceLevelObjectivesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service_service.ListServiceLevelObjectivesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[service_service.ListServiceLevelObjectivesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[service.ServiceLevelObjective]:
        async def async_generator():
            async for page in self.pages:
                for response in page.service_level_objectives:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
