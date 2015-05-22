from application import app
from flask import render_template, redirect, url_for, session, request
from .forms import SigninForm, ReportForm
from flask.ext.login import LoginManager, login_user, logout_user
from flask.ext.login import current_user, login_required
from application.database import *
from application.login import valid_user

#structure to hold DB data
class User(object):
    def __init__(self, user_id, email):
        self.user_id = user_id
        self.email = email
        self.password = ''
        self.name = ''
        self.line_manager = ''
        self.job_title = ''
        self.trill_role = ''
        self.active = None
        self.gds_list = []
        self.is_list = []

    def Add_gds_skill_group(self, skill_group):
        self.gds_list.append(skill_group)

    def Add_is_skill_group(self, skill_group):
        self.is_list.append(skill_group)

    def Add_user_cred(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def Add_user_data(self, name, line_manager, job_title, trill_role):
        self.name = name
        self.line_manager = line_manager
        self.job_title = job_title
        self.trill_role = trill_role

    def Set_active(self, active):
        self.active = active

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id

class Skill_group(object):
    def __init__(self, name, n):
        self.name = name
        self.n = n
        self.title_list = []

    def Add_skill_title(self, skill_title):
        self.title_list.append(skill_title)

class Skill_title(object):
    def __init__(self, name, n):
        self.name = name
        self.n = n
        self.skill_list = []

    def Add_skill(self, skill_desc):
        self.skill_list.append(skill_desc)

class Skill_desc(object):
    def __init__(self, code, name, n, skill_prof, skill_conf, skill_age):
        self.n = n
        self.name = name
        self.code = code
        self.prof = skill_prof
        self.conf = skill_conf
        self.age = skill_age

class Skill_report(object):
    def __init__(self):
        self.skills1 = []
        self.skills2 = []
        self.skills3 = []
        self.categs = GetSkillCategs()


#end of data structure
skill_report = Skill_report()
users = ''
categ_value1 = ''
categ_value2 = ''
categ_value3 = ''
skill_value1 = ''
skill_value2 = ''
skill_value3 = ''


@app.route('/')
def index():
    return redirect(url_for('signin'))
    #return render_template('testpanel.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    #a pretend user for testing
    #email = 'Maranda.Caron@land.gsi.gov.uk'
    #password = 'Rabbit'

    if request.method=='POST':
        if current_user and current_user.is_authenticated():
            return redirect(url_for('record'))
        form = SigninForm(request.form)
        if form.validate():
            email = form.username.data
            password = form.password.data
            #remember = form.remember_me.data
            userId = GetUserId(email)
            error = None
            if valid_user(email, password):
                user = User(userId, email)
                name = GetUserName(userId)
                login_user(user)
                session['signed'] = True
                session['userId'] = userId
                session['username'] = email
                session['name'] = name
                if session.get('next'):
                    next_page = session.get('next')
                    session.pop('next')
                    return redirect(next_page)
                else:
                    return redirect(url_for('record'))
            else:
                #form.password.errors.append('Username or password is incorrect')
                error = 'Username or password is incorrect'
                return render_template('signinpage.html',  signinpage_form = form, error=error)

        return render_template('signinpage.html',  signinpage_form = form)
    else:
        session['next'] = request.args.get('next')
        if current_user and current_user.is_authenticated():
            return redirect(url_for('record'))
        return render_template('signinpage.html', signinpage_form = SigninForm())

@app.route('/user')
@login_required
def user():
    return render_template('user.html')

@app.route('/signout')
@login_required
def signout():
    session.pop('signed')
    session.pop('userId')
    session.pop('username')
    logout_user()
    return redirect(url_for('signin'))

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/signin'

@login_manager.user_loader
def user_loader(userId):
    #get the user
    email = GetEmail(userId)
    user = User(userId, email)

    user.Set_active(True)
    return user

'''@app.route('/home')
def home():
    return render_template('welcome.html')'''

@app.route('/record', methods=['GET', 'POST'])
@login_required
def record():
    #get the user
    email = (session['username'])
    userId = GetUserId(email)

    if request.method == "POST":

        #returns the radio button value as a | separated string
        choice = request.form
        string_0 = (choice['name1'])

        #decode the skill type - prof_radio = proficency, conf_radio = confidence, age_radio = age
        end1 = string_0.find('|')
        skill_type = (string_0[0:end1])

        #decode the skill title
        string_1 = string_0[end1+1:]
        end2 = string_1.find('|')
        skill_title = string_1[0:end2]

        #decode the skill code
        string_2 = string_1[end2+1:]
        end3 = string_2.find('|')
        skill_code = string_2[0:end3]

        #decode the skill description
        string_3 = string_2[end3+1:]
        #end4 = string_3.find('|')
        skill_value = string_3

        #decode the skill value
        #string_4 = string_3[end4+1:]
        #skill_value = string_4

        skill_id = GetSkillId(skill_code)

        #save the skill values
        if skill_type == 'prof_radio':
            res = SetUserSkillProficiency(userId, skill_id, skill_value)
            #print (userId, skill_id, skill_value)
        elif skill_type == 'conf_radio':
            res = SetUserSkillConfidence(userId, skill_id, skill_value)
            #print (userId, skill_id, skill_value)
        elif skill_type == 'age_radio':
            res = SetUserSkillAge(userId, skill_id, skill_value)
            #print (userId, skill_id, skill_value)
        return 'OK'

    if request.method == "GET":

        user = User(userId, email)

        #setup a pretend user as we are bypassing the login process for now
        #email = 'Maranda.Caron@landregistry.gsi.gov.uk'

        #populate the basic user data in the user object
        name    = GetUserName(userId)
        trill_role   = GetTrillRole(userId)
        job_title    = GetJobTitle(userId)
        line_manager = GetLineManager(userId)

        user.Add_user_data(name, line_manager, job_title, trill_role)

        #Get Skill group based on user
        GDSskillGroups  = GetUserSkillGroups(userId, 1)
        n = 0

        #loop through the skill groups to get the skill titles and add to user skill groups
        for skillGroup in GDSskillGroups:
            n += 1
            skill_group = Skill_group(skillGroup, n)
            skillTitles = GetSkillTitles(skillGroup)
            t = 0
            #loop through the skill titles to get the skill descriptions and add to skill title
            for skillTitle in skillTitles:
                t += 1
                skill_title = Skill_title(skillTitle, t)
                skills = GetSkills(skillTitle)
                s = 0
                #add the skill data, title, and groups
                for skill in skills:
                    s += 1
                    skill_prof = GetUserSkillProficiencyLevel(userId, skill.id)
                    skill_conf = GetUserSkillConfidenceLevel(userId, skill.id)
                    skill_desc = Skill_desc(skill.skillcode, skill.skilldescription, s, skill_prof, skill_conf, 0)
                    skill_title.Add_skill(skill_desc)

                skill_group.Add_skill_title(skill_title)
            user.Add_gds_skill_group(skill_group)

        #Get Skill group based on user
        ISskillGroups  = GetUserSkillGroups(userId, 2)
        n = 0

        #loop through the skill groups to get the skill titles and add to user skill groups
        for skillGroup in ISskillGroups:
            n += 1
            skill_group = Skill_group(skillGroup, n)
            skillTitles = GetSkillTitles(skillGroup)
            t = 0
            #loop through the skill titles to get the skill descriptions and add to skill title
            for skillTitle in skillTitles:
                t += 1
                skill_title = Skill_title(skillTitle, t)
                skills = GetSkills(skillTitle)
                s = 0
                #add the skill data, title, and groups
                for skill in skills:
                    s += 1
                    skill_prof = GetUserSkillProficiencyLevel(userId, skill.id)
                    skill_age = GetUserSkillAgeLevel(userId, skill.id)
                    skill_desc = Skill_desc(skill.skillcode, skill.skilldescription, s, skill_prof, 0, skill_age)
                    skill_title.Add_skill(skill_desc)

                skill_group.Add_skill_title(skill_title)
            user.Add_is_skill_group(skill_group)

        #send the user object to the template
        return render_template('view_skills.html', user_obj = user)


@app.route('/resource')
@login_required
def resource():
    #declare some global variables
    global skill_report
    global skill1
    global skill2
    global users
    global categ_value1
    global categ_value2
    global categ_value3
    global skill_value1
    global skill_value2
    global skill_value3

    #clear categ and skill values if new state
    if 'state' in request.args:
        categ_value1 = ''
        categ_value2 = ''
        categ_value3 = ''
        skill_value1 = ''
        skill_value2 = ''
        skill_value3 = ''


    #process if category box 1 in hit
    if 'categ1' in request.args:
        #get the value selected
        categ_value1 = request.args['categ1']
        #check the value selected is in the category list
        if categ_value1 in skill_report.categs:
            #populate the first skills list with skills for that category from the database
            skill_report.skills1 = GetSkillforCategory(categ_value1)
            #assumption made that if the first category box is hit, a new search is happening
            #so clear out other data
            skill_report.skills2.clear()
            skill_report.skills3.clear()
            skill1 = ''
            skill2 = ''
            skill3 = ''
            users = ''
            skill_value1 =''
            skill_value2 =''
            skill_value3 =''

    #process the next category box, so on...
    elif 'categ2' in request.args:
        categ_value2 = request.args['categ2']
        if categ_value2 in skill_report.categs:
            skill_report.skills2 = GetSkillforCategory(categ_value2)
            skill_report.skills3.clear()
            skill2 = ''
            skill3 = ''
            skill_report.skills3.clear()
            skill_value2 =''
            skill_value3 =''

    elif 'categ3' in request.args:
        categ_value3 = request.args['categ3']
        if categ_value3 in skill_report.categs:
            skill_report.skills3 = GetSkillforCategory(categ_value3)

    #process the first skills box hit
    elif 'skill1' in request.args:
        #get the value selected
        skill_value1 = request.args['skill1']
        print(skill_value1)

        #check the value selected is in the skills list
        if skill_value1 in skill_report.skills1:

            #populate the user list with user who have this skill from the database
            users = GetusersWithOneSkill(skill_value1)

            #remember this choice so it can be used in the next search
            skill1 = skill_value1
            skill_value2 = ''
            skill_value3 = ''


    #process the next skill box...
    elif 'skill2' in request.args:
        skill_value2 = request.args['skill2']
        if skill_value2 in skill_report.skills2:
            users = GetusersWithTwoSkills(skill1, skill_value2)
            skill2 = skill_value2
            skill_value3 = ''

    elif 'skill3' in request.args:
        skill_value3 = request.args['skill3']
        if skill_value3 in skill_report.skills3:
            users = GetusersWithThreeSkills(skill1, skill2, skill_value3)
    else:
        #nothing has been selected, clear the data
        skill_report.skills1.clear()
        skill_report.skills2.clear()
        skill_report.skills3.clear()
        skill1 = ''
        skill2 = ''
        users = ''
        print ('refresh')

    #render the template
    return render_template('resource.html', skill_report = skill_report, categ_value1 = categ_value1, skill_value1 = skill_value1, categ_value2 = categ_value2, skill_value2 = skill_value2, categ_value3 = categ_value3, skill_value3 = skill_value3, users = users)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

'''@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

@app.route('/export')
@login_required
def export_skills():
    return render_template('export_skills.html')

@app.route('/add_skill')
@login_required
def add_skill():
    return render_template('add_skill.html')

@app.route('/book')
@login_required
def book():
    return render_template('book.html')

@app.route('/bookings')
@login_required
def bookings():
    return render_template('bookings.html')

@app.route('/add_course')
@login_required
def add_course():
    return render_template('add_course.html')'''

'''@app.route('/tour')
def tour():
    return render_template('tour.html')'''

@app.route('/health')
def health():
    return 'OK'
