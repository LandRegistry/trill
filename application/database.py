from application.models import *
from application import db

def GetAllSkillNames():

    skills = []

    for instance in db.session.query(Skill).order_by(Skill.id):
        #skills = skills + instance.skillname + str(instance.skill_group_id) + '\n'
        skills.append(instance.skillname)

    return skills

def GetUserSkills():


    '''q = db.session.query(User).join(TrillRoleGroup).filter(TrillRoleGroup.groupname == 'ServiceDesk').\
                    all()'''


    '''
    q = db.session.query(JobTitle).join(TrillRoleGroup).\
                    filter(TrillRoleGroup.groupname == 'ServiceDesk').\
                    all() '''

    '''
    q = db.session.query(UserJob).filter(UserJob.job_title_id == JobTitle.id).\
                    filter(JobTitle.id == TrillRoleGroup.id).\
                    filter(TrillRoleGroup.groupname == 'ServiceDesk').\
                    all()
                    '''

    q = db.session.query(User).join(UserSKill).\
                    filter(UserSKill.user_id == '1').\
                    all()

    return q
