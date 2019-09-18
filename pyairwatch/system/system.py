class System(object):
    """
    Base System class
    """
    def __init__(self, client):
        self.client = client

    def _get(self, module='system', path=None,
             version=None, params=None, header=None):
        """
        GET requests for base system endpoints
        """
        return self.client.get(module=module, path=path,
                               version=version, params=params, header=header)

    def _post(self, module='system', path=None,
              version=None, params=None, data=None, json=None, header=None):
        """POST requests"""
        return self.client.post(module=module, path=path, version=version,
                                params=params, data=data,
                                json=json, header=header)

    def _post_no_error_check(self, module='system', path=None,
                             version=None, params=None, data=None,
                             json=None, header=None):
        """POST requests with no error check when none json is returned"""
        return self.client.post_no_error_check(module=module, path=path,
                                               version=version, params=params,
                                               data=data,
                                               json=json, header=header)

    def _put(self, module='system', path=None,
             version=None, params=None, data=None, json=None, header=None):
        """PUT requests"""
        return self.client.put(module=module, path=path, version=version,
                               params=params, data=data,
                               json=json, header=header)
