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

    for instance in db.session.query(User).filter(User.email == email):
        id = instance.id

    return id

def GetUserName(id):

    for instance in db.session.query(User).filter(User.id == id):
        userName = instance.firstname + " " + instance.surname

    return userName

def GetTrillRole(id):

    for instance in db.session.query(TrillRoleGroup).join(JobTitle, UserJob, User).filter(User.id == id):
        trillRole = instance.groupname

    return trillRole

def GetJobTitle(id):

    for instance in db.session.query(JobTitle).join(UserJob, User).filter(User.id == id):
        jobTitle = instance.title

    return jobTitle

def GetLineManager(id):

    for instance in db.session.query(User).filter(User.id == id):
        lineManager = instance.managerfirstname + ' ' + instance.managersurname

    return lineManager

def GetUserSkillGroups(id):

    skillGroups = []

    for instance in db.session.query(SkillGroup).join(TrillRoleGroup, JobTitle, UserJob, User).filter(User.id == id):
        skillGroups.append(instance.skillgroupname)

    return skillGroups

def GetSkills(skillgroupname):

    skillTitles = []

    for instance in db.session.query(SkillTitle).join(SkillGroup).filter(SkillGroup.skillgroupname == skillgroupname):
        skillTitles.append(instance.skilltitlename)

    skills = []

    for skillTitle in skillTitles:

        for instance in db.session.query(Skill).join(SkillTitle).filter(SkillTitle.skilltitlename == skillTitle):
            skills.append({'SkillTitle':skillTitle,'SkillDescription':instance.skilldescription})

    return skills
