class MAM(object):
    """
    Application management
    """

    def __init__(self, client):
        self.client = client

    def _get(self, path=None, version=None, params=None,
             header=None):
        """GET requests for base mam endpoints"""
        return self.client.get(module='mam', path=path,
                               version=version, params=params, header=header)

    def _post(self, path=None, version=None, params=None,
              data=None, json=None, header=None):
        """POST requests for base mam endpoints"""
        return self.client.post(module='mam', path=path, version=version,
                                params=params, data=data,
                                json=json, header=header)

    def _put(self, path=None, version=None, params=None,
             data=None, json=None, header=None):
        """PUT requests for base mam endpoints"""
        return self.client.put(module='mam', path=path, version=version,
                               params=params, data=data,
                               json=json, header=header)

    def _patch(self, path=None, version=None, params=None,
               data=None, json=None, header=None):
        """Patch requests for base mam endpoints"""
        return self.client.patch(module='mam', path=path, version=version,
                               params=params, data=data,
                               json=json, header=header)

    def _delete(self, path=None, version=None, params=None, header=None):
        return self.client.delete(module='mam', path=path, version=version, params=params, header=header)