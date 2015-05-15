from application.models import *
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

'''
def GetAllSkillNames():

    skills = []

    for instance in db.session.query(Skill).order_by(Skill.id):
        skills.append(instance.skillcode)

    return skills
'''
def GetUserId(email):

    id = ''
    for instance in db.session.query(User).filter(User.email == email):
        id = instance.id

    return id

def GetSkillId(code):

    id = ''
    for instance in db.session.query(Skill).filter(Skill.skillcode == code):
        id = instance.id

    return id

def GetEmail(id):

    email = ''
    for instance in db.session.query(User).filter(User.id == id):
        id = instance.email

    return email

def GetUserName(id):

    userName = ''

    for instance in db.session.query(User).filter(User.id == id):
        userName = instance.firstname + " " + instance.surname

    return userName

def GetTrillRole(id):

    trillRole = ''

    for instance in db.session.query(TrillRoleGroup).join(JobTitle, UserJob, User).filter(User.id == id):
        trillRole = instance.groupname

    return trillRole

def GetJobTitle(id):

    jobTitle = ''

    for instance in db.session.query(JobTitle).join(UserJob, User).filter(User.id == id):
        jobTitle = instance.title

    return jobTitle

def GetLineManager(id):

    lineManager = ''

    for instance in db.session.query(User).filter(User.id == id):
        lineManager = instance.managerfirstname + ' ' + instance.managersurname

    return lineManager

def GetUserSkillGroups(id, skilltype):

    skillGroups = []

    for instance in db.session.query(SkillGroup).join(TrillRoleSkillGroup,TrillRoleGroup, JobTitle, UserJob, User).filter(User.id == id, SkillGroup.skilltype == skilltype):
        skillGroups.append(instance.skillgroupname)

    return skillGroups


def GetSkillTitles(skillgroupname):

    skillTitles = []

    for instance in db.session.query(SkillTitle).join(SkillGroup).filter(SkillGroup.skillgroupname == skillgroupname):
        skillTitles.append(instance.skilltitlename)

    return skillTitles

def GetSkills(skillTitle):

    skills = []

    for instance in db.session.query(Skill).join(SkillTitle).filter(SkillTitle.skilltitlename == skillTitle):
        #skills.append(instance.skillcode + ' ' + instance.skilldescription)
        skills.append(instance)

    return skills

def GetSkillCategs():
    skill_categs = []
    
    skill_categs.append('Skills')
    skill_categs.append('Knowledge')
    #skill_categs.append('GDS')
    
    return skill_categs

def GetSkillforCategory(category):
    skills = []
    if category == ('Skills'):
        skills.append('delphi')
        skills.append('python')
        skills.append('ruby')
    if category == ('Knowledge'):
        skills.append('mapping')
        skills.append('cora')
        skills.append('portal')  
    return skills

def GetusersWithOneSkill(skill):
    users = []
    if skill == 'delphi':
        users.append('tom')
        users.append('jerry')
    if skill == 'python':
        users.append('fred')
        users.append('barney')
    if skill == 'ruby':
        users.append('mickey')
        users.append('donald')
    
    if skill == 'mapping':
        users.append('anton')
        users.append('clark')
    if skill == 'cora':
        users.append('simone')
        users.append('dick')
    if skill == 'portal':
        users.append('ginny')
        users.append('sid')
    return users

def GetusersWithTwoSkills(skill1, skill2):
    users = []
    if skill1 == 'delphi' and skill2 == 'mapping':
        users.append('tom')
        users.append('anton')
    
    if skill1 == 'python' and skill2 == 'portal':
        users.append('anton')
    
    if skill1 == 'mapping' and skill2 == 'cora':        
        users.append('clark')
        users.append('simone')
        users.append('dick')

    return users

def GetusersWithThreeSkills(skill1, skill2, skill3):
    users = []
    if skill1 == 'delphi' and skill2 == 'mapping' and skill3 == 'ruby':
        users.append('tom')
    
    if skill1 == 'python' and skill2 == 'portal' and skill3 == 'cora':
        users.append('anton')

    return users

def GetUserPwHash(id):

    pwHash = ''
    for instance in db.session.query(User).filter(User.id == id):
         pwHash = instance.pwhash


    return pwHash

def GetUserSkillProficiencyLevel(userId,skillId):

    level = 1

    for instance in db.session.query(UserSkill).filter(UserSkill.user_id == userId, UserSkill.skill_id == skillId):
        level = instance.proficiency

    return int(level)

def GetUserSkillConfidenceLevel(userId,skillId):

    level = 1

    for instance in db.session.query(UserSkill).filter(UserSkill.user_id == userId, UserSkill.skill_id == skillId):
        level = instance.confidence

    return int(level)

def GetUserSkillAgeLevel(userId,skillId):

    level = 1

    for instance in db.session.query(UserSkill).filter(UserSkill.user_id == userId, UserSkill.skill_id == skillId):
        level = instance.age

    return int(level)


def SetUserSkillProficiency(userId,skillId,level):

    success = False

    try:
        for instance in db.session.query(UserSkill).filter(UserSkill.user_id == userId, UserSkill.skill_id == skillId):
            instance.proficiency = level

        db.session.commit()
        success = True

    except:

        success = False

    return success

def SetUserSkillConfidence(userId,skillId,level):

    success = False

    try:
        for instance in db.session.query(UserSkill).filter(UserSkill.user_id == userId, UserSkill.skill_id == skillId):
            instance.confidence = level

        db.session.commit()
        success = True

    except:

        success = False

    return success

def SetUserSkillAge(userId,skillId,level):

    success = False

    try:
        for instance in db.session.query(UserSkill).filter(UserSkill.user_id == userId, UserSkill.skill_id == skillId):
            instance.age = level

        db.session.commit()
        success = True

    except:

        success = False

    return success
