from application import app
from flask import render_template, redirect, url_for, session, request
from .forms import LoginForm, SigninForm
from flask.ext.login import LoginManager, login_user, logout_user 
from flask.ext.login import current_user, login_required
from application.database import *

#simple structure to hold harded coded pretend DB test data
class User(object):
    def __init__(self, user_name, password, name, line_manager, job_title, trill_role, active):
        self.user_name = user_name
        self.password = password
        self.name = name
        self.line_manager = line_manager
        self.job_title = job_title
        self.trill_role = trill_role
        self.active = active
        self.group_list = []
        
    def Add_skill_group(self, skill_group):
        self.group_list.append(skill_group)
        
    def Add_user_cred(self, user_name, password):
        self.user_name = user_name
        self.password = password
        
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.user_name
        
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


#possible future functionality
@app.route('/home')
def home():
    return render_template('welcome.html')

@app.route('/record')
@login_required
def record():
    #setup a pretend user as we are bypassing the login process for now
    #email = 'Maranda.Caron@landregistry.gsi.gov.uk'
    
    #get the user
    userId = GetUserId(session['username'])
    
    #populate the basic user data in the user object
    password = '123456'
    name    = GetUserName(userId)
    trill_role   = GetTrillRole(userId)
    job_title    = GetJobTitle(userId)
    line_manager = GetLineManager(userId)
    active = None

    user = User(userId, password, name, line_manager, job_title, trill_role, active)
    
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
@login_required
def about():
    return render_template('about.html')

'''@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm
    return render_template('login.html', signin_form = form)'''

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/signin'

@login_manager.user_loader
def user_loader(user_name):
    #get the user
    userId = GetUserId(user_name)
    
    #populate the basic user data in the user object
    password = '123456'
    name    = GetUserName(userId)
    trill_role   = GetTrillRole(userId)
    job_title    = GetJobTitle(userId)
    line_manager = GetLineManager(userId)
    active = True

    user = User(userId, password, name, line_manager, job_title, trill_role, active)
    return user

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method=='POST':
        if current_user is not None and current_user.is_authenticated():
            return redirect(url_for('index'))
        form = SigninForm(request.form)
        if form.validate():
            user_name = form.username.data
            password = form.password.data
            userId = GetUserId(user_name)

            #print (userId, user_name)
            if userId != '':
                #populate the basic user data in the user object
                name    = GetUserName(userId)
                trill_role   = GetTrillRole(userId)
                job_title    = GetJobTitle(userId)
                line_manager = GetLineManager(userId)
                active = True

                user = User(user_name, password, name, line_manager, job_title, trill_role, active)

                remember = form.remember_me.data
                
                login_user(user, remember)
                session['signed'] = True
                session['userId'] = userId
                session['username'] = user_name
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
                form.username.errors.append('Username not found')
                return render_template('signinpage.html',  signinpage_form = form)
            
        return render_template('signinpage.html',  signinpage_form = form)
    else:
        session['next'] = request.args.get('next')
        return render_template('signinpage.html', signinpage_form = SigninForm())
    
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/signout')
@login_required
def signout():
    session.pop('signed')
    session.pop('username')
    logout_user()
    return redirect(url_for('home'))
#end of future functionality

#the prototype functionality is here
@app.route('/')
def test_skills():
    #setup a pretend user as we are bypassing the login process for now
    email = 'Maranda.Caron@landregistry.gsi.gov.uk'
    
    #get the user
    userId = GetUserId(email)
    password = '12334556'
    
    #populate the basic user data in the user object
    user_name    = GetUserName(userId)
    trill_role   = GetTrillRole(userId)
    job_title    = GetJobTitle(userId)
    line_manager = GetLineManager(userId)
    active = None

    user = User(email, password, user_name, line_manager, job_title, trill_role, None)
    
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
    return render_template('view_skills_proto.html', user_obj = user)
    return 'ok', 200
