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

def GetUserSkillGroups(id):

    skillGroups = []

    for instance in db.session.query(SkillGroup).join(TrillRoleGroup, JobTitle, UserJob, User).filter(User.id == id):
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

def GetUserPwHash(id):

    pwHash = ''
    for instance in db.session.query(User).filter(User.id == id):
         pwHash = instance.pwhash


    return pwHash

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
