from application import app
from flask import render_template,redirect
from application.database import *

#simple structure to hold user and skill data
class User(object):
    def __init__(self, userId, name, line_manager, job_title, trill_role):
        self.name = name
        self.userId = userId
        self.line_manager = line_manager
        self.job_title = job_title
        self.trill_role = trill_role
        self.group_list = []
        
    def Add_skill_group(self, skill_group):
        self.group_list.append(skill_group)
        
class Skill_group(object):
    def __init__(self, name, n):
        self.name = name
        self.n = n
        self.title_list = []
        
    def Add_skill_title(self, skill_title):
        self.title_list.append(skill_title)
        
class Skill_title(object):
    def __init__(self, name):
        self.name = name
        self.skill_list = []

    def Add_skill(self, skill_desc):
        self.skill_list.append(skill_desc)
#end of data structure


#possible future functionality
'''@app.route('/home')
def welcome():
    return render_template('welcome.html')

@app.route('/record')
def view_skills():
    return render_template('view_skills.html', user_obj = user)

@app.route('/edit')
def edit_skills():
    return render_template('edit_skills.html')

@app.route('/admin')
def admin_func():
    return render_template('admin_func.html')'''
#end of future functionality

#the prototype functionality is here
@app.route('/')
def test_skills():
    #setup a pretend user as we are bypassing the login process for now
    email = 'Maranda.Caron@landregistry.gsi.gov.uk'
    
    #get the user
    userId = GetUserId(email)
    
    #populate the basic user data in the user object
    user_name    = GetUserName(userId)
    trill_role   = GetTrillRole(userId)
    job_title    = GetJobTitle(userId)
    line_manager = GetLineManager(userId)

    user = User(userId, user_name, line_manager, job_title, trill_role)
    
    #Get Skill group based on user
    skillGroups  = GetUserSkillGroups(userId)
    n = 0

    #loop through the skill groups to get the skill titles and add to user skill groups
    for skillGroup in skillGroups:
        n += 1
        skill_group = Skill_group(skillGroup, n)
        skillTitles = GetSkillTitles(skillGroup)

        #loop through the skill titles to get the skill descriptions and add to skill title
        for skillTitle in skillTitles:
            skill_title = Skill_title(skillTitle)
            skills = GetSkills(skillTitle)
            
            #add the skill data, title, and groups
            for skill in skills:
                skill_title.Add_skill(skill)

            skill_group.Add_skill_title(skill_title)
        user.Add_skill_group(skill_group)
        
    #send the user object to the template
    return render_template('view_skills_proto.html', user_obj = user)
    return 'ok', 200
