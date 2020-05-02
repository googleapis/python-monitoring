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

"""Wrappers for protocol buffer enum types."""

import enum


class CalendarPeriod(enum.IntEnum):
    """
    ``distribution_cut`` is used when ``good_service`` is a count of
    values aggregated in a ``Distribution`` that fall into a good range. The
    ``total_service`` is the total count of all values aggregated in the
    ``Distribution``.

    Attributes:
      CALENDAR_PERIOD_UNSPECIFIED (int): Undefined period, raises an error.
      DAY (int): A day.
      WEEK (int): The set of fields to preserve when ``cross_series_reducer`` is
      specified. The ``group_by_fields`` determine how the time series are
      partitioned into subsets prior to applying the aggregation operation.
      Each subset contains time series that have the same value for each of
      the grouping fields. Each individual time series is a member of exactly
      one subset. The ``cross_series_reducer`` is applied to each subset of
      time series. It is not possible to reduce across different resource
      types, so this field implicitly contains ``resource.type``. Fields not
      specified in ``group_by_fields`` are aggregated away. If
      ``group_by_fields`` is not specified and all the time series have the
      same resource type, then the time series are aggregated into a single
      output time series. If ``cross_series_reducer`` is not defined, this
      field is ignored.
      FORTNIGHT (int): Optional (defaults to 80 when ``use_ssl`` is ``false``, and 443 when
      ``use_ssl`` is ``true``). The TCP port on the HTTP server against which
      to run the check. Will be combined with host (specified within the
      ``monitored_resource``) and ``path`` to construct the full URL.
      MONTH (int): A month.
      QUARTER (int): A quarter. Quarters start on dates 1-Jan, 1-Apr, 1-Jul, and 1-Oct of each
      year.
      HALF (int): A half-year. Half-years start on dates 1-Jan and 1-Jul.
      YEAR (int): A year.
    """

    CALENDAR_PERIOD_UNSPECIFIED = 0
    DAY = 1
    WEEK = 2
    FORTNIGHT = 3
    MONTH = 4
    QUARTER = 5
    HALF = 6
    YEAR = 7


class ComparisonType(enum.IntEnum):
    """
    A ``CalendarPeriod`` represents the abstract concept of a time
    period that has a canonical start. Grammatically, "the start of the
    current ``CalendarPeriod``." All calendar times begin at midnight UTC.

    Attributes:
      COMPARISON_UNSPECIFIED (int): No ordering relationship is specified.
      COMPARISON_GT (int): True if the left argument is greater than the right argument.
      COMPARISON_GE (int): True if the left argument is greater than or equal to the right argument.
      COMPARISON_LT (int): True if the left argument is less than the right argument.
      COMPARISON_LE (int): True if the left argument is less than or equal to the right argument.
      COMPARISON_EQ (int): True if the left argument is equal to the right argument.
      COMPARISON_NE (int): True if the left argument is not equal to the right argument.
    """

    COMPARISON_UNSPECIFIED = 0
    COMPARISON_GT = 1
    COMPARISON_GE = 2
    COMPARISON_LT = 3
    COMPARISON_LE = 4
    COMPARISON_EQ = 5
    COMPARISON_NE = 6


class GroupResourceType(enum.IntEnum):
    """
    Required. A group definition. It is an error to define the ``name``
    field because the system assigns the name.

    Attributes:
      RESOURCE_TYPE_UNSPECIFIED (int): Default value (not valid).
      INSTANCE (int): A group of instances from Google Cloud Platform (GCP) or
      Amazon Web Services (AWS).
      AWS_ELB_LOAD_BALANCER (int): A group of Amazon ELB load balancers.
    """

    RESOURCE_TYPE_UNSPECIFIED = 0
    INSTANCE = 1
    AWS_ELB_LOAD_BALANCER = 2


class LaunchStage(enum.IntEnum):
    """
    A developer-facing error message, which should be in English. Any
    user-facing error message should be localized and sent in the
    ``google.rpc.Status.details`` field, or localized by the client.

    Attributes:
      LAUNCH_STAGE_UNSPECIFIED (int): Do not use this default value.
      EARLY_ACCESS (int): Early Access features are limited to a closed group of testers. To use
      these features, you must sign up in advance and sign a Trusted Tester
      agreement (which includes confidentiality provisions). These features may
      be unstable, changed in backward-incompatible ways, and are not
      guaranteed to be released.
      ALPHA (int): Alpha is a limited availability test for releases before they are cleared
      for widespread use. By Alpha, all significant design issues are resolved
      and we are in the process of verifying functionality. Alpha customers
      need to apply for access, agree to applicable terms, and have their
      projects whitelisted. Alpha releases don’t have to be feature complete,
      no SLAs are provided, and there are no technical support obligations, but
      they will be far enough along that customers can actually use them in
      test environments or for limited-use tests -- just like they would in
      normal production cases.
      BETA (int): Beta is the point at which we are ready to open a release for any
      customer to use. There are no SLA or technical support obligations in a
      Beta release. Products will be complete from a feature perspective, but
      may have some open outstanding issues. Beta releases are suitable for
      limited production use cases.
      GA (int): GA features are open to all developers and are considered stable and
      fully qualified for production use.
      DEPRECATED (int): Identifier for the mesh in which this Istio service is defined.
      Corresponds to the ``mesh_uid`` metric label in Istio metrics.
    """

    LAUNCH_STAGE_UNSPECIFIED = 0
    EARLY_ACCESS = 1
    ALPHA = 2
    BETA = 3
    GA = 4
    DEPRECATED = 5


class NullValue(enum.IntEnum):
    """
    Required. Resource name of the ``ServiceLevelObjective`` to delete.
    The format is:

    ::

        projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]

    Attributes:
      NULL_VALUE (int): Null value.
    """

    NULL_VALUE = 0


class ServiceTier(enum.IntEnum):
    """
    The name of the request field whose value is mapped to the HTTP
    request body, or ``*`` for mapping all request fields not captured by
    the path pattern to the HTTP body, or omitted for not having any HTTP
    request body.

    NOTE: the referred field must be present at the top-level of the request
    message type.

    Attributes:
      SERVICE_TIER_UNSPECIFIED (int): An invalid sentinel value, used to indicate that a tier has not
      been provided explicitly.
      SERVICE_TIER_BASIC (int): The ``DeleteService`` request.
      SERVICE_TIER_PREMIUM (int): Required. Resource name of the ``Service`` to delete. The format is:

      ::

          projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]
    """

    SERVICE_TIER_UNSPECIFIED = 0
    SERVICE_TIER_BASIC = 1
    SERVICE_TIER_PREMIUM = 2


class UptimeCheckRegion(enum.IntEnum):
    """
    The regions from which an Uptime check can be run.

    Attributes:
      REGION_UNSPECIFIED (int): Default value if no region is specified. Will result in Uptime checks
      running from all regions.
      USA (int): Allows checks to run from locations within the United States of America.
      EUROPE (int): Allows checks to run from locations within the continent of Europe.
      SOUTH_AMERICA (int): Allows checks to run from locations within the continent of South
      America.
      ASIA_PACIFIC (int): Allows checks to run from locations within the Asia Pacific area (ex:
      Singapore).
    """

    REGION_UNSPECIFIED = 0
    USA = 1
    EUROPE = 2
    SOUTH_AMERICA = 3
    ASIA_PACIFIC = 4


class Aggregation(object):
    class Aligner(enum.IntEnum):
        """
        Specifies a linear sequence of buckets that all have the same width
        (except overflow and underflow). Each bucket represents a constant
        absolute uncertainty on the specific value in the bucket.

        There are ``num_finite_buckets + 2`` (= N) buckets. Bucket ``i`` has the
        following boundaries:

        ::

           Upper bound (0 <= i < N-1):     offset + (width * i).
           Lower bound (1 <= i < N):       offset + (width * (i - 1)).

        Attributes:
          ALIGN_NONE (int): The maximum number of results to return in a single response. The
          server may further constrain the maximum number of results returned in a
          single page. If the page_size is <=0, the server will decide the number
          of results to be returned. NOTE: this field is not yet implemented
          ALIGN_DELTA (int): The ``GetNotificationChannelVerificationCode`` request.
          ALIGN_RATE (int): Required. The Uptime check configuration to retrieve. The format is:

          ::

              projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID]
          ALIGN_INTERPOLATE (int): The protocol for the ``ListUptimeCheckConfigs`` response.
          ALIGN_NEXT_OLDER (int): A filter specifying what ``Service``\ s to return. The filter
          currently supports the following fields:

          ::

              - `identifier_case`
              - `app_engine.module_id`
              - `cloud_endpoints.service`
              - `cluster_istio.location`
              - `cluster_istio.cluster_name`
              - `cluster_istio.service_namespace`
              - `cluster_istio.service_name`

          ``identifier_case`` refers to which option in the identifier oneof is
          populated. For example, the filter ``identifier_case = "CUSTOM"`` would
          match all services with a value for the ``custom`` field. Valid options
          are "CUSTOM", "APP_ENGINE", "CLOUD_ENDPOINTS", and "CLUSTER_ISTIO".
          ALIGN_MIN (int): The protocol for the ``DeleteAlertPolicy`` request.
          ALIGN_MAX (int): The protocol for the ``ListUptimeCheckConfigs`` request.
          ALIGN_MEAN (int): Required. The alerting policy to delete. The format is:

          ::

              projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID]

          For more information, see ``AlertPolicy``.
          ALIGN_COUNT (int): Specifies the alignment of data points in individual time series as
          well as how to combine the retrieved time series across specified
          labels.

          By default (if no ``aggregation`` is explicitly specified), the raw time
          series data is returned.
          ALIGN_SUM (int): A `filter <https://cloud.google.com/monitoring/api/v3/filters>`__
          that identifies which time series should be compared with the threshold.

          The filter is similar to the one that is specified in the
          ```ListTimeSeries``
          request <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list>`__
          (that call is useful to verify the time series that will be retrieved /
          processed) and must specify the metric type and optionally may contain
          restrictions on resource type, resource labels, and metric labels. This
          field may not exceed 2048 Unicode characters in length.
          ALIGN_STDDEV (int): The ``VerifyNotificationChannel`` request.
          ALIGN_COUNT_TRUE (int): Deprecated. Please use the MetricDescriptor.launch_stage instead.
          The launch stage of the metric definition.
          ALIGN_COUNT_FALSE (int): Specifies the alignment of data points in individual time series as
          well as how to combine the retrieved time series together (such as when
          aggregating multiple streams on each resource to a single stream for
          each resource or when aggregating streams across all members of a group
          of resrouces). Multiple aggregations are applied in the order specified.

          This field is similar to the one in the ```ListTimeSeries``
          request <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list>`__.
          It is advisable to use the ``ListTimeSeries`` method when debugging this
          field.
          ALIGN_FRACTION_TRUE (int): Specifies an exponential sequence of buckets that have a width that
          is proportional to the value of the lower bound. Each bucket represents
          a constant relative uncertainty on a specific value in the bucket.

          There are ``num_finite_buckets + 2`` (= N) buckets. Bucket ``i`` has the
          following boundaries:

          ::

             Upper bound (0 <= i < N-1):     scale * (growth_factor ^ i).
             Lower bound (1 <= i < N):       scale * (growth_factor ^ (i - 1)).
          ALIGN_PERCENTILE_99 (int): List ``Service``\ s for this workspace.
          ALIGN_PERCENTILE_95 (int): The fraction of service that must be good in order for this
          objective to be met. ``0 < goal <= 0.999``.
          ALIGN_PERCENTILE_50 (int): Whether the message is an automatically generated map entry type for
          the maps field.

          For maps fields: map<KeyType, ValueType> map_field = 1; The parsed
          descriptor looks like: message MapFieldEntry { option map_entry = true;
          optional KeyType key = 1; optional ValueType value = 2; } repeated
          MapFieldEntry map_field = 1;

          Implementations may choose not to generate the map_entry=true message,
          but use a native map in the target language to hold the keys and values.
          The reflection APIs in such implementations still need to work as if the
          field is a repeated message field.

          NOTE: Do not set the option in .proto files. Always use the maps syntax
          instead. The option should only be implicitly set by the proto compiler
          parser.
          ALIGN_PERCENTILE_05 (int): A `filter <https://cloud.google.com/monitoring/api/v3/filters>`__
          that identifies a time series that should be used as the denominator of
          a ratio that will be compared with the threshold. If a
          ``denominator_filter`` is specified, the time series specified by the
          ``filter`` field will be used as the numerator.

          The filter must specify the metric type and optionally may contain
          restrictions on resource type, resource labels, and metric labels. This
          field may not exceed 2048 Unicode characters in length.
          ALIGN_PERCENT_CHANGE (int): The GCP zone the Uptime check should egress from. Only respected for
          internal Uptime checks, where internal_network is specified.
        """

        ALIGN_NONE = 0
        ALIGN_DELTA = 1
        ALIGN_RATE = 2
        ALIGN_INTERPOLATE = 3
        ALIGN_NEXT_OLDER = 4
        ALIGN_MIN = 10
        ALIGN_MAX = 11
        ALIGN_MEAN = 12
        ALIGN_COUNT = 13
        ALIGN_SUM = 14
        ALIGN_STDDEV = 15
        ALIGN_COUNT_TRUE = 16
        ALIGN_COUNT_FALSE = 24
        ALIGN_FRACTION_TRUE = 17
        ALIGN_PERCENTILE_99 = 18
        ALIGN_PERCENTILE_95 = 19
        ALIGN_PERCENTILE_50 = 20
        ALIGN_PERCENTILE_05 = 21
        ALIGN_PERCENT_CHANGE = 23

    class Reducer(enum.IntEnum):
        """
        A Reducer operation describes how to aggregate data points from multiple
        time series into a single time series, where the value of each data point
        in the resulting series is a function of all the already aligned values in
        the input time series.

        Attributes:
          REDUCE_NONE (int): The ``Service``\ s matching the specified filter.
          REDUCE_MEAN (int): Required. The verification code that was delivered to the channel as
          a result of invoking the ``SendNotificationChannelVerificationCode`` API
          method or that was retrieved from a verified channel via
          ``GetNotificationChannelVerificationCode``. For example, one might have
          "G-123456" or "TKNZGhhd2EyN3I1MnRnMjRv" (in general, one is only
          guaranteed that the code is valid UTF-8; one should not make any
          assumptions regarding the structure or format of the code).
          REDUCE_MIN (int): A group name. The format is:

          ::

              projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]

          Returns groups that are ancestors of the specified group. The groups are
          returned in order, starting with the immediate parent and ending with
          the most distant ancestor. If the specified group has no immediate
          parent, the results are empty.
          REDUCE_MAX (int): The UptimeCheckService API is used to manage (list, create, delete,
          edit) Uptime check configurations in the Stackdriver Monitoring product.
          An Uptime check is a piece of configuration that determines which
          resources and services to monitor for availability. These configurations
          can also be configured interactively by navigating to the [Cloud
          Console] (http://console.cloud.google.com), selecting the appropriate
          project, clicking on "Monitoring" on the left-hand side to navigate to
          Stackdriver, and then clicking on "Uptime".
          REDUCE_SUM (int): Specifies the alignment of data points in individual time series
          selected by ``denominatorFilter`` as well as how to combine the
          retrieved time series together (such as when aggregating multiple
          streams on each resource to a single stream for each resource or when
          aggregating streams across all members of a group of resources).

          When computing ratios, the ``aggregations`` and
          ``denominator_aggregations`` fields must use the same alignment period
          and produce time series that have the same periodicity and labels.
          REDUCE_STDDEV (int): javalite_serializable
          REDUCE_COUNT (int): If there are more results than have been returned, then this field
          is set to a non-empty value. To see the additional results, use that
          value as ``page_token`` in the next call to this method.
          REDUCE_COUNT_TRUE (int): A ``TimeSeriesRatio`` specifies two ``TimeSeries`` to use for
          computing the ``good_service / total_service`` ratio. The specified
          ``TimeSeries`` must have ``ValueType = DOUBLE`` or ``ValueType = INT64``
          and must have ``MetricKind = DELTA`` or ``MetricKind = CUMULATIVE``. The
          ``TimeSeriesRatio`` must specify exactly two of good, bad, and total,
          and the relationship ``good_service + bad_service = total_service`` will
          be assumed.
          REDUCE_COUNT_FALSE (int): javanano_as_lite
          REDUCE_FRACTION_TRUE (int): The comparison to apply between the time series (indicated by
          ``filter`` and ``aggregation``) and the threshold (indicated by
          ``threshold_value``). The comparison is applied on each time series,
          with the time series on the left-hand side and the threshold on the
          right-hand side.

          Only ``COMPARISON_LT`` and ``COMPARISON_GT`` are supported currently.
          REDUCE_PERCENTILE_99 (int): Specifies a set of buckets with arbitrary widths.

          There are ``size(bounds) + 1`` (= N) buckets. Bucket ``i`` has the
          following boundaries:

          ::

             Upper bound (0 <= i < N-1):     bounds[i]
             Lower bound (1 <= i < N);       bounds[i - 1]

          The ``bounds`` field must contain at least one element. If ``bounds``
          has only one element, then there are no finite buckets, and that single
          element is the common boundary of the overflow and underflow buckets.
          REDUCE_PERCENTILE_95 (int): The ``UpdateService`` request.
          REDUCE_PERCENTILE_50 (int): This field represents the pagination token to retrieve the next page
          of results. If the value is empty, it means no further results for the
          request. To retrieve the next page of results, the value of the
          next_page_token is passed to the subsequent List method call (in the
          request message's page_token field).
          REDUCE_PERCENTILE_05 (int): Required. The ``Service`` to draw updates from. The given ``name``
          specifies the resource to update.
        """

        REDUCE_NONE = 0
        REDUCE_MEAN = 1
        REDUCE_MIN = 2
        REDUCE_MAX = 3
        REDUCE_SUM = 4
        REDUCE_STDDEV = 5
        REDUCE_COUNT = 6
        REDUCE_COUNT_TRUE = 7
        REDUCE_COUNT_FALSE = 15
        REDUCE_FRACTION_TRUE = 8
        REDUCE_PERCENTILE_99 = 9
        REDUCE_PERCENTILE_95 = 10
        REDUCE_PERCENTILE_50 = 11
        REDUCE_PERCENTILE_05 = 12


class AlertPolicy(object):
    class ConditionCombinerType(enum.IntEnum):
        """
        Operators for combining conditions.

        Attributes:
          COMBINE_UNSPECIFIED (int): An unspecified combiner.
          AND (int): Required if the condition exists. The unique resource name for this
          condition. Its format is:

          ::

              projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID]

          ``[CONDITION_ID]`` is assigned by Stackdriver Monitoring when the
          condition is created as part of a new or updated alerting policy.

          When calling the ``alertPolicies.create`` method, do not include the
          ``name`` field in the conditions of the requested alerting policy.
          Stackdriver Monitoring creates the condition identifiers and includes
          them in the new policy.

          When calling the ``alertPolicies.update`` method to update a policy,
          including a condition ``name`` causes the existing condition to be
          updated. Conditions without names are added to the updated policy.
          Existing conditions are deleted if they are not updated.

          Best practice is to preserve ``[CONDITION_ID]`` if you make only small
          changes, such as those to condition thresholds, durations, or trigger
          values. Otherwise, treat the change as a new condition and let the
          existing condition be deleted.
          OR (int): The protocol for the ``DeleteUptimeCheckConfig`` request.
          AND_WITH_MATCHING_RESOURCE (int): If specified, contains the range of the population values. The field
          must not be present if the ``count`` is zero.
        """

        COMBINE_UNSPECIFIED = 0
        AND = 1
        OR = 2
        AND_WITH_MATCHING_RESOURCE = 3


class InternalChecker(object):
    class State(enum.IntEnum):
        """
        Operational states for an internal checker.

        Attributes:
          UNSPECIFIED (int): An internal checker should never be in the unspecified state.
          CREATING (int): The ``CreateNotificationChannel`` request.
          RUNNING (int): The ``ListMonitoredResourceDescriptors`` response.
        """

        UNSPECIFIED = 0
        CREATING = 1
        RUNNING = 2


class LabelDescriptor(object):
    class ValueType(enum.IntEnum):
        """
        Value types that can be used as label values.

        Attributes:
          STRING (int): A variable-length string. This is the default.
          BOOL (int): Boolean; true or false.
          INT64 (int): A 64-bit signed integer.
        """

        STRING = 0
        BOOL = 1
        INT64 = 2


class ListTimeSeriesRequest(object):
    class TimeSeriesView(enum.IntEnum):
        """
        Align the time series by using `percentile
        aggregation <https://en.wikipedia.org/wiki/Percentile>`__. The resulting
        data point in each alignment period is the 95th percentile of all data
        points in the period. This aligner is valid for ``GAUGE`` and ``DELTA``
        metrics with distribution values. The output is a ``GAUGE`` metric with
        ``value_type`` ``DOUBLE``.

        Attributes:
          FULL (int): Returns the identity of the metric(s), the time series,
          and the time series data.
          HEADERS (int): Returns the identity of the metric and the time series resource,
          but not the time series data.
        """

        FULL = 0
        HEADERS = 1


class MetricDescriptor(object):
    class MetricKind(enum.IntEnum):
        """
        The kind of measurement. It describes how the data is reported.

        Attributes:
          METRIC_KIND_UNSPECIFIED (int): Do not use this default value.
          GAUGE (int): An instantaneous measurement of a value.
          DELTA (int): The change in a value during a time interval.
          CUMULATIVE (int): A value accumulated over a time interval.  Cumulative
          measurements in a time series should have the same start time
          and increasing end times, until an event resets the cumulative
          value to zero and sets a new start time for the following
          points.
        """

        METRIC_KIND_UNSPECIFIED = 0
        GAUGE = 1
        DELTA = 2
        CUMULATIVE = 3

    class ValueType(enum.IntEnum):
        """
        The value type of a metric.

        Attributes:
          VALUE_TYPE_UNSPECIFIED (int): Do not use this default value.
          BOOL (int): The full REST resource name for this descriptor. The format is:

          ::

              projects/[PROJECT_ID_OR_NUMBER]/notificationChannelDescriptors/[TYPE]

          In the above, ``[TYPE]`` is the value of the ``type`` field.
          INT64 (int): The value is a signed 64-bit integer.
          DOUBLE (int): The value is a double precision floating point number.
          STRING (int): The ``Aligner`` specifies the operation that will be applied to the
          data points in each alignment period in a time series. Except for
          ``ALIGN_NONE``, which specifies that no operation be applied, each
          alignment operation replaces the set of data values in each alignment
          period with a single value: the result of applying the operation to the
          data values. An aligned time series has a single data value at the end
          of each ``alignment_period``.

          An alignment operation can change the data type of the values, too. For
          example, if you apply a counting operation to boolean values, the data
          ``value_type`` in the original time series is ``BOOLEAN``, but the
          ``value_type`` in the aligned result is ``INT64``.
          DISTRIBUTION (int): ``Value`` represents a dynamically typed value which can be either
          null, a number, a string, a boolean, a recursive struct value, or a list
          of values. A producer of value is expected to set one of that variants,
          absence of any variant indicates an error.

          The JSON representation for ``Value`` is JSON value.
          MONEY (int): The value is money.
        """

        VALUE_TYPE_UNSPECIFIED = 0
        BOOL = 1
        INT64 = 2
        DOUBLE = 3
        STRING = 4
        DISTRIBUTION = 5
        MONEY = 6


class NotificationChannel(object):
    class VerificationStatus(enum.IntEnum):
        """
        The authentication parameters to provide to the specified resource
        or URL that requires a username and password. Currently, only `Basic
        HTTP authentication <https://tools.ietf.org/html/rfc7617>`__ is
        supported in Uptime checks.

        Attributes:
          VERIFICATION_STATUS_UNSPECIFIED (int): Sentinel value used to indicate that the state is unknown, omitted, or
          is not applicable (as in the case of channels that neither support
          nor require verification in order to function).
          UNVERIFIED (int): The channel has yet to be verified and requires verification to function.
          Note that this state also applies to the case where the verification
          process has been initiated by sending a verification code but where
          the verification code has not been submitted to complete the process.
          VERIFIED (int): It has been proven that notifications can be received on this
          notification channel and that someone on the project has access
          to messages that are delivered to that channel.
        """

        VERIFICATION_STATUS_UNSPECIFIED = 0
        UNVERIFIED = 1
        VERIFIED = 2


class ServiceLevelObjective(object):
    class View(enum.IntEnum):
        """
        The supported resource types that can be used as values of
        ``group_resource.resource_type``. ``INSTANCE`` includes ``gce_instance``
        and ``aws_ec2_instance`` resource types. The resource types ``gae_app``
        and ``uptime_url`` are not valid here because group checks on App Engine
        modules and URLs are not allowed.

        Attributes:
          VIEW_UNSPECIFIED (int): Same as FULL.
          FULL (int): An SLI measuring performance on a well-known service type.
          Performance will be computed on the basis of pre-defined metrics. The
          type of the ``service_resource`` determines the metrics to use and the
          ``service_resource.labels`` and ``metric_labels`` are used to construct
          a monitoring filter to filter that metric down to just the data relevant
          to this service.
          EXPLICIT (int): Denotes a field as required. This indicates that the field **must**
          be provided as part of the request, and failure to do so will cause an
          error (usually ``INVALID_ARGUMENT``).
        """

        VIEW_UNSPECIFIED = 0
        FULL = 2
        EXPLICIT = 1


class UptimeCheckConfig(object):
    class HttpCheck(object):
        class ContentType(enum.IntEnum):
            """
            The ``GetGroup`` request.

            Attributes:
              TYPE_UNSPECIFIED (int): No content type specified. If the request method is POST, an
              unspecified content type results in a check creation rejection.
              URL_ENCODED (int): If this field is not empty then it must contain the
              ``nextPageToken`` value returned by a previous call to this method.
              Using this field causes the method to return more results from the
              previous method call.
            """

            TYPE_UNSPECIFIED = 0
            URL_ENCODED = 1

        class RequestMethod(enum.IntEnum):
            """
            The HTTP request method options.

            Attributes:
              METHOD_UNSPECIFIED (int): No request method specified.
              GET (int): GET request.
              POST (int): POST request.
            """

            METHOD_UNSPECIFIED = 0
            GET = 1
            POST = 2

    class ContentMatcher(object):
        class ContentMatcherOption(enum.IntEnum):
            """
            Options to perform content matching.

            Attributes:
              CONTENT_MATCHER_OPTION_UNSPECIFIED (int): Required. The monitored resource descriptor to get. The format is:

              ::

                  projects/[PROJECT_ID_OR_NUMBER]/monitoredResourceDescriptors/[RESOURCE_TYPE]

              The ``[RESOURCE_TYPE]`` is a predefined type, such as
              ``cloudsql_database``.
              CONTAINS_STRING (int): The ``CreateGroup`` request.
              NOT_CONTAINS_STRING (int): The ``ListNotificationChannels`` request.
              MATCHES_REGEX (int): The resource type that the annotated field references.

              Example:

              ::

                  message Subscription {
                    string topic = 2 [(google.api.resource_reference) = {
                      type: "pubsub.googleapis.com/Topic"
                    }];
                  }
              NOT_MATCHES_REGEX (int): Deletes a metric descriptor. Only user-created `custom
              metrics <https://cloud.google.com/monitoring/custom-metrics>`__ can be
              deleted.
            """

            CONTENT_MATCHER_OPTION_UNSPECIFIED = 0
            CONTAINS_STRING = 1
            NOT_CONTAINS_STRING = 2
            MATCHES_REGEX = 3
            NOT_MATCHES_REGEX = 4
