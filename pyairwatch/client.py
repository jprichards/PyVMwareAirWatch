from __future__ import print_function, absolute_import
import base64
import logging
import requests
from pyairwatch.error import AirWatchAPIError
from pyairwatch.mdm.devices import Devices
from pyairwatch.mdm.profiles import Profiles
from pyairwatch.mdm.smartgroups import SmartGroups
from pyairwatch.mdm.tags import Tags
from pyairwatch.mdm.ldap import LDAP
from pyairwatch.mdm.network import Network
from pyairwatch.system.admins import Admins
from pyairwatch.system.groups import Groups
from pyairwatch.system.usergroups import UserGroups
from pyairwatch.system.users import Users
from pyairwatch.system.featureflag import FeatureFlag
from pyairwatch.system.info import Info
from pyairwatch.mam.application import Application
from pyairwatch.mam.vpp import VPP


# Enabling debugging at http.client level (requests->urllib3->http.client)
# you will see the REQUEST, including HEADERS and DATA, and RESPONSE with
# HEADERS but without DATA.
# the only thing missing will be the response.body which is not logged.
try:
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection
HTTPConnection.debuglevel = 0

#todo: programing using library should be able to set logging level
#todo: Implement logging to using config https://docs.python.org/3/howto/logging.html#configuring-logging
#todo: sett logging correclty for a library https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


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
        self.usergroups = UserGroups(self)
        self.featureflag = FeatureFlag(self)
        self.ldap = LDAP(self)
        self.info = Info(self)
        self.network = Network(self)
        self.application = Application(self)
        self.vpp = VPP(self)

    def get(self, module, path, version=None, params=None, header=None,
            timeout=30):
        """
        Sends a GET request to the API. Returns the response object.
        """
        if header is None:
            header = {}
        header.update(self._build_header(self.username, self.password,
                                         self.apikey))
        header.update({'Content-Type': 'application/json'})
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            r = requests.get(endpoint, params=params, headers=header,
                             timeout=timeout)
            r = self._check_for_error(r)
            return r
        except AirWatchAPIError as e:
            raise e

    def post(self, module, path, version=None, params=None, data=None,
             json=None, header=None, timeout=30):
        """
        Sends a POST request to the API. Returns the response object.
        """
        if header is None:
            header = {}
        header.update(self._build_header(self.username, self.password,
                                         self.apikey))
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            r = requests.post(endpoint, params=params, data=data, json=json,
                              headers=header, timeout=timeout)
            r = self._check_for_error(r)
            return r
        except AirWatchAPIError as e:
            raise e

    def put(self, module, path, version=None, params=None, data=None,
            json=None, header=None, timeout=30):
        """
        Sends a PUT request to the API. Returns the response object.
        """
        if header is None:
            header = {}
        header.update(self._build_header(self.username, self.password,
                                         self.apikey))
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            r = requests.put(endpoint, params=params, data=data, json=json,
                             headers=header, timeout=timeout)
            r = self._check_for_error(r)
            return r
        except AirWatchAPIError as e:
            raise e

    def patch(self, module, path, version=None, params=None, data=None,
              json=None, header=None, timeout=30):
        """
        Sends a Patch request to the API. Returns the response object.
        """
        if header is None:
            header = {}
        header.update(self._build_header(self.username, self.password,
                                         self.apikey))
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            r = requests.patch(endpoint, params=params, data=data, json=json,
                               headers=header, timeout=timeout)
            r = self._check_for_error(r)
            return r
        except AirWatchAPIError as e:
            raise e

    # NOQA

    def delete(self, module, path, version=None, params=None, header=None,
               timeout=30):
        """
        Sends a DELETE request to the API. Returns the response object.
        """
        if header is None:
            header = {}
        header.update(self._build_header(self.username, self.password,
                                         self.apikey))
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            r = requests.delete(endpoint, params=params, headers=header,
                                timeout=timeout)
            r = self._check_for_error(r)
            return r
        except AirWatchAPIError as e:
            raise e

    @staticmethod
    def _check_for_error(response):
        """
        Checks the response for json data, then for an error, then for
        a status code
        """
        if response.headers.get('Content-Type') in ('application/json',
                                                    'application/json; charset=utf-8'):
            json = response.json()
            if json.get('errorCode'):
                raise AirWatchAPIError(json_response=json)
            else:
                return json
        else:
            return response.status_code

    @staticmethod
    def _build_endpoint(base_url, module, path=None, version=None):
        """
        Builds the full url endpoint for the API request
        """
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
        """
        Build the header with base64 login, AW API token,
        and accept a json response
        """
        hashed_auth = base64.b64encode((username + ':' + password).encode('utf8')).decode("utf-8")
        header = {
            'Authorization': 'Basic {}'.format(hashed_auth),
            'aw-tenant-code': token,
            'Accept': accept
        }
        return header
