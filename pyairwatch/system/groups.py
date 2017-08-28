class Groups(object):
    """
    A class to manage all core functionalities for AirWatch Organization Groups.
    """
    jheader = {'Content-Type': 'application/json'}

    def __init__(self, client):
        self.client = client

    def search(self, **kwargs):
        """Returns the Groups matching the search parameters."""
        response = self._get(path='/groups/search', params=kwargs)
        return response

    def get_id_from_groupid(self, groupid):
        """Returns the OG ID for a given Group ID"""
        response = self.search(groupid=str(groupid))
        return response['LocationGroups'][0]['Id']['Value']

    def create(self, parent_id, ogdata):
        """Creates a Group and returns the new ID."""
        response = self._post(path='/groups/{}'.format(parent_id), data=ogdata, header=jheader)
        return response

    def _get(self, module='system', path=None, version=None, params=None, header=None):
        """GET requests for the /System/Groups module."""
        response = self.client.get(module=module, path=path, version=version, params=params, header=header)
        return response

    def _post(self, module='system', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /System/Groups module."""
        response = self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
        return response
