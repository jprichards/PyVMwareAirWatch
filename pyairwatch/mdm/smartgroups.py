class SmartGroups(object):
    """
    A class to manage AirWatch Smart Groups.
    """

    def __init__(self, client):
        self.client = client

    def search(self, **kwargs):
        """Returns the Smart Groups details matching the search parameters"""
        response = self._get(path='/smartgroups/search', params=kwargs)
        return response

    def get_id_from_og_id(self, og_id, sg_name):
        """Returns the Smart Group ID for a given SG Name & OG ID"""
        response = self.search(managedbyorganizationgroupid=str(og_id), orderby='smartgroupid')
        for keys in response['SmartGroups']:
            if keys['Name'] == sg_name:
                sg_id = keys.get('SmartGroupID')
                return sg_id

    def _get(self, module='mdm', path=None, version=None, params=None, header=None):
        """GET requests for the /System/Groups module."""
        response = self.client.get(module=module, path=path, version=version, params=params, header=header)
        return response

    def _post(self, module='mdm', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /System/Groups module."""
        response = self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
        return response
