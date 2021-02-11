from .mam import MAM


class Application(MAM):
    """
    A class to manage Internal Applications
    """

    def __init__(self, client):
        MAM.__init__(self, client)

    def get_app_assignment(self, application_uuid):
        path = '/apps/{}/assignment-rule'.format(application_uuid)
        return MAM._get(self, path=path)

    def create_app_assignment(self, application_uuid, assignment_data, action):
        path = '/apps/{}/assignment-rule'.format(application_uuid)
        return MAM._post(self, path=path, json=assignment_data)

    def update_app_assignment(self, application_uuid, assignment_data):
        path = '/apps/{}/assignment-rule'.format(application_uuid)
        return MAM._put(self, path=path, json=assignment_data)