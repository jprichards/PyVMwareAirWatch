class Admins(object):
    def __init__(self, client):
        self.client = client

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
        response = self._get(path="/admins/search", params=kwargs)
        page = 1
        while (
            isinstance(response, dict)
            and page * response["PageSize"] < response["Total"]
        ):
            kwargs["page"] = page
            new_page = self._get(path="/admins/search", params=kwargs)
            if isinstance(new_page, dict):
                response["Admins"].append(new_page.get("Admins", []))
                response["Page"] = page
            page += 1
        return response

    def _get(self, module="system", path=None, version=None, params=None, header=None):
        """GET requests for the /System/Admins module."""
        response = self.client.get(
            module=module, path=path, version=version, params=params, header=header
        )
        return response

    def _post(
        self,
        module="system",
        path=None,
        version=None,
        params=None,
        data=None,
        json=None,
        header=None,
    ):
        """POST requests for the /System/Admins module."""
        response = self.client.post(
            module=module,
            path=path,
            version=version,
            params=params,
            data=data,
            json=json,
            header=header,
        )
        return response
