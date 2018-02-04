class Tags(object):
    """A class to manage various AirWatch device tag functionalities"""

    def __init__(self, client):
        self.client = client

    def get_id_by_name(self, name, og_id):
        # /tags/search?name={name}
        response = self._get(path='/tags/search', params={'name':str(name), 'organizationgroupid':str(og_id)})
        for t in response['Tags']:
            if t['TagName'] == str(name):
                return t['Id']['Value']

    #NOQA
    def get_devices_by_tag_id(self, tag_id, last_seen=None):
        # /tags/{tagid}/devices?LastSeen={lastseen}
        response = self._get(path='/tags/{}/devices'.format(tag_id), params={'LastSeen':str(lastseen)})
        return response

    #NOQA
    def add_devices_to_tag(self, tag_id, devices):
        # /tags/{tagid}/adddevices
        payload = {'BulkValues':{'Value':[]}}
        for i in devices:
            payload['BulkValues']['Value'].append(i)
        response = self._post(path='/tags/{}/adddevices'.format(tag_id), data=payload)
        return response

    #NOQA
    def remove_devices_from_tag(self, tag_id, devices):
        # /tags/{tagid}/removedevices
        payload = {'BulkValues':{'Value':[]}}
        for i in devices:
            payload['BulkValues']['Value'].append(i)
        response = self._post(path='/tags/{}/removedevices'.format(tag_id), data=payload)
        return response

    #NOQA
    def delete_tag(self, tag_id):
        # /tags/{tagid}
        response = self._delete(path='/tags/{}'.format(tag_id))
        return response

    def _get(self, module='mdm', path=None, version=None, params=None, header=None):
        """GET requests for the /MDM/Tags module."""
        response = self.client.get(module=module, path=path, version=version, params=params, header=header)
        return response

    def _post(self, module='mdm', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /MDM/Tags module."""
        response = self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
        return response

    def _delete(self, module='mdm', path=None, version=None, params=None, header=None):
        """DELETE reqeuests for the /MDM/Tags module."""
        response = self.client.delete(module=module, path=path, version=version, params=params, header=header)
        return response
