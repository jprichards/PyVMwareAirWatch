from .mam import MAM


class Blobs(object):
    """
    A class to manage Blobs
    """

    def __init__(self, client):
        MAM.__init__(self, client)
