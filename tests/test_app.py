import unittest
import mock
from application import server
from application.server import app

from config import CONFIG_DICT

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        app.config.update(CONFIG_DICT)
        self.app = app.test_client()

    def test_landing_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)
