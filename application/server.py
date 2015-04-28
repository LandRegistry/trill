from application import app
from flask import render_template, redirect, url_for, session, request
from .forms import LoginForm, SigninForm
from flask.ext.login import LoginManager, login_user, logout_user 
from flask.ext.login import current_user, login_required

#simple structure to hold harded coded pretend DB test data
class User(object):
    def __init__(self, user_name, password, first_name, last_name, line_manager, job_title, trill_role, active):
        self.id = id
        self.user_name = user_name
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
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
        return self.active
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)
        
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

'''<<<<<<< HEAD
#hard coded test data for prototype (a pretend database)
first_name = 'Alex'
last_name = 'Blewett'
user_name = 'alex@home'
password = '123456'
trill_role = 'Developer'
job_title = 'Front end web developer'
line_manager = 'Marc McCoy'
active = None
user = User(user_name, password, first_name, last_name, line_manager, job_title, trill_role, active)
#user.Add_user_cred(user_name, password)

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

user.Add_skill_group(skill_group)'''
#end of test data

#possible future functionality
@app.route('/home')
def home():
    return render_template('welcome.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/signout')
def signout():
    session.pop('signed')
    session.pop('username')
    logout_user()
    return redirect(url_for('home'))

@app.route('/record')
#@login_required
def record():
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

    return render_template('view_skills.html', user_obj = user)

@app.route('/edit')
@login_required
def edit_skills():
    return render_template('edit_skills.html')

@app.route('/admin')
@login_required
def admin_func():
    return render_template('admin_func.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm
    return render_template('login.html', signin_form = form)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/signin'
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method=='POST':
        if current_user is not None and current_user.is_authenticated():
            return redirect(url_for('index'))
        form = SigninForm(request.form)
        if form.validate():
            user_name = form.username.data
            userId = GetUserId(user_name)
            print (userId)
            if userId != '':
                name         = GetUserName(userId)
                trill_role   = GetTrillRole(userId)
                job_title    = GetJobTitle(userId)
                line_manager = GetLineManager(userId)
                active = None
                user = User(userId, name, line_manager, job_title, trill_role, active)

                login_user(userId, remember = form.remember_me.data)
                session['signed'] = True
                session['username'] = userId
                if session.get('next'):                
                    next_page = session.get('next')
                    session.pop('next')
                    return redirect(next_page)  
                else:
                    return redirect(url_for('home'))
                '''else:
                    form.password.errors.append('Passwod did not match')
                    return render_template('signinpage.html',  signinpage_form = form)'''
            else:
                form.username.errors.append('Username not found')
                return render_template('signinpage.html',  signinpage_form = form)
            
        return render_template('signinpage.html',  signinpage_form = form)
    else:
        session['next'] = request.args.get('next')
        return render_template('signinpage.html', signinpage_form = SigninForm())
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
