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
        page = 1
        while isinstance(response, dict) and page * response["PageSize"] < response["Total"]:
            kwargs["page"] = page
            new_page = self._get(path='/groups/search', params=kwargs)
            if isinstance(new_page, dict):
                response["Groups"].append(new_page.get("Groups", []))
                response["Page"] = page
            page += 1
        return response

    def get_id_from_groupid(self, groupid):
        """Returns the OG ID for a given Group ID"""
        response = self.search(groupid=str(groupid))
        return response['LocationGroups'][0]['Id']['Value']

    def create(self, parent_id, ogdata):
        """Creates a Group and returns the new ID."""
        response = self._post(path='/groups/{}'.format(parent_id), data=ogdata, header=self.jheader)
        return response

    def create_customer_og(self, groupid, name=None):
        """Creates a Customer type OG, with a given Group ID and Name, and returns the new ID"""
        import json
        new_og = {'GroupId': str(groupid),
                  'Name': str(name),
                  'LocationGroupType': 'Customer'}
        if name is None:
            new_og['Name'] = str(groupid)
        response = self.create(parent_id=7, ogdata=json.dumps(new_og))
        return response.get('Value')

    def create_child_og(self, parent_groupid, groupid, og_type=None, name=None):
        """Creates a Child OG for a given Parent Group ID, with a given Type, Group ID, and Name, and returns the new ID"""
        import json
        pid = self.get_id_from_groupid(parent_groupid)
        new_og = {'GroupId': str(groupid),
                  'Name': str(name),
                  'LocationGroupType': str(og_type)}
        if name is None:
            new_og['Name'] = str(groupid)
        if og_type is None:
            new_og['LocationGroupType'] = 'Container'
        response = self.create(parent_id=pid, ogdata=json.dumps(new_og))
        return response.get('Value')

    def _get(self, module='system', path=None, version=None, params=None, header=None):
        """GET requests for the /System/Groups module."""
        response = self.client.get(module=module, path=path, version=version, params=params, header=header)
        return response

    def _post(self, module='system', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /System/Groups module."""
        response = self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
        return response
