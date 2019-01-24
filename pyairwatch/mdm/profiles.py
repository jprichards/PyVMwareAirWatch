from .mdm import MDM


class Profiles(MDM):
    """
    A class to manage V2 API's for AirWatch Profiles Management
    """

    def __init__(self, client):
        MDM.__init__(self, client)

    def search(self, **kwargs):
        """
        Returns the Profile information matching the search parameters.

        /api/mdm/profiles/search?{params}

        PARAMS:
            type={type}
            profilename={profilename}
            organizationgroupid={organizationgroupid}
            platform={platform}
            status={status}
            ownership={ownership}
        """
        return MDM._get(self, path='/profiles/search', params=kwargs)

    def install_profile(self, device_id, profile_id, payloads=None):
        """
        Queues up installation commands for interactive
        profiles for a device by overriding payload settings.
        """
        path = '/devices/{}/commands/installprofile'.format(device_id)
        query = 'profileid=' + str(profile_id)
        return MDM._post(self, path=path, params=query)

    def get_profile_by_id(self, profile_id):
        return MDM._get(self, path='/profiles/{}'.format(profile_id), version=2)
