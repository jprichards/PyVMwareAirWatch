class Devices(object):
    """
    A class to manage functionalities of Mobile Device Management (MDM).
    """

    def __init__(self, client):
        self.client = client

    def _get(self, module='mdm', path=None, version=None, params=None, header=None):
        """GET requests for the /MDM/Devices module."""
        response = self.client.get(module=module, path=path, version=version, params=params, header=header)
        return response

    def _post(self, module='mdm', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /MDM/Devices module."""
        response = self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
        return response
