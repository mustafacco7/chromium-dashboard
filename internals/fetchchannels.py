# -*- coding: utf-8 -*-
# Copyright 2021 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License")
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

import json
import logging
import requests

from framework import rediscache
# Note: this file cannot import core_models because it would be circular.
import settings


OMAHA_URL_TEMPLATE = (
    'https://versionhistory.googleapis.com'
    '/v1/chrome/platforms/win/channels/%s/versions/?pageSize=1')

# Expected response for the "stable" channel looks like:
# {
#   "versions": [
#     {
#       "name": "chrome/platforms/win/channels/stable/versions/119.0.6045.160",
#       "version": "119.0.6045.160"
#     }
#   ],
#   "nextPageToken": "652474890"
# }
# We really only need the version string.


def get_channel_version(channel):
  """Return the version string that is live on the given channel."""
  url = OMAHA_URL_TEMPLATE % channel
  logging.info('fetching %s' % url)
  result = requests.get(url)
  if result.status_code != 200:
    logging.info('Could not fetch channel info for %s', channel)
    return '0.0'
  channel_info = json.loads(result.content)
  logging.info('channel_info is %r', channel_info)
  version = channel_info['versions'][0]['version']
  return version


def get_omaha_data():
  omaha_data = rediscache.get('omaha_data')

  if omaha_data is None:
    win_versions = [
        {'channel': 'stable', 'version': get_channel_version('stable')},
        {'channel': 'beta', 'version': get_channel_version('beta')},
        {'channel': 'dev', 'version': get_channel_version('dev')},
        ]
    omaha_info = [{'versions': win_versions}]
    omaha_data = json.dumps(omaha_info)
    rediscache.set('omaha_data', omaha_data, time=86400) # cache for 24hrs.

  return json.loads(omaha_data)


SCHEDULE_CACHE_TIME = 60 * 60  # 1 hour


def fetch_chrome_release_info(version):
  key = 'chromerelease|%s' % version

  data = rediscache.get(key)
  if data is None:
    url = ('https://chromiumdash.appspot.com/fetch_milestone_schedule?'
           'mstone=%s' % version)
    result = requests.get(url, timeout=60)
    if result.status_code == 200:
      try:
        logging.info(
            'result.content is:\n%s', result.content[:settings.MAX_LOG_LINE])
        result_json = json.loads(result.content)
        if 'mstones' in result_json:
          data = result_json['mstones'][0]
          del data['owners']
          del data['feature_freeze']
          del data['ldaps']
          rediscache.set(key, data, time=SCHEDULE_CACHE_TIME)
      except ValueError:
        pass  # Handled by next statement

    if not data:
      data = {
          'stable_date': None,
          'earliest_beta': None,
          'latest_beta': None,
          'mstone': version,
          'version': version,
      }
      # Note: we don't put placeholder data into redis.

  return data
