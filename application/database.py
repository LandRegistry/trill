from application.models import *
from application import db

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
    print (skillTitle)
    for instance in db.session.query(Skill).join(SkillTitle).filter(SkillTitle.skilltitlename == skillTitle):
        skills.append(instance.skilldescription)

    return skills
