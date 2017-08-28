class Groups(object):
    """
    A class to manage all core functionalities for AirWatch Organization Groups.
    """

    def __init__(self, client):
        self.client = client

    def search(self, **kwargs):
        """Returns the Groups matching the search parameters."""
        response = self._get(path='/groups/search', params=kwargs)
        return response

    def create(self, parent_id, ogdata):
        """Creates a Group and returns the new ID."""
        response = self._post(path='/groups/{}'.format(parent_id), data=ogdata, header={'Content-Type': 'application/json'})
        return response

    def _get(self, module='system', path=None, version=None, params=None, header=None):
        """GET requests for the /System/Groups module."""
        if params is None:
            params = {}
        response = self.client.get(module=module, path=path, version=version, params=params, header=header)
        return response

    def _post(self, module='system', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /System/Groups module."""
        if params is None:
            params = {}
        response = self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
        return response
