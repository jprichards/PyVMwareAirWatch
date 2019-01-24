from .system import System


class Info(System):
    """
    Get enverioment information
    """
    def __init__(self, client):
        System.__init__(self, client)

    def get_enviroment_info(self):
        """get enviroment information"""
        return System._get(self, path='/info')
