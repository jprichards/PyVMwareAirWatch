class Users(object):

    def __init__(self, client):
        self.client = client

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
        response = self._get(path='/users/search', params=kwargs)
        return response

    def get_id_from_username(self, username):
        """Returns the User ID for a given Username"""
        userID = ''
        response = self.search(username=str(username))
        # search does not do an exact string match, so we need to do it here
        if len(response['Users']) > 1:
            for u in response['Users']:
                if username == u['UserName']:
                    #If there are multiple users with the same exact username it picks the first one
                    userID = u['Id']['Value']
                    break
                else:
                    continue
        else:
            userID = response['Users'][0]['Id']['Value']
        return userID

    def _get(self, module='system', path=None, version=None, params=None, header=None):
        """GET requests for the /System/Users module."""
        response = self.client.get(module=module, path=path, version=version, params=params, header=header)
        return response

    def _post(self, module='system', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /System/Users module."""
        response = self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
        return response
