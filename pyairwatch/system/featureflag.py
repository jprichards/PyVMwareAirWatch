class FeatureFlag(object):
    """
    For Feature Flags
    """

    def __init__(self, client):
        self.client = client

    def set_flag(self, feature_flag, og_uuid, override):
        """Set the Feature Flag"""
        return self._post(path='/featureFlag/{}/{}/{}'.format(feature_flag, og_uuid, override))

    def get_status(self, feature_flag, og_uuid):
        """GET a specific Feature Flag status"""
        return self._get(path='/featureFlag/{}/{}'.format(feature_flag, og_uuid))

    def og_status(self, og_uuid):
        """GET all Feature Flags for a particular OG need UUID"""
        return self._get(path='/featureFlag/{}'.format(og_uuid))

    def _get(self, module='system', path=None, version=None, params=None, header=None):
        """GET requests for the /System/featureFlag module."""
        return self.client.get(module=module, path=path, version=version, params=params, header=header)

    def _post(self, module='system', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /System/featureFlag module."""
        return self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
