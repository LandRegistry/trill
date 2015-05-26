from application.models import *
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

SKILL_TYPE_GDS = 1
SKILL_TYPE_SKILL = 2
SKILL_TYPE_KNOWLEDGE= 3

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

        print(skillGroups)

    return skillGroups


def GetSkillTitles(skillgroupname):

    skillTitles = []

    for instance in db.session.query(SkillTitle).join(SkillGroup).filter(SkillGroup.skillgroupname == skillgroupname):
        skillTitles.append(instance.skilltitlename)

    return skillTitles

def GetSkills(skillTitle):

    skills = []

    for instance in db.session.query(Skill).join(SkillTitle).filter(SkillTitle.skilltitlename == skillTitle):
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
        for instance in db.session.query(Skill).order_by(Skill.skillcode).join(SkillTitle,SkillGroup).filter(SkillGroup.skilltype == SKILL_TYPE_SKILL):
            #skills.append(instance)
            skills.append(str(instance.id) + " - " + instance.skilldescription)

    if category == ('Knowledge'):
        for instance in db.session.query(Skill).order_by(Skill.skillcode).join(SkillTitle,SkillGroup).filter(SkillGroup.skilltype == SKILL_TYPE_KNOWLEDGE):
            #skills.append(instance)
            skills.append(str(instance.id) + " - " + instance.skilldescription)

    return skills

def GetusersWithOneSkill(skill):
    users = []

    #get skill_id from passed in composite code and skill
    raw_skill = skill.split(' - ')
    skill_id = raw_skill[0]

    for instance in db.session.query(User).order_by(User.surname).join(UserSkill,Skill).filter(Skill.id == skill_id):
        #users.append(instance)
        user ={}
        proficiency = GetUserSkillProficiencyLevel(instance.id,skill_id)

        if proficiency > 1:
            user.update({'firstname': instance.firstname,'surname': instance.surname, 'proficiency_a': (proficiency - 1)})
            users.append(user)

    return users

def GetusersWithTwoSkills(skill1, skill2):
    users = []


    #get skill_id from passed in composite code and skill
    raw_skill1 = skill1.split(' - ')
    skill1_id = raw_skill1[0]

    raw_skill2 = skill2.split(' - ')
    skill2_id = raw_skill2[0]

    for instance in db.session.query(User).order_by(User.surname).join(UserSkill,Skill).filter(Skill.id == skill1_id):
        #users.append(instance)
        user ={}
        proficiency_a = GetUserSkillProficiencyLevel(instance.id,skill1_id)

        for instance2 in db.session.query(User).order_by(User.surname).join(UserSkill,Skill).filter(Skill.id == skill2_id, User.id == instance.id):
            proficiency_b = GetUserSkillProficiencyLevel(instance2.id,skill2_id)

            if (proficiency_a > 1) or (proficiency_b > 1):
                user.update({'firstname': instance.firstname,'surname': instance.surname, 'proficiency_a': (proficiency_a -1), 'proficiency_b': (proficiency_b -1)})
                users.append(user)

    return users

def GetusersWithThreeSkills(skill1, skill2, skill3):
    users = []


    #get skill_id from passed in composite code and skill
    raw_skill1 = skill1.split(' - ')
    skill1_id = raw_skill1[0]

    raw_skill2 = skill2.split(' - ')
    skill2_id = raw_skill2[0]

    raw_skill3 = skill3.split(' - ')
    skill3_id = raw_skill3[0]

    for instance in db.session.query(User).order_by(User.surname).join(UserSkill,Skill).filter(Skill.id == skill1_id):
        proficiency_a = GetUserSkillProficiencyLevel(instance.id,skill1_id)


        for instance2 in db.session.query(User).order_by(User.surname).join(UserSkill,Skill).filter(Skill.id == skill2_id, User.id == instance.id):
            proficiency_b = GetUserSkillProficiencyLevel(instance2.id,skill2_id)

            for instance3 in db.session.query(User).order_by(User.surname).join(UserSkill,Skill).filter(Skill.id == skill3_id, User.id == instance2.id):
                proficiency_c = GetUserSkillProficiencyLevel(instance3.id,skill3_id)

                if (proficiency_a > 1) or (proficiency_b > 1) or (proficiency_c > 1):

                      user ={}
                      user.update({'firstname': instance.firstname,'surname': instance.surname, 'proficiency_a': (proficiency_a -1), 'proficiency_b': (proficiency_b -1), 'proficiency_c': (proficiency_c -1)})
                      users.append(user)

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
