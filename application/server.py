from application import app
from flask import render_template, redirect, url_for, session, request
from .forms import LoginForm, SigninForm
from flask.ext.login import LoginManager, login_user, logout_user
from flask.ext.login import current_user, login_required
from application.database import *
from application.login import valid_user

#simple structure to hold harded coded pretend DB test data
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
        self.group_list = []

    def Add_skill_group(self, skill_group):
        self.group_list.append(skill_group)

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
    def __init__(self, name, n):
        self.n = n
        self.name = name
#end of data structure


@app.route('/')
def index():
    return redirect(url_for('signin'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    #setup a pretend user as we are bypassing the login process for now
    #email = 'Maranda.Caron@landregistry.gsi.gov.uk'

    if request.method=='POST':
        if current_user is not None and current_user.is_authenticated():
            return redirect(url_for('home'))
        form = SigninForm(request.form)
        if form.validate():
            email = form.username.data
            password = form.password.data
            remember = form.remember_me.data

            userId = GetUserId(email)

            if valid_user(email, password):
                user = User(userId, email)
                login_user(user, remember)
                session['signed'] = True
                session['userId'] = userId
                session['username'] = email
                if session.get('next'):
                    next_page = session.get('next')
                    session.pop('next')
                    return redirect(next_page)
                else:
                    return redirect(url_for('home'))
                '''else:
                    form.password.errors.append('Password did not match')
                    return render_template('signinpage.html',  signinpage_form = form)'''
            else:
                form.username.errors.append('Username or password incorrect')
                return render_template('signinpage.html',  signinpage_form = form)

        return render_template('signinpage.html',  signinpage_form = form)
    else:
        session['next'] = request.args.get('next')
        return render_template('signinpage.html', signinpage_form = SigninForm())

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

@app.route('/signout')
@login_required
def signout():
    session.pop('signed')
    session.pop('userId')
    session.pop('username')
    logout_user()
    return redirect(url_for('home'))

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

@app.route('/home')
def home():
    return render_template('welcome.html')

@app.route('/record', methods=['GET', 'POST'])
@login_required
def record():

    #get the user
    email = (session['username'])
    userId = GetUserId(email)
    user = User(userId, email)

    #setup a pretend user as we are bypassing the login process for now
    #email = 'Maranda.Caron@landregistry.gsi.gov.uk'
    if request.method == "POST":
        #returns the radio button value as a | separated string
        choice = request.form
        string_0 = (choice['name1'])

        #decode the skill type - prof_radio = proficency, prof_conf = confidence
        end1 = string_0.find('|')
        skill_type = (string_0[0:end1])

        #decode the skill title
        string_1 = string_0[end1+1:]
        end2 = string_1.find('|')
        skill_title = string_1[0:end2]

        #decode the skill description
        string_2 = string_1[end2+1:]
        end3 = string_2.find('|')
        skill_desc = string_2[0:end3]

        #decode the skill value
        string_3 = string_2[end3+1:]
        skill_value = string_3


        if skill_type == 'prof_radio':

            SetUserSkillProficiency(userId,skill_value)

        elif skill_type == 'conf_radio':

            SetUserSkillConfidence(userId,skill_value)


        print (skill_type, skill_title, skill_desc, skill_value)



    #get the user
    email = (session['username'])
    userId = GetUserId(email)
    user = User(userId, email)

    #populate the basic user data in the user object
    #password = '123456'
    name    = GetUserName(userId)
    trill_role   = GetTrillRole(userId)
    job_title    = GetJobTitle(userId)
    line_manager = GetLineManager(userId)

    user.Add_user_data(name, line_manager, job_title, trill_role)

    #Get Skill group based on user
    skillGroups  = GetUserSkillGroups(userId)
    n = 0

    #loop through the skill groups to get the skill titles and add to user skill groups
    for skillGroup in skillGroups:
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
                skill_desc = Skill_desc(skill, s)
                skill_title.Add_skill(skill_desc)

            skill_group.Add_skill_title(skill_title)
        user.Add_skill_group(skill_group)

    #send the user object to the template
    return render_template('view_skills.html', user_obj = user)
    return 'ok', 200

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
    return render_template('add_course.html')

@app.route('/resource')
@login_required
def resource():
    return render_template('resource.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tour')
def tour():
    return render_template('tour.html')
