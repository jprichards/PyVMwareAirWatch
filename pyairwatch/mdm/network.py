from .mdm import MDM


class Network(MDM):
    """
    Get network sample information
    version 1
    """
    def __init__(self, client):
        MDM.__init__(self, client)

    def get_network_by_device_id(self, device_id):
        """get network sample information based with Device ID"""
        return MDM._get(self, path='/devices/{}/network'.format(device_id))
