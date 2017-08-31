class Tags(object):
    """A class to manage various AirWatch device tag functionalities"""

    def __init__(self, client):
        self.client = client

    def get_id_by_name(self, name, og_id):
        # mdm/tags/search?name={name}
        response = self._get(path='/tags/search', params={'name':str(name), 'organizationgroupid':str(og_id)})
        print response

    def _get(self, module='mdm', path=None, version=None, params=None, header=None):
        """GET requests for the /MDM/Tags module."""
        response = self.client.get(module=module, path=path, version=version, params=params, header=header)
        return response

    def _post(self, module='mdm', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /MDM/Tags module."""
        response = self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
        return response
