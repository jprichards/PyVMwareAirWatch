from .system import System


class FeatureFlag(System):
    """
    For Feature Flags
    """

    def __init__(self, client):
        super().__init__(client)

    def set_flag(self, feature_flag, og_uuid, override):
        """Set the Feature Flag"""
        path = '/featureFlag/{}/{}/{}'.format(feature_flag, og_uuid, override)
        return super._post(path=path)

    def get_status(self, feature_flag, og_uuid):
        """GET a specific Feature Flag status"""
        path = '/featureFlag/{}/{}'.format(feature_flag, og_uuid)
        return super._get(path=path)

    def og_status(self, og_uuid):
        """GET all Feature Flags for a particular OG need UUID"""
        return super._get(path='/featureFlag/{}'.format(og_uuid))
