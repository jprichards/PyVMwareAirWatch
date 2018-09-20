class LDAP(object):
    """
    A class to manage functionalities of LDAP Definition.
    """
    jheader = {'Content-Type': 'application/json'}

    def __init__(self, client):
        self.client = client

    def _post(self, module='mdm', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /MDM/Devices/EnterpriseIntegration/LDAP module."""
        return self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)

    def create_ldap(self, ldap_data):
        return self._post(path='/enterpriseintegration/ldap', json=ldap_data, header=self.jheader)
