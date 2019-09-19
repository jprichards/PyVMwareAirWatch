from .mdm import MDM


class Tags(MDM):
    """A class to manage various AirWatch device tag functionalities"""

    def __init__(self, client):
        MDM.__init__(self, client)

    def get_id_by_name(self, name, og_id):
        """mdm/tags/search?name={name}"""
        _params = {'name': str(name), 'organizationgroupid': str(og_id)}
        response = MDM._get(self, path='/tags/search', params=_params)
        return response
