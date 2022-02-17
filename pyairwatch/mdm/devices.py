class Devices(object):
    """
    A class to manage functionalities of Mobile Device Management (MDM).
    """

    def __init__(self, client):
        self.client = client

    def search(self, **kwargs):
        """Returns the Device information matching the search parameters."""
        response = self._get(path="/devices", params=kwargs)
        return response

    def search_all(self, **kwargs):
        """Returns the Devices matching the search parameters."""
        response = self._get(path="/devices/search", params=kwargs)
        page = 1
        while (
            isinstance(response, dict)
            and page * response["PageSize"] < response["Total"]
        ):
            kwargs["page"] = page
            new_page = self._get(path="/devices/search", params=kwargs)
            if isinstance(new_page, dict):
                response["Devices"].append(new_page.get("Devices", []))
                response["Page"] = page
            page += 1

        return response

    def get_details_by_alt_id(
        self, serialnumber=None, macaddress=None, udid=None, imeinumber=None, easid=None
    ):
        """Returns the Device information matching the search parameters."""
        params = {}
        if serialnumber:
            response = self.search(searchby="Serialnumber", id=str(serialnumber))
        elif macaddress:
            response = self.search(searchby="Macaddress", id=str(macaddress))
        elif udid:
            response = self.search(searchby="Udid", id=str(udid))
        elif imeinumber:
            response = self.search(searchby="ImeiNumber", id=str(imeinumber))
        elif easid:
            response = self.search(searchby="EasId", id=str(easid))
        else:
            return None
        return response

    def get_id_by_alt_id(
        self, serialnumber=None, macaddress=None, udid=None, imeinumber=None, easid=None
    ):
        if serialnumber:
            response = self.search(searchby="Serialnumber", id=str(serialnumber))
        elif macaddress:
            response = self.search(searchby="Macaddress", id=str(macaddress))
        elif udid:
            response = self.search(searchby="Udid", id=str(udid))
        elif imeinumber:
            response = self.search(searchby="ImeiNumber", id=str(imeinumber))
        elif easid:
            response = self.search(searchby="EasId", id=str(easid))
        else:
            return None
        return response["Id"]["Value"]

    def _get(self, module="mdm", path=None, version=None, params=None, header=None):
        """GET requests for the /MDM/Devices module."""
        response = self.client.get(
            module=module, path=path, version=version, params=params, header=header
        )
        return response

    def _post(
        self,
        module="mdm",
        path=None,
        version=None,
        params=None,
        data=None,
        json=None,
        header=None,
    ):
        """POST requests for the /MDM/Devices module."""
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
