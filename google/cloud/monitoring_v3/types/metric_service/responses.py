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

__manifest__ = (
    "ListMonitoredResourceDescriptorsResponse",
    "ListMetricDescriptorsResponse",
    "ListTimeSeriesResponse",
    "QueryTimeSeriesResponse",
)


class ListMonitoredResourceDescriptorsResponse(proto.Message):
    r"""The ``ListMonitoredResourceDescriptors`` response.

    Attributes:
        resource_descriptors (Sequence[google.api.monitored_resource_pb2.MonitoredResourceDescriptor]):
            The monitored resource descriptors that are available to
            this project and that match ``filter``, if present.
        next_page_token (str):
            If there are more results than have been returned, then this
            field is set to a non-empty value. To see the additional
            results, use that value as ``page_token`` in the next call
            to this method.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    resource_descriptors = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=monitored_resource_pb2.MonitoredResourceDescriptor,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class ListMetricDescriptorsResponse(proto.Message):
    r"""The ``ListMetricDescriptors`` response.

    Attributes:
        metric_descriptors (Sequence[google.api.metric_pb2.MetricDescriptor]):
            The metric descriptors that are available to the project and
            that match the value of ``filter``, if present.
        next_page_token (str):
            If there are more results than have been returned, then this
            field is set to a non-empty value. To see the additional
            results, use that value as ``page_token`` in the next call
            to this method.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    metric_descriptors = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=metric_pb2.MetricDescriptor,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class ListTimeSeriesResponse(proto.Message):
    r"""The ``ListTimeSeries`` response.

    Attributes:
        time_series (Sequence[google.cloud.monitoring_v3.types.TimeSeries]):
            One or more time series that match the filter
            included in the request.
        next_page_token (str):
            If there are more results than have been returned, then this
            field is set to a non-empty value. To see the additional
            results, use that value as ``page_token`` in the next call
            to this method.
        execution_errors (Sequence[google.rpc.status_pb2.Status]):
            Query execution errors that may have caused
            the time series data returned to be incomplete.
        unit (str):
            The unit in which all ``time_series`` point values are
            reported. ``unit`` follows the UCUM format for units as seen
            in https://unitsofmeasure.org/ucum.html. If different
            ``time_series`` have different units (for example, because
            they come from different metric types, or a unit is absent),
            then ``unit`` will be "{not_a_unit}".
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    time_series = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gm_metric.TimeSeries,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )
    execution_errors = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )
    unit = proto.Field(
        proto.STRING,
        number=5,
    )


class QueryTimeSeriesResponse(proto.Message):
    r"""The ``QueryTimeSeries`` response.

    Attributes:
        time_series_descriptor (google.cloud.monitoring_v3.types.TimeSeriesDescriptor):
            The descriptor for the time series data.
        time_series_data (Sequence[google.cloud.monitoring_v3.types.TimeSeriesData]):
            The time series data.
        next_page_token (str):
            If there are more results than have been returned, then this
            field is set to a non-empty value. To see the additional
            results, use that value as ``page_token`` in the next call
            to this method.
        partial_errors (Sequence[google.rpc.status_pb2.Status]):
            Query execution errors that may have caused
            the time series data returned to be incomplete.
            The available data will be available in the
            response.
    """
    __module__ = __module__.rsplit(".", maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    time_series_descriptor = proto.Field(
        proto.MESSAGE,
        number=8,
        message=gm_metric.TimeSeriesDescriptor,
    )
    time_series_data = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=gm_metric.TimeSeriesData,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=10,
    )
    partial_errors = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=status_pb2.Status,
    )


__all__ = tuple(sorted(__manifest__))
