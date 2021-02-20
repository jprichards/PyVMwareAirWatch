from .mam import MAM


class InternalApps(MAM):
    """
    A class to manage Internal Applications
    """

    def __init__(self, client):
        MAM.__init__(self, client)
