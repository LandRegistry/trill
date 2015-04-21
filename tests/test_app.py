import unittest
import os
from application.server import app

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        app.config.from_object(os.environ.get('SETTINGS'))
        self.app = app.test_client()

    def test_server_code(self):
        self.assertEqual((self.app.get('/')).status, '200 OK')


    def test_server_message(self):
        self.assertTrue('ok',(self.app.get('/')).data.decode("utf-8"))
