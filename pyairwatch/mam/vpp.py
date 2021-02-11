from .mam import MAM


class VPP(MAM):
    """
    A class to manage Internal Applications
    """

    def __init__(self, client):
        MAM.__init__(self, client)

    def get_vpp_details(self, application_id):
        path = '/apps/purchased/{}'.format(application_id)
        header = {'Content-Type': 'application/json;version=2'}
        return MAM._get(self, path=path, header=header , version=2)

    def search(self, **kwargs):
        """
        Search for VPP application details, its assignments, and deployment parameters.
        :param kwargs:
        :return:
        """
        return MAM._get(self, path='/apps/purchased/search', params=kwargs)

    # def search_by_atl_id(self, search_by, value):
    #     return self.search(search_by, str(value))
