from .system import System


class UserGroups(System):
    """
    A class to manage all core functionalities for AirWatch Organization Groups.
    """
    jheader = {'Content-Type': 'application/json'}

    def __init__(self, client):
        System.__init__(self, client)

    def search(self, **kwargs):
        """Returns the Users Groups matching the search parameters."""
        response = System._get(self, path='/usergroups/search', params=kwargs)
        return response

    def search_users(self, id, **kwargs):
        """Retrieves list of users from the provided user group id."""
        response = System._get(self, path='/usergroups/{}/users'.format(id),
                               params=kwargs)
        return response
