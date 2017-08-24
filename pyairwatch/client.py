import base64
import json
import requests


class AirWatchAPI(object):
    def __init__(self, env, apikey, username, password):
            self.env = env
            self.apikey = apikey
            self.username = username
            self.password = password

    def get(self, module, path, **params, header=None):
        """
        Sents a POST request to the API.
        Returns the JSON output, or the HTTP response status code if no JSON is returned.
        """

    def post(self, module, path, data=None, header=None):
        """
        Sents a GET request to the API.
        Returns the JSON output, or the HTTP response status code if no JSON is returned.
        """

    @staticmethod
    def _build_endpoint(base_url, module, version=None, path=None):
        """Builds the full url endpoint for the API request"""
        if base_url.startswith('https://') is not True:
            base_url = 'https://' + base_url
        if base_url.endswith('/'):
            base_url = base_url[:-1]
        if version is None:
            url = '{0}/api/{1}'.format(base_url, module)
        else:
            url = '{0}/api/v{1}/{2}'.format(base_url, version, module)
        if path:
            return url + '{0}'.format(path)
        return url


    @staticmethod
    def _build_header(username, password, token, accept='application/json'):
        hashed_auth = base64.b64encode('%s:%s' % (username, password))
        header = {'Authorization': 'Basic %s' % hashed_auth.encode('utf-8'),
                  'aw-tenant-code': token.encode('utf-8'),
                  'Accept': accept}
        return header

    def validate(self):
        """
         Tries to validate the user credentials.
         Returns True if successful, False if validation fails.
        """
