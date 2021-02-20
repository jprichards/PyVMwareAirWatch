from pyairwatch.client import AirWatchAPI
import unittest
import json

# convert to pytest

class TestBasicTests(unittest.TestCase):
    def setUp(self):
        input = "cnaapp"
        with open("environments.json") as json_file:
            server_details = json.load(json_file)
        self.environment = AirWatchAPI(env=server_details[input]["server"],
                                       apikey=server_details[input]["apikey"],
                                       username=server_details[input]["username"],
                                       password=server_details[input]["password"])

    def teardown(self):
        print("TEAR DOWN!")

    def test_is_this_AirWatch(self):
        response = self.environment.info.get_enviroment_info()
        self.assertEqual(response["ProductName"], "AirWatch Platform Service",
                         "Info API ran")
# todo: more tests


if __name__ == '__main__':
    unittest.main()
