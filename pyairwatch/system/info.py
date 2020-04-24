from .system import System


class Info(System):
    """
    Get environment information
    """
    def __init__(self, client):
        System.__init__(self, client)

    def get_environment_info(self):
        """get environment information"""
        return System._get(self, path='/info')
