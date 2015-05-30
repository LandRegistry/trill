import unittest
import mock
from application import server
from application import database
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

    # database layer tests
    def get_id(self, *args):da 
        return 9
    def do_nothing(self, *args):
        return ''

    def get_users1_list(self, *args):
        users1 = [{'id': 10, 'surname': 'Jones'},{'id': 11, 'surname': 'Doe'}]
        return users1

    def test_GetUsersInASingleList(self):
        users_x = [{'id': 10},{'id': 11},{'id': 12}]
        users_origin = [{'id': 8},{'id': 9},{'id': 12}]
        self.assertEqual(database.GetUsersInASingleList(users_origin,users_x),\
        [{'id': 8}, {'id': 9}, {'id': 12}, {'id': 10}, {'id': 11}])

        users_x = [{'id': 8},{'id': 9},{'id': 12}]
        users_origin = [{'id': 8},{'id': 9},{'id': 12}]
        self.assertEqual(database.GetUsersInASingleList(users_origin,users_x),\
        [{'id': 8},{'id': 9},{'id': 12}])

        users_x = []
        users_origin = [{'id': 8},{'id': 9},{'id': 12}]
        self.assertEqual(database.GetUsersInASingleList(users_origin,users_x),\
        [{'id': 8},{'id': 9},{'id': 12}])

        users_x = []
        users_origin = []
        self.assertEqual(database.GetUsersInASingleList(users_origin,users_x),[])

        users_x = [{'id': 8},{'id': 9},{'id': 12}]
        users_origin = []
        self.assertEqual(database.GetUsersInASingleList(users_origin,users_x),\
        [{'id': 8},{'id': 9},{'id': 12}])


    def test_ExtractSkillId(self):
        self.assertEqual(database.ExtractSkillId("83 - VPR"),83)

    def test_DecodeProf(self):
        self.assertEqual(database.DecodeProf(1),"None")
        self.assertEqual(database.DecodeProf(2),"Basic")
        self.assertEqual(database.DecodeProf(3),"Proficient")
        self.assertEqual(database.DecodeProf(4),"Expert")

    @mock.patch('application.database.db.session.query')
    def test_GetUserID(self, mocksession):
        mocksession.side_effect = self.do_nothing
        self.assertEqual(database.GetUserId("some.ones@email.com"),'')

        mocksession.side_effect = self.get_id
        self.assertEqual(database.GetUserId("some.ones@email.com"),9)

    @mock.patch('application.database.ExtractSkillId')
    @mock.patch('application.database.GetUsersWithCertainSkills')
    def test_GetusersWithOneSkill(self, mockgetuserswithcertainskills, mockextractskillid):
        mockextractskillid.side_effect = self.do_nothing
        mockgetuserswithcertainskills.side_effect = self.get_users1_list
        self.assertEqual(database.GetusersWithOneSkill("83 - VPR"),[{'surname': 'Doe', 'id': 11},{'id': 10, 'surname': 'Jones'}])
