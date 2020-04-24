from .system import System


class Admins(System):

    def __init__(self, client):
        System.__init__(self, client)

    def search(self, **kwargs):
        """
        Returns the Admin User's details matching the search parameters

        /api/system/admins/search?{params}

        PARAMS:
            username={username}
            firstname={firstname}
            lastname={lastname}
            email={email}
            organizationgroupid={locationgroupid}
            role={role}
        """
        response = System._get(self, path='/admins/search', params=kwargs)
        return response

    def create_adim_v1(self, user_data):
        """
        Performs necessary checks and Create a new basic Admin user.
        """
        path = '/admins/addadminuser'
        response = System._post(self, path=path, data=user_data)
        return response
