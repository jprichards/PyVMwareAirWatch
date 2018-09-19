import base64
import json
import logging
import requests
from .mam.apps import Apps
from .mam.blobs import Blobs
from .mam.internalapps import InternalApps
from .mdm.devices import Devices
from .mdm.profiles import Profiles
from .mdm.smartgroups import SmartGroups
from .mdm.tags import Tags
from .system.admins import Admins
from .system.groups import Groups
from .system.users import Users
from .system.featureflag import FeatureFlag
from .mdm.ldap import LDAP


# Enabling debugging at http.client level (requests->urllib3->http.client)
# you will see the REQUEST, including HEADERS and DATA, and RESPONSE with
# HEADERS but without DATA.
# the only thing missing will be the response.body which is not logged.
try:
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection
HTTPConnection.debuglevel = 0

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True



class AirWatchAPIError(Exception):
    def __init__(self, json_response=None):
        if json_response is None:
            pass
        else:
            self.response = json_response
            self.error_code = json_response.get('errorCode')
            self.error_msg = str(json_response.get('message'))
            if self.error_code is None:
                self.error_code = 0
                self.error_msg = 'Unknown API error occurred'

    def __str__(self):
        return 'Error #{}: {}'.format(self.error_code, self.error_msg)


class AirWatchAPI(object):
    def __init__(self, env, apikey, username, password):
            self.env = env
            self.apikey = apikey
            self.username = username
            self.password = password
            self.groups = Groups(self)
            self.smartgroups = SmartGroups(self)
            self.devices = Devices(self)
            self.profiles = Profiles(self)
            self.tags = Tags(self)
            self.admins = Admins(self)
            self.users = Users(self)
            self.featureflag = FeatureFlag(self)
            self.ldap = LDAP(self)

    def get(self, module, path, version=None, params=None, header=None, timeout=30):
        """Sends a GET request to the API. Returns the response object."""
        if header is None:
            header = {}
        header.update(self._build_header(self.username, self.password, self.apikey))
        header.update({'Content-Type': 'application/json'})
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            r = requests.get(endpoint, params=params, headers=header, timeout=timeout)
            r = self._check_for_error(r)
            return r
        except AirWatchAPIError as e:
            raise e

    def post(self, module, path, version=None, params=None, data=None, json=None, header=None, timeout=30):
        """Sends a POST request to the API. Returns the response object."""
        if header is None:
            header = {}
        header.update(self._build_header(self.username, self.password, self.apikey))
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            r = requests.post(endpoint, params=params, data=data, json=json, headers=header, timeout=timeout)
            r = self._check_for_error(r)
            return r
        except AirWatchAPIError as e:
            raise e

    def put(self, module, path, version=None, params=None, data=None, json=None, header=None, timeout=30):
        """Sends a PUT request to the API. Returns the response object."""
        if header is None:
            header = {}
        header.update(self._build_header(self.username, self.password, self.apikey))
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            r = requests.put(endpoint, params=params, data=data, json=json, headers=header, timeout=timeout)
            r = self._check_for_error(r)
            return r
        except AirWatchAPIError as e:
            raise e

    #NOQA
    def delete(self, module, path, version=None, params=None, header=None, timeout=30):
        """Sends a DELETE request to the API. Returns the response object."""
        if header is None:
            header = {}
        header.update(self._build_header(self.username, self.password, self.apikey))
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            r = requests.delete(endpoint, params=params, headers=header, timeout=timeout)
            r = self._check_for_error(r)
            return r
        except AirWatchAPIError as e:
            raise e

    @staticmethod
    def _check_for_error(response):
        """Checks the response for json data, then for an error, then for a status code"""
        if response.headers.get('Content-Type') in ('application/json', 'application/json; charset=utf-8'):
            json = response.json()
            if json.get('errorCode'):
                raise AirWatchAPIError(json_response=json)
            else:
                return json
        else:
            return response.status_code

    @staticmethod
    def _build_endpoint(base_url, module, path=None, version=None):
        """Builds the full url endpoint for the API request"""
        if not base_url.startswith('https://'):
            base_url = 'https://' + base_url
        if base_url.endswith('/'):
            base_url = base_url[:-1]
        if version is None:
            url = '{}/api/{}'.format(base_url, module)
        else:
            url = '{}/api/v{}/{}'.format(base_url, version, module)
        if path:
            if path.startswith('/'):
                return url + '{}'.format(path)
            else:
                return url + '/{}'.format(path)
        return url


    @staticmethod
    def _build_header(username, password, token, accept='application/json'):
        """Build the header with base64 login, AW API token, and accept a json response"""
        hashed_auth = base64.b64encode('{}:{}'.format(username, password))
        header = {
                  'Authorization': 'Basic {}'.format(hashed_auth.encode('utf-8')),
                  'aw-tenant-code': token.encode('utf-8'),
                  'Accept': accept
                 }
        return header
