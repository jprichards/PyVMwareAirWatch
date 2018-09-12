class FeatureFlag(object):
    """
    For Feature Flags
    """

    def __init__(self, client):
        self.client = client

    def feature_flag_update(self, feature_flag, org_group_uuid, override_value):
        response = self._post(path='/featureFlag/{}/{}/{}'.format(feature_flag, org_group_uuid, override_value))
        return response

    def _get(self, module='system', path=None, version=None, params=None, header=None):
        """GET requests for the /System/featureFlag module."""
        response = self.client.get(module=module, path=path, version=version, params=params, header=header)
        return response

    def _post(self, module='system', path=None, version=None, params=None, data=None, json=None, header=None):
        """POST requests for the /System/featureFlag module."""
        response = self.client.post(module=module, path=path, version=version, params=params, data=data, json=json, header=header)
        return response
