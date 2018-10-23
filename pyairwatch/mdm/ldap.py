from .mdm import MDM


class LDAP(MDM):
    """
    A class to manage functionalities of LDAP Definition.
    """
    def __init__(self, client):
        MDM.__init__(self, client)
        self.jheader = {'Content-Type': 'application/json'}

    def create_ldap(self, ldap_data):
        path = '/enterpriseintegration/ldap'
        return MDM._post(self, path=path, json=ldap_data, header=self.jheader)
