from .mdm import MDM


class Devices(MDM):
    """
    A class to manage functionalities of Mobile Device Management (MDM).
    """

    def __init__(self, client):
        MDM.__init__(self, client)

    def search(self, **kwargs):
        """Returns the Device information matching the search parameters."""
        return MDM._get(path='/devices', params=kwargs)

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

    def commands_for_device_id(self, command, device_id):
        """
        Commands for devices selecting device based on id
        """
        path = '/devices/{}/commands'.format(device_id)
        command = 'command=' + command
        return MDM._post(self, path=path, params=command)

    def send_commands_by_id(self, command, searchby, id):
        """
        Commands for devices selecting device based on id
        """
        path = '/devices/commands'
        query = 'command=' + str(command) + '&searchBy=' + str(searchby)
        query = query + '&id=' + str(id)
        return MDM._post(self, path=path, params=query)

    def get_details_by_device_id(self, device_id):
        """
        device detals by device id
        """
        return MDM._get(self, path='/devices/{}'.format(device_id))
