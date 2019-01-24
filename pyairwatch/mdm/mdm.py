class MDM(object):
    """
    Base MDM class
    """
    def __init__(self, client):
        self.client = client

    def _get(self, module='mdm', path=None,
             version=None, params=None, header=None):
        """GET requests for base mdm endpoints"""
        return self.client.get(module=module, path=path,
                               version=version, params=params, header=header)

    def _post(self, module='mdm', path=None,
              version=None, params=None, data=None, json=None, header=None):
        """POST requests for base mdm endpoints"""
        return self.client.post(module=module, path=path, version=version,
                                params=params, data=data,
                                json=json, header=header)

    def _put(self, module='mdm', path=None,
             version=None, params=None, data=None, json=None, header=None):
        """PUT requests for base mdm endpoints"""
        return self.client.put(module=module, path=path, version=version,
                               params=params, data=data,
                               json=json, header=header)
