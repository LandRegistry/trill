import unittest
import mock
from application import server
from application.server import app

from config import CONFIG_DICT

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        app.config.update(CONFIG_DICT)
        self.app = app.test_client()

    def test_server_health(self):
        self.assertEqual((self.app.get('/health')).data.decode("utf-8"),"OK")
        
    def test_root(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue('/home' in response.location)

    def test_signin_page(self):
        response = self.app.get('/signin')
        self.assertEqual(response.status_code, 200)

    def test_skill_page(self):
        response = self.app.get('/record')
        self.assertEqual(response.status_code, 302)
        
    def test_resource_page(self):
        response = self.app.get('/resource')
        self.assertEqual(response.status_code, 302)
        
    def test_home_page(self):
        response = self.app.get('/home')
        self.assertEqual(response.status_code, 200)
