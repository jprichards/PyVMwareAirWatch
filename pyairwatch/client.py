import base64
import json
import requests

class AirWatchAPIError(Exception):
    pass

class AirWatchAPI(object):
    def __init__(self, env, apikey, username, password):
            self.env = env
            self.apikey = apikey
            self.username = username
            self.password = password

    def get(self, module, path, version=None, params=None, header=None, timeout=30):
        """Sends a GET request to the API. Returns the response object."""
        if header is None:
            header = {}
        header.update(self._build_header(self.username, self.password, self.apikey))
        header.update({'Content-Type': 'application/json'})
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            r = requests.get(endpoint, params=params, headers=header, timeout=timeout)
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
            return r
        except AirWatchAPIError as e:
            raise e

    @staticmethod
    def _build_endpoint(base_url, module, path=None, version=None):
        """Builds the full url endpoint for the API request"""
        if base_url.startswith('https://') is not True:
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
        hashed_auth = base64.b64encode('{}:{}'.format(username, password))
        header = {
                  'Authorization': 'Basic {}'.format(hashed_auth.encode('utf-8')),
                  'aw-tenant-code': token.encode('utf-8'),
                  'Accept': accept
                 }
        return header
