from flask import current_app
import unittest

class AppBasicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = current_app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_submit_scrapyjob(self):
        result = self.app.post(
            '/scrapyjob/', json={'url': 'https://www.reddit.com/r/Python/'})

        self.assertEqual(result.status_code, 200)

   