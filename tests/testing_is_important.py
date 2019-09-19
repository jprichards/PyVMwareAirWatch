from pyairwatch.client import AirWatchAPI
import unittest
import json


class TestBasicTests(unittest.TestCase):
    def setUp(self):
        input = "cnaapp"
        with open("environments.json") as json_file:
            server_details = json.load(json_file)
        self.enviroment = AirWatchAPI(env=server_details[input]["server"],
                                      apikey=server_details[input]["apikey"],
                                      username=server_details[input]["username"],
                                      password=server_details[input]["password"])

    def teardown(self):
        print("TEAR DOWN!")

    def test_is_this_AirWatch(self):
        response = self.enviroment.info.get_enviroment_info()
        self.assertEqual(response["ProductName"], "AirWatch Platform Service",
                         "Info API ran")


if __name__ == '__main__':
    unittest.main()
