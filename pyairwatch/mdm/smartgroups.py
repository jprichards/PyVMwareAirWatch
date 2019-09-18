from .mdm import MDM


class SmartGroups(object):
    """
    A class to manage AirWatch Smart Groups.
    """

    def __init__(self, client):
        MDM.__init__(self, client)

    def search(self, **kwargs):
        """
        Returns the Smart Groups details matching the search parameters

        /api/mdm/smartgroups/search?{params}

        PARAMS:
            name={name}
            organizationgroupid={organizationgroupid}
            managedbyorganizationgroupid={managedbyorganizationgroupid}
        """
        response = MDM._get(self, path='/smartgroups/search', params=kwargs)
        return response

    def get_details(self, id):
        """Retrieves the Smart Group details created in an Organization Group"""
        response = MDM._get(self, path='/smartgroups/{}'.format(id))
        return response

    def get_devices(self, id):
        """Retrieves all devices from Smart Group"""
        devices = MDM._get(self, path='/smartgroups/{}/devices'.format(id))
        return devices

    def get_id_from_og_id(self, og_id, sg_name):
        """Returns the Smart Group ID for a given SG Name & OG ID"""
        response = self.search(managedbyorganizationgroupid=str(og_id),
                               orderby='smartgroupid')
        for keys in response['SmartGroups']:
            if keys['Name'] == sg_name:
                sg_id = keys.get('SmartGroupID')
                return sg_id

    def move_device_to_sg(self, sg_id, device_id, device_name):
        """Move Device to a Smart Group by Device ID"""
        # sg_details = self.get_details(sg_id)
        # print type(sg_details)
        sg_details = {}
        sg_details[u'DeviceAdditions'] = [{u'Id': str(device_id).decode(),
                                           u'Name': str(device_name).decode()}]
        print(sg_details)
        # device = {'DeviceAdditions':[{ 'Id':'{}'.format(device_id)}]}
        path = '/smartgroups/{}/update'.format(str(sg_id))
        response = MDM._post(self, path=path, data=sg_details)

        d = self.get_details(sg_id)
        print(d)

        return response

    # Inconsistent behaviors during testing, commenting out these methods for now:
    #
    # def remove_device_from_sg(self, sg_id, device_id):
    #     """Remove Device from a Smart Group by Device ID"""
    #     device = {'DeviceExclusions':[{ 'Id':'{}'.format(device_id)}]}
    #     response = self._put(path='/smartgroups/{}'.format(str(sg_id)), data=device)
    #     return response
