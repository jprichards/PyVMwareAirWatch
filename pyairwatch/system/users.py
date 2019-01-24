from .system import System


class Users(System):

    def __init__(self, client):
        System.__init__(self, client)

    # UNTESTED
    def search(self, **kwargs):
        """
        Returns the Enrollment User's details matching the search parameters

        /api/system/users/search?{params}

        PARAMS:
            username={username}
            firstname={firstname}
            lastname={lastname}
            email={email}
            organizationgroupid={locationgroupid}
            role={role}
        """
        return System._get(path='/users/search', params=kwargs)
