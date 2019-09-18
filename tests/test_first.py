import pyairwatch.client
import unittest


class TestBasicTests(unittest.TestCase):
    def setUP(self):
        print("SETUP!")

    def teardown(self):
        print("TEAR DOWN!")

    def test_basic(self):
        self.assert_(True, "I RAN!")


if __name__ == '__main__':
    unittest.main()
