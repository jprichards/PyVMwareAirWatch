from .mdm import MDM


class Devices(MDM):
    """
    A class to manage functionalities of Mobile Device Management (MDM).
    """

    def __init__(self, client):
        MDM.__init__(self, client)

    def search(self, **kwargs):
        """Returns the Device information matching the search parameters."""
        return MDM._get(self, path='/devices', params=kwargs)

    def get_details_by_alt_id(self, serialnumber=None, macaddress=None, udid=None, imeinumber=None, easid=None):
        """Returns the Device information matching the search parameters."""
        params = {}
        if serialnumber:
            response = self.search(searchby='Serialnumber', id=str(serialnumber))
        elif macaddress:
            response = self.search(searchby='Macaddress', id=str(macaddress))
        elif udid:
            response = self.search(searchby='Udid', id=str(udid))
        elif imeinumber:
            response = self.search(searchby='ImeiNumber', id=str(imeinumber))
        elif easid:
            response = self.search(searchby='EasId', id=str(easid))
        else:
            return None
        return response

    def get_id_by_alt_id(self, serialnumber=None, macaddress=None, udid=None, imeinumber=None, easid=None):
        if serialnumber:
            response = self.search(searchby='Serialnumber', id=str(serialnumber))
        elif macaddress:
            response = self.search(searchby='Macaddress', id=str(macaddress))
        elif udid:
            response = self.search(searchby='Udid', id=str(udid))
        elif imeinumber:
            response = self.search(searchby='ImeiNumber', id=str(imeinumber))
        elif easid:
            response = self.search(searchby='EasId', id=str(easid))
        else:
            return None
        return response['Id']['Value']

    def clear_device_passcode(self, device_id):
        """
        Clear the passcode on a device
        """
        return MDM._post(self, path='/devices/{}/clearpasscode'.format(device_id))

    def send_commands_for_device_id(self, command, device_id):
        """
        Commands for devices selecting device based on id
        """
        path = '/devices/{}/commands'.format(device_id)
        command = 'command={}'.format(command)
        return MDM._post(self, path=path, params=command)

    def send_commands_by_id(self, command, searchby, id):
        """
        Commands for devices selecting device based on id
        """
        path = '/devices/commands'
        query = 'command={}&searchBy={}&id={}'.format(str(command),
                                                      str(searchby),
                                                      str(id))
        return MDM._post(self, path=path, params=query)

    def get_details_by_device_id(self, device_id):
        """
        device detals by device id
        """
        return MDM._get(self, path='/devices/{}'.format(device_id))

    def get_device_filevualt_recovery_key(self, device_uuid):
        """
        Gets a maccOS device's FileVualt Recovery Key
        """
        _path = '/devices/{}/security/recovery-key'.format(device_uuid)
        return MDM._get(self, path=_path)

    def get_security_info_by_id(self, device_id):
        """
        Processes the device ID to retrieve the security
        information sample related info
        """
        _path = '/devices/{}/security'.format(device_id)
        return MDM._get(self, path=_path)

    def get_security_info_by_atlternat_id(self, searchby, id):
        """
        Processes the device ID to retrieve the security
        information sample related info by Alternater ID
        """
        _path = '/devices/security'
        _params = 'searchby={}&id={}'.format(searchby, id)
        return MDM._get(self, path=_path, params=_params)

    def get_bulk_security_info(self, organization_group_id, user_name, params=None):
        """
        Processes the information like organizationgroup ID, user name, model,
        platform, last seen, ownership, compliant status, seen since parameters
        and fetches the security information for the same.
        """
        _path = '/devices/securityinfosearch'
        _query = 'organizationgroupid={}&user={}'.format(organization_group_id,
                                                         user_name)
        return MDM._get(self, path=_path, params=_query)
