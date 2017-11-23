import unittest
import requests
from mock import Mock, patch
import app
from services import ise


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()


    def test_get_failure_reasons(self):
        # Send a request to the API server and store the response.
        response = ise.get_failure_reasons()
        # Confirm that the request-response cycle completed successfully.
        self.assertTrue(response.ok)

    def test_get_active_session_count(self):
        response = ise.get_active_count()
        self.assertTrue(response.ok)

    def test_get_active_session_list(self):
        # Send a request to the API server and store the response.
        response = ise.get_active_list()
        # Confirm that the request-response cycle completed successfully.
        self.assertTrue(response.ok)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
