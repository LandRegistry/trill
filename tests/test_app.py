import unittest
import os
import mock
from application.server import app
from application import db, database

from config import CONFIG_DICT

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
#        app.config.from_object(os.environ.get('SETTINGS'))
        app.config.update(CONFIG_DICT)
        db.create_all()
        self.app = app
        self.app = app.test_client()


    def do_nothing(self, *args):
        return ''

    @mock.patch('application.database.GetUserId')
    @mock.patch('application.database.GetUserName')
    @mock.patch('application.database.GetTrillRole')
    @mock.patch('application.database.GetJobTitle')
    @mock.patch('application.database.GetLineManager')
    @mock.patch('application.database.GetUserSkillGroups')
    @mock.patch('application.database.GetSkillTitles')
    @mock.patch('application.database.GetSkills')
    def test_server_code(self, mockgetskills,mockgetskilltitles,mockgetuserskillgroups,mockgetlinemanager, mockgetjobtitle,mockgettrillrole, mockgetusername, mockgetuserid):

        mockgetskills.side_effect = self.do_nothing
        mockgetskilltitles.side_effect = self.do_nothing
        mockgetuserskillgroups.side_effect = self.do_nothing
        mockgetlinemanager.side_effect = self.do_nothing
        mockgetjobtitle.side_effect = self.do_nothing
        mockgettrillrole.side_effect = self.do_nothing
        mockgetusername.side_effect = self.do_nothing
        mockgetuserid.side_effect = self.do_nothing

        self.assertEqual((self.app.get('/')).status, '200 OK')


    def test_server_message(self):
        self.assertTrue('ok',(self.app.get('/')).data.decode("utf-8"))
