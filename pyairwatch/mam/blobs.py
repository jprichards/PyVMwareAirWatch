from .mam import MAM


class Blobs(MAM):
    """
    A class to manage Blobs
    """

    def __init__(self, client):
        MAM.__init__(self, client)
