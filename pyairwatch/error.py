class AirWatchAPIError(Exception):
    def __init__(self, json_response=None):
        if json_response is None:
            pass
        else:
            self.response = json_response
            self.error_code = json_response.get('errorCode')
            self.error_msg = str(json_response.get('message'))
            if self.error_code is None:
                self.error_code = 0
                self.error_msg = 'Unknown API error occurred'

    def __str__(self):
        return 'Error #{}: {}'.format(self.error_code, self.error_msg)
