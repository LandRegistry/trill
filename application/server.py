from application import app
from flask import render_template
#, flash, redirect, request, session, make_response

#simple structure to hold harded coded test data
class Skill_group(object):
    def __init__(self, name, n):
        self.name = name
        self.n = n
        self.skill_list = []

    def Add_skill(self, skill_name, skill_desc):
        self.skill_list.append(skill_name +' - '+ skill_desc)

#hard coded test data for prototype
group_list = []

user_name = 'Alex Blewett'
trill_role = 'Developer'
job_title = 'Front end web developer'
line_manager = 'Marc McCoy'

data = Skill_group('Skill Group 1 - code', 1)
data.Add_skill('Develop code', 'produce bug free code')
data.Add_skill('Develop code', 'unit test code')
group_list.append(data)

data = Skill_group('Skill Group 2 - agile', 2)
data.Add_skill('Plan work', 'work in agile')
data.Add_skill('Plan work', 'attend stand up')
data.Add_skill('Plan work', 'attend planning meeting')
group_list.append(data)

data = Skill_group('Skill Group 3 - deliver', 3)
data.Add_skill('Present work', 'show team')
data.Add_skill('Present work', 'show product owner')
data.Add_skill('Present work', 'show n tell')
group_list.append(data)
#end of test data

#possible future functionality
@app.route('/home')
def welcome():
    return render_template('welcome.html')

@app.route('/view')
def view_skills():
    return render_template('view_skills.html', user_name = user_name, trill_role = trill_role, group_list = group_list, job_title = job_title, line_manager = line_manager)

@app.route('/edit')
def edit_skills():
    return render_template('edit_skills.html')

@app.route('/admin')
def admin_func():
    return render_template('admin_func.html')

#the prototype functionality is here
@app.route('/')
def test_skills():
    return render_template('view_skills_proto.html', user_name = user_name, trill_role = trill_role, group_list = group_list)
    return 'ok', 200


