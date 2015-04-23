import unittest
import os
import mock
from application.server import app
from application import db, database

class TestSequenceFunctions(unittest.TestCase):

    @mock.patch('application.database.GetUserId')
    def setUp(self,mockgetuserid):
        mockgetuserid.side_effect = return_id
        app.config.from_object(os.environ.get('SETTINGS'))
        #app.config["TESTING"] = True
        db.create_all()
        self.app = app
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_server_code(self):
        self.assertEqual((self.app.get('/')).status, '200 OK')


    def test_server_message(self):
        self.assertTrue('ok',(self.app.get('/')).data.decode("utf-8"))



    def return_id(self, *args):
        return 1
