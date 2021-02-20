from .system import System


class FeatureFlag(System):
    """
    For Feature Flags
    """

    def __init__(self, client):
        System.__init__(self, client)

    def set_feature_flag(self, feature_flag, og_uuid, override):
        """Set the Feature Flag"""
        _path = '/featureFlag/{}/{}/{}'.format(feature_flag, og_uuid, override)
        return System._post(self, path=_path)

    def get_feature_flag_status(self, feature_flag, og_uuid):
        """GET a specific Feature Flag status"""
        _path = '/featureFlag/{}/{}'.format(feature_flag, og_uuid)
        return System._get(self, path=_path)

    def list_feature_flags_by_og(self, og_uuid):
        """GET all Feature Flags for a particular OG need UUID"""
        return System._get(self, path='/featureFlag/{}'.format(og_uuid))
