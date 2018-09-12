class InternalApps(object):
    """
    A class to manage Internal Applications
    """

    def __init__(self, client):
        self.client = client

    def _get(self, module='mam/apps', path=None, version=None, params=None, header=None):
        """GET requests for the /MAM/apps/internal module."""
        response = self.client.get(module=module, path=path, version=version, params=params, header=header)
        return response

    def _post(self, module='mam/apps', path=None, version=None, params=None, data=None, json=None, header=None):
        """Post requests for the /MAM/apps/internal module."""
        response = self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
