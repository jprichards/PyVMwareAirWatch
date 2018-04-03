class SmartGroups(object):
    """
    A class to manage AirWatch Smart Groups.
    """

    def __init__(self, client):
        self.client = client

    def search(self, **kwargs):
        """
        Returns the Smart Groups details matching the search parameters

        /api/mdm/smartgroups/search?{params}

        PARAMS:
            name={name}
            organizationgroupid={organizationgroupid}
            managedbyorganizationgroupid={managedbyorganizationgroupid}
        """
        response = self._get(path='/smartgroups/search', params=kwargs)
        return response

    def get_details(self, id):
        """Retrieves the Smart Group details created in an Organization Group"""
        response = self._get(path='/smartgroups/{}'.format(id))
        return response

    def get_id_from_og_id(self, og_id, sg_name):
        """Returns the Smart Group ID for a given SG Name & OG ID"""
        response = self.search(managedbyorganizationgroupid=str(og_id), orderby='smartgroupid')
        for keys in response['SmartGroups']:
            if keys['Name'] == sg_name:
                sg_id = keys.get('SmartGroupID')
                return sg_id

    #NOQA
    def move_device_to_sg(self, sg_id, device_id, device_name):
        """Move Device to a Smart Group by Device ID"""
        # sg_details = self.get_details(sg_id)
        # print type(sg_details)
        sg_details = {}
        sg_details[u'DeviceAdditions'] = [{u'Id': str(device_id).decode(), u'Name': str(device_name).decode()}]
        sg_details[u'CriteriaType'] = 'UserDevice'
        print sg_details
        # device = {'DeviceAdditions':[{ 'Id':'{}'.format(device_id)}]}
        response = self._put(path='/smartgroups/{}'.format(str(sg_id)), data=sg_details)

        d = self.get_details(sg_id)
        print d

        return response

    #NOQA
    def add_tag_to_sg(self, sg_id, tag_id, tag_name):
        sg_details = self.get_details(sg_id)
        # sg_details = {}
        sg_details['Tags'] = [{u'Id': str(tag_id).decode(), u'Name': str(tag_name).decode()}]
        sg_details['Devices'] = 1
        print sg_details

        response = self._post(path='/smartgroups/{}/update'.format(str(sg_id)), data=sg_details)
        print response

    def _get(self, module='mdm', path=None, version=None, params=None, header=None):
        """GET requests for the /MDM/SmartGroups module."""
        response = self.client.get(module=module, path=path, version=version, params=params, header=header)
        return response

    def _post(self, module='mdm', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /MDM/SmartGroups module."""
        response = self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
        return response

    def _put(self, module='mdm', path=None, version=None, params=None, data=None, json=None, header=None):
        """PUT requests for the /MDM/SmartGroups module."""
        response = self.client.put(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
        return response

    # Inconsistent behaviors during testing, commenting out these methods for now:
    #
    # def remove_device_from_sg(self, sg_id, device_id):
    #     """Remove Device from a Smart Group by Device ID"""
    #     device = {'DeviceExclusions':[{ 'Id':'{}'.format(device_id)}]}
    #     response = self._put(path='/smartgroups/{}'.format(str(sg_id)), data=device)
    #     return response
