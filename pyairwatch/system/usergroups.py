class UserGroups(object):
    """
    A class to manage all core functionalities for AirWatch Organization Groups.
    """
    jheader = {'Content-Type': 'application/json'}

    def __init__(self, client):
        self.client = client

    def search(self, **kwargs):
        """Returns the Users Groups matching the search parameters."""
        response = self._get(path='/usergroups/search', params=kwargs)
        return response

    def search_users(self, id, **kwargs):
        """Retrieves list of users from the provided user group id."""
        response = self._get(path='/usergroups/{}/users'.format(id), params=kwargs)
        return response

    def _get(self, module='system', path=None, version=None, params=None, header=None):
        """GET requests for the /System/UsersGroups module."""
        response = self.client.get(module=module, path=path, version=version, params=params, header=header)
        return response

    def _post(self, module='system', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /System/UsersGroups module."""
        response = self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
        return response
