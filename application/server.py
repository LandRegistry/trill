from application import app
from flask import render_template
#, flash, redirect, request, session, make_response

#simple structure to hold harded coded test data
class User(object):
    def __init__(self, name, line_manager, job_title, trill_role):
        self.name = name
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

#hard coded test data for prototype
user_name = 'Alex Blewett'
trill_role = 'Developer'
job_title = 'Front end web developer'
line_manager = 'Marc McCoy'
user = User(user_name, line_manager, job_title, trill_role)

skill_group_name = 'Skill Group 1 - code'
skill_group = Skill_group(skill_group_name, 1)

skill_title = Skill_title('Develop code')
skill_title.Add_skill('produce bug free code')
skill_title.Add_skill('unit test code')
skill_group.Add_skill_title(skill_title)

skill_title = Skill_title('Design code')
skill_title.Add_skill('Model objects')
skill_title.Add_skill('Review design')
skill_group.Add_skill_title(skill_title)

user.Add_skill_group(skill_group)

skill_group_name = 'Skill Group 2 - agile'
skill_group = Skill_group(skill_group_name, 2)

skill_title = Skill_title('Plan work')
skill_title.Add_skill('work in agile')
skill_title.Add_skill('attend stand up')
skill_title.Add_skill('attend planning meeting')
skill_group.Add_skill_title(skill_title)

skill_title = Skill_title('Do scrum')
skill_title.Add_skill('estimate story points')
skill_title.Add_skill('feedback during retrospective')
skill_title.Add_skill('do other srum stuff')
skill_group.Add_skill_title(skill_title)

user.Add_skill_group(skill_group)

skill_group_name = 'Skill Group 3 - deliver'
skill_group = Skill_group(skill_group_name, 3)

skill_title = Skill_title('Present work')
skill_title.Add_skill('show team')
skill_title.Add_skill('show product owner')
skill_title.Add_skill('show n tell')
skill_group.Add_skill_title(skill_title)

user.Add_skill_group(skill_group)
#end of test data

#possible future functionality
@app.route('/home')
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
    return render_template('admin_func.html')
#end of future functionality

#the prototype functionality is here
@app.route('/')
def test_skills():
    return render_template('view_skills_proto.html', user_obj = user)
    return 'ok', 200


