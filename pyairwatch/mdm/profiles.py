class Profiles(object):
    """
    A class to manage V2 API's for AirWatch Profiles Management
    """

    def __init__(self, client):
        self.client = client

    def search(self, **kwargs):
        """
        Returns the Profile information matching the search parameters.

        /api/mdm/profiles/search?{params}

        PARAMS:
            type={type}
            profilename={profilename}
            organizationgroupid={organizationgroupid}
            platform={platform}
            status={status}
            ownership={ownership}
        """
        response = self._get(path='/profiles/search', params=kwargs)
        page = 1
        while isinstance(response, dict) and page * response["PageSize"] < response["Total"]:
            kwargs["page"] = page
            new_page = self._get(path='/profiles/search', params=kwargs)
            if isinstance(new_page, dict):
                response["Profiles"].append(new_page.get("Profiles", []))
                response["Page"] = page
            page += 1
        return response

    def _get(self, module='mdm', path=None, version=None, params=None, header=None):
        """GET requests for the /MDM/Profiles module."""
        response = self.client.get(module=module, path=path, version=version, params=params, header=header)
        return response

    def _post(self, module='mdm', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /MDM/Profiles module."""
        response = self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
        return response
