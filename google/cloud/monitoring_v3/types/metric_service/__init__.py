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
import proto  # type: ignore

from google.api import metric_pb2  # type: ignore
from google.api import monitored_resource_pb2  # type: ignore
from google.cloud.monitoring_v3.types import common
from google.cloud.monitoring_v3.types import metric as gm_metric
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.monitoring.v3",
    manifest={
        "ListMonitoredResourceDescriptorsRequest",
        "ListMonitoredResourceDescriptorsResponse",
        "GetMonitoredResourceDescriptorRequest",
        "ListMetricDescriptorsRequest",
        "ListMetricDescriptorsResponse",
        "GetMetricDescriptorRequest",
        "CreateMetricDescriptorRequest",
        "DeleteMetricDescriptorRequest",
        "ListTimeSeriesRequest",
        "ListTimeSeriesResponse",
        "CreateTimeSeriesRequest",
        "CreateTimeSeriesError",
        "CreateTimeSeriesSummary",
        "QueryTimeSeriesRequest",
        "QueryTimeSeriesResponse",
        "QueryErrorList",
    },
)


from .requests import (
    ListMonitoredResourceDescriptorsRequest,
    GetMonitoredResourceDescriptorRequest,
    ListMetricDescriptorsRequest,
    GetMetricDescriptorRequest,
    CreateMetricDescriptorRequest,
    DeleteMetricDescriptorRequest,
    ListTimeSeriesRequest,
    CreateTimeSeriesRequest,
    QueryTimeSeriesRequest,
)

from .responses import (
    ListMonitoredResourceDescriptorsResponse,
    ListMetricDescriptorsResponse,
    ListTimeSeriesResponse,
    QueryTimeSeriesResponse,
)


class CreateTimeSeriesError(proto.Message):
    r"""DEPRECATED. Used to hold per-time-series error status.

    Attributes:
        time_series (google.cloud.monitoring_v3.types.TimeSeries):
            DEPRECATED. Time series ID that resulted in the ``status``
            error.
        status (google.rpc.status_pb2.Status):
            DEPRECATED. The status of the requested write operation for
            ``time_series``.
    """

    time_series = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gm_metric.TimeSeries,
    )
    status = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )


class CreateTimeSeriesSummary(proto.Message):
    r"""Summary of the result of a failed request to write data to a
    time series.

    Attributes:
        total_point_count (int):
            The number of points in the request.
        success_point_count (int):
            The number of points that were successfully
            written.
        errors (Sequence[google.cloud.monitoring_v3.types.CreateTimeSeriesSummary.Error]):
            The number of points that failed to be
            written. Order is not guaranteed.
    """

    class Error(proto.Message):
        r"""Detailed information about an error category.

        Attributes:
            status (google.rpc.status_pb2.Status):
                The status of the requested write operation.
            point_count (int):
                The number of points that couldn't be written because of
                ``status``.
        """

        status = proto.Field(
            proto.MESSAGE,
            number=1,
            message=status_pb2.Status,
        )
        point_count = proto.Field(
            proto.INT32,
            number=2,
        )

    total_point_count = proto.Field(
        proto.INT32,
        number=1,
    )
    success_point_count = proto.Field(
        proto.INT32,
        number=2,
    )
    errors = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Error,
    )


class QueryErrorList(proto.Message):
    r"""This is an error detail intended to be used with INVALID_ARGUMENT
    errors.

    Attributes:
        errors (Sequence[google.cloud.monitoring_v3.types.QueryError]):
            Errors in parsing the time series query
            language text. The number of errors in the
            response may be limited.
        error_summary (str):
            A summary of all the errors.
    """

    errors = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gm_metric.QueryError,
    )
    error_summary = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
