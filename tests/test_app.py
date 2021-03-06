import unittest
import mock
from application import server
from application import database
from application.server import app
from application.models import *


from config import CONFIG_DICT

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        app.config.update(CONFIG_DICT)
        self.app = app.test_client()
        database.users_a = []
        database.users_b = []

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

    def get_users_lists(self, list_selection):

        users_list = []

        if list_selection == 1:
            users_list = [\
            {'id': 9, 'firstname': 'Ross','surname': 'Zeb', 'proficiency_a': 3, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
            {'id': 11, 'firstname': 'Jane','surname': 'Jones', 'proficiency_a': 2, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
            {'id': 12, 'firstname': 'James','surname': 'Doe', 'proficiency_a': 4, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
            {'id': 13, 'firstname': 'Anniken','surname': 'Will', 'proficiency_a': 3, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
            {'id': 15, 'firstname': 'Ness','surname': 'Hut', 'proficiency_a': 2, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
            {'id': 16, 'firstname': 'Em','surname': 'Alx', 'proficiency_a': 3, 'proficiency_b': 'None', 'proficiency_c': 'None'}\
            ]

        if list_selection == 2:
            users_list = [\
            {'id': 9, 'firstname': 'Ross','surname': 'Zeb', 'proficiency_a': 'None', 'proficiency_b': 4, 'proficiency_c': 'None'},\
            {'id': 12, 'firstname': 'James','surname': 'Doe', 'proficiency_a': 'None', 'proficiency_b': 3, 'proficiency_c': 'None'},\
            {'id': 13, 'firstname': 'Anniken','surname': 'Will', 'proficiency_a': 'None', 'proficiency_b': 4, 'proficiency_c': 'None'},\
            {'id': 16, 'firstname': 'Em','surname': 'Alx', 'proficiency_a': 'None', 'proficiency_b': 2, 'proficiency_c': 'None'},\
            {'id': 19, 'firstname': 'Jane','surname': 'Wlx', 'proficiency_a': 'None', 'proficiency_b': 4, 'proficiency_c': 'None'},\
            {'id': 22, 'firstname': 'Kate','surname': 'Alm', 'proficiency_a': 'None', 'proficiency_b': 2, 'proficiency_c': 'None'}\
            ]

        if list_selection == 3:
            users_list = [\
            {'id': 12, 'firstname': 'James','surname': 'Doe', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 4},\
            {'id': 13, 'firstname': 'Anniken','surname': 'Will', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 4},\
            {'id': 16, 'firstname': 'Em','surname': 'Alx', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 4},\
            {'id': 19, 'firstname': 'Jane','surname': 'Wlx', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 2},\
            {'id': 22, 'firstname': 'Kate','surname': 'Alm', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 3},\
            {'id': 11, 'firstname': 'Jane','surname': 'Jones', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 4},\
            {'id': 99, 'firstname': 'Ben','surname': 'Hut', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 3}\
            ]

        return users_list


    def do_nothing(self, *args):
        return ''

    def get_empty_list(self, *args):
        return[]

    def get_one_skill_list(self, *args):
        users = self.get_users_lists(1)
        return users

    def get_two_skills_list(self, *args):
        users2 = self.get_users_lists(2)
        return users2

    def get_three_skills_list(self, *args):
        users3 = self.get_users_lists(3)
        return users3

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


    @mock.patch('application.database.ExtractSkillId')
    @mock.patch('application.database.GetUsersWithCertainSkills')
    def test_GetusersWithOneSkill(self, mockgetuserswithcertainskills, mockextractskillid):
        mockextractskillid.side_effect = self.do_nothing
        mockgetuserswithcertainskills.side_effect = self.get_one_skill_list
        self.assertEqual(database.GetusersWithOneSkill("83 - VPR"),\
        [\
        {'id': 16, 'firstname': 'Em','surname': 'Alx', 'proficiency_a': 3, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
        {'id': 12, 'firstname': 'James','surname': 'Doe', 'proficiency_a': 4, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
        {'id': 15, 'firstname': 'Ness','surname': 'Hut', 'proficiency_a': 2, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
        {'id': 11, 'firstname': 'Jane','surname': 'Jones', 'proficiency_a': 2, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
        {'id': 13, 'firstname': 'Anniken','surname': 'Will', 'proficiency_a': 3, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
        {'id': 9, 'firstname': 'Ross','surname': 'Zeb', 'proficiency_a': 3, 'proficiency_b': 'None', 'proficiency_c': 'None'}\
        ])

    @mock.patch('application.database.ExtractSkillId')
    @mock.patch('application.database.GetUsersWithCertainSkills')
    def test_GetusersWithTwoSkills(self, mockgetuserswithcertainskills, mockextractskillid):
        mockextractskillid.side_effect = self.do_nothing
        mockgetuserswithcertainskills.side_effect = self.get_two_skills_list
        self.assertEqual(database.GetusersWithTwoSkills("83 - VPR","83 - VPR"),\
        [\
        {'id': 22, 'firstname': 'Kate','surname': 'Alm', 'proficiency_a': 'None', 'proficiency_b': 2, 'proficiency_c': 'None'},\
        {'id': 16, 'firstname': 'Em','surname': 'Alx', 'proficiency_a': 'None', 'proficiency_b': 2, 'proficiency_c': 'None'},\
        {'id': 12, 'firstname': 'James','surname': 'Doe', 'proficiency_a': 'None', 'proficiency_b': 3, 'proficiency_c': 'None'},\
        {'id': 13, 'firstname': 'Anniken','surname': 'Will', 'proficiency_a': 'None', 'proficiency_b': 4, 'proficiency_c': 'None'},\
        {'id': 19, 'firstname': 'Jane','surname': 'Wlx', 'proficiency_a': 'None', 'proficiency_b': 4, 'proficiency_c': 'None'},\
        {'id': 9, 'firstname': 'Ross','surname': 'Zeb', 'proficiency_a': 'None', 'proficiency_b': 4, 'proficiency_c': 'None'}\
        ])


    @mock.patch('application.database.ExtractSkillId')
    @mock.patch('application.database.GetUsersWithCertainSkills')
    def test_GetusersWithTwoSkills_2(self, mockgetuserswithcertainskills, mockextractskillid):
        database.users_a = self.get_users_lists(1)
        mockextractskillid.side_effect = self.do_nothing
        mockgetuserswithcertainskills.side_effect = self.do_nothing
        self.assertEqual(database.GetusersWithTwoSkills("83 - VPR","83 - VPR"),\
        [\
        {'id': 16, 'firstname': 'Em','surname': 'Alx', 'proficiency_a': 3, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
        {'id': 12, 'firstname': 'James','surname': 'Doe', 'proficiency_a': 4, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
        {'id': 15, 'firstname': 'Ness','surname': 'Hut', 'proficiency_a': 2, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
        {'id': 11, 'firstname': 'Jane','surname': 'Jones', 'proficiency_a': 2, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
        {'id': 13, 'firstname': 'Anniken','surname': 'Will', 'proficiency_a': 3, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
        {'id': 9, 'firstname': 'Ross','surname': 'Zeb', 'proficiency_a': 3, 'proficiency_b': 'None', 'proficiency_c': 'None'}\
        ])

    @mock.patch('application.database.ExtractSkillId')
    @mock.patch('application.database.GetUsersWithCertainSkills')
    def test_GetusersWithTwoSkills_3(self, mockgetuserswithcertainskills, mockextractskillid):
        database.users_a = self.get_users_lists(1)
        mockextractskillid.side_effect = self.do_nothing
        mockgetuserswithcertainskills.side_effect = self.get_two_skills_list
        self.assertEqual(database.GetusersWithTwoSkills("83 - VPR","83 - VPR"),\
        [\
        {'id': 22, 'firstname': 'Kate','surname': 'Alm', 'proficiency_a': 'None', 'proficiency_b': 2, 'proficiency_c': 'None'},\
        {'id': 16, 'firstname': 'Em','surname': 'Alx', 'proficiency_a': 3, 'proficiency_b': 2, 'proficiency_c': 'None'},\
        {'id': 12, 'firstname': 'James','surname': 'Doe', 'proficiency_a': 4, 'proficiency_b': 3, 'proficiency_c': 'None'},\
        {'id': 15, 'firstname': 'Ness','surname': 'Hut', 'proficiency_a': 2, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
        {'id': 11, 'firstname': 'Jane','surname': 'Jones', 'proficiency_a': 2, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
        {'id': 13, 'firstname': 'Anniken','surname': 'Will', 'proficiency_a': 3, 'proficiency_b': 4, 'proficiency_c': 'None'},\
        {'id': 19, 'firstname': 'Jane','surname': 'Wlx', 'proficiency_a': 'None', 'proficiency_b': 4, 'proficiency_c': 'None'},\
        {'id': 9, 'firstname': 'Ross','surname': 'Zeb', 'proficiency_a': 3, 'proficiency_b': 4, 'proficiency_c': 'None'}\
        ])



    @mock.patch('application.database.ExtractSkillId')
    @mock.patch('application.database.GetUsersWithCertainSkills')
    def test_GetusersWithThreeSkills(self, mockgetuserswithcertainskills, mockextractskillid):
        mockextractskillid.side_effect = self.do_nothing
        mockgetuserswithcertainskills.side_effect = self.get_three_skills_list
        self.assertEqual(database.GetusersWithThreeSkills("83 - VPR","83 - VPR","83 - VPR"),\
        [\
        {'id': 22, 'firstname': 'Kate','surname': 'Alm', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 3},\
        {'id': 16, 'firstname': 'Em','surname': 'Alx', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 4},\
        {'id': 12, 'firstname': 'James','surname': 'Doe', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 4},\
        {'id': 99, 'firstname': 'Ben','surname': 'Hut', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 3},\
        {'id': 11, 'firstname': 'Jane','surname': 'Jones', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 4},\
        {'id': 13, 'firstname': 'Anniken','surname': 'Will', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 4},\
        {'id': 19, 'firstname': 'Jane','surname': 'Wlx', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 2}\
        ])

    @mock.patch('application.database.ExtractSkillId')
    @mock.patch('application.database.GetUsersWithCertainSkills')
    def test_GetusersWithThreeSkills(self, mockgetuserswithcertainskills, mockextractskillid):
        database.users_a = self.get_users_lists(1)
        database.users_b = self.get_users_lists(2)
        mockextractskillid.side_effect = self.do_nothing
        mockgetuserswithcertainskills.side_effect = self.get_three_skills_list
        self.assertEqual(database.GetusersWithThreeSkills("83 - VPR","83 - VPR","83 - VPR"),\
        [\
        {'id': 22, 'firstname': 'Kate','surname': 'Alm', 'proficiency_a': 'None', 'proficiency_b': 2, 'proficiency_c': 3},\
        {'id': 16, 'firstname': 'Em','surname': 'Alx', 'proficiency_a': 3, 'proficiency_b': 2, 'proficiency_c': 4},\
        {'id': 12, 'firstname': 'James','surname': 'Doe', 'proficiency_a': 4, 'proficiency_b': 3, 'proficiency_c': 4},\
        {'id': 15, 'firstname': 'Ness','surname': 'Hut', 'proficiency_a': 2, 'proficiency_b': 'None', 'proficiency_c': 'None'},\
        {'id': 99, 'firstname': 'Ben','surname': 'Hut', 'proficiency_a': 'None', 'proficiency_b': 'None', 'proficiency_c': 3},\
        {'id': 11, 'firstname': 'Jane','surname': 'Jones', 'proficiency_a': 2, 'proficiency_b': 'None', 'proficiency_c': 4},\
        {'id': 13, 'firstname': 'Anniken','surname': 'Will', 'proficiency_a': 3, 'proficiency_b': 4, 'proficiency_c': 4},\
        {'id': 19, 'firstname': 'Jane','surname': 'Wlx', 'proficiency_a': 'None', 'proficiency_b': 4, 'proficiency_c': 2},\
        {'id': 9, 'firstname': 'Ross','surname': 'Zeb', 'proficiency_a': 3, 'proficiency_b': 4, 'proficiency_c': 'None'}\
        ])

    #test database models
    def test_User(self):
        user = User('firstname', 'surname', 'email', 'managerfirstname', 'managersurname', 'pwhash')
        self.assertEqual(user.firstname,'firstname')
        self.assertEqual(user.surname,'surname')
        self.assertEqual(user.email,'email')
        self.assertEqual(user.managerfirstname,'managerfirstname')
        self.assertEqual(user.managersurname,'managersurname')
        self.assertEqual(user.pwhash,'pwhash')

        test = repr(User('firstname', 'surname', 'email', 'managerfirstname', 'managersurname', 'pwhash'))
        self.assertEqual(test, "<User 'surname'>")

    def test_JobTitle(self):
        jobtitle = JobTitle('title')
        self.assertEqual(jobtitle.title,'title')

        test = repr(JobTitle('title'))
        self.assertEqual(test,"<Job_Title 'title'>")

    def test_TrillRoleGroup(self):
        trillrolegroup = TrillRoleGroup('groupname')
        self.assertEqual(trillrolegroup.groupname,'groupname')

        test = repr(TrillRoleGroup('groupname'))
        self.assertEqual(test,"<Trill_Role_Group 'groupname'>")

    def test_SkillGroup(self):
        skillgroup = SkillGroup('skillgroupname', 1)
        self.assertEqual(skillgroup.skillgroupname, 'skillgroupname')
        self.assertEqual(skillgroup.skilltype, 1)

        test = repr(SkillGroup('skillgroupname', 1))
        self.assertEqual(test,"<Skill_Group 'skillgroupname'>")

    def test_SkillTitle(self):
        skilltitle = SkillTitle('skilltitlename')
        self.assertEqual(skilltitle.skilltitlename, 'skilltitlename')

        test = repr(SkillTitle('skilltitlename'))
        self.assertEqual(test,"<Skill_Title 'skilltitlename'>")

    def test_Skill(self):
        skill = Skill('skillcode', 'skilldescription')
        self.assertEqual(skill.skillcode, 'skillcode')
        self.assertEqual(skill.skilldescription, 'skilldescription')

        test = repr(Skill('skillcode', 'skilldescription'))
        self.assertEqual(test,"<Skill 'skillcode'>")

    def test_UserJob(self):
        userjob = UserJob('20/12/1990', '20/12/1990')
        self.assertEqual(userjob.startdate, '20/12/1990')
        self.assertEqual(userjob.enddate, '20/12/1990')

        test = repr(UserJob('20/12/1990', '20/12/1990'))
        self.assertEqual(test,"<User_Job '20/12/1990'>")

    def test_UserSkill(self):
        userskill = UserSkill(2, 3, 4)
        self.assertEqual(userskill.age, 2)
        self.assertEqual(userskill.proficiency, 3)
        self.assertEqual(userskill.confidence, 4)

        test = repr(UserSkill(2, 3, 4))
        self.assertEqual(test,'<User_Skill 2>')
