#!/usr/bin/env python
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Sample command-line program for retrieving Stackdriver Monitoring API V3
data.

See README.md for instructions on setting up your development environment.

To run locally:

    python list_resources.py --project_id=<YOUR-PROJECT-ID>

"""

# [START all]
import argparse
import datetime
import pprint

from apiclient import discovery
from oauth2client.client import GoogleCredentials


def format_rfc3339(datetime_instance):
    """Formats a datetime per RFC 3339."""
    return datetime_instance.isoformat("T") + "Z"


def get_start_time():
    """ Returns the start time for the 5-minute window to read the custom
    metric from within.
    :return: The start time to begin reading time series values, picked
    arbitrarily to be an hour ago and 5 minutes
    """
    # Return an hour ago - 5 minutes
    start_time = (datetime.datetime.utcnow() -
                  datetime.timedelta(hours=1, minutes=5))
    return format_rfc3339(start_time)


def get_end_time():
    """ Returns the end time for the 5-minute window to read the custom metric
    from within.
    :return: The start time to begin reading time series values, picked
    arbitrarily to be an hour ago, or 5 minutes from the start time.
    """
    end_time = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
    return format_rfc3339(end_time)


def list_monitored_resource_descriptors(client, project_resource):
    """Query the projects.monitoredResourceDescriptors.list API method.
    This lists all the resources available to be monitored in the API.
    """
    request = client.projects().monitoredResourceDescriptors().list(
        name=project_resource)
    response = request.execute()
    print('list_monitored_resource_descriptors response:\n{}'.format(
        pprint.pformat(response)))


def list_metric_descriptors(client, project_resource, metric):
    """Query to MetricDescriptors.list
    This lists the metric specified by METRIC.
    """
    request = client.projects().metricDescriptors().list(
        name=project_resource,
        filter='metric.type="{}"'.format(metric))
    response = request.execute()
    print(
        'list_metric_descriptors response:\n{}'.format(
            pprint.pformat(response)))


def list_timeseries(client, project_resource, metric):
    """Query the TimeSeries.list API method.
    This lists all the timeseries created between START_TIME and END_TIME.
    """
    request = client.projects().timeSeries().list(
        name=project_resource,
        filter='metric.type="{}"'.format(metric),
        pageSize=3,
        interval_startTime=get_start_time(),
        interval_endTime=get_end_time())
    response = request.execute()
    print('list_timeseries response:\n{}'.format(pprint.pformat(response)))


def get_client():
    """Builds an http client authenticated with the service account
    credentials."""
    credentials = GoogleCredentials.get_application_default()
    client = discovery.build('monitoring', 'v3', credentials=credentials)
    return client


def main(project_id):
    project_resource = "projects/{}".format(project_id)
    client = get_client()
    list_monitored_resource_descriptors(client, project_resource)
    # Metric to list
    metric = 'compute.googleapis.com/instance/cpu/usage_time'
    list_metric_descriptors(client, project_resource, metric)
    list_timeseries(client, project_resource, metric)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--project_id', help='Project ID you want to access.', required=True)

    args = parser.parse_args()
    main(args.project_id)

# [END all]
