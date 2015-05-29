from application.models import *
from application import db
from werkzeug.security import generate_password_hash, check_password_hash
from operator import itemgetter

SKILL_TYPE_GDS = 1
SKILL_TYPE_SKILL = 2
SKILL_TYPE_KNOWLEDGE= 3

ONE_SKILL = 1
TWO_SKILLS = 2
THREE_SKILLS = 3

FIRST_POSITION = 1
SECOND_POSITION = 2
THIRD_POSITION = 3

DEFAULT_PROFICIENCY = 'None'

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

def ExtractSkillId(skill):

    #get skill_id from passed in composite code and skill
    raw_skill = skill.split(' - ')
    skill_id = int(raw_skill[0])

    return skill_id

def DecodeProf(number):
    if number == 1:
        level = 'None'
    elif number == 2:
        level = 'Basic'
    elif number == 3:
        level = 'Proficient'
    elif number == 4:
        level = 'Expert'

    return level

def GetUsersInASingleList(users_origin,users_x):

    users = users_origin

    #add users only in list x
    for user_x in users_x:
        user_not_found = True;
        for user in users:
            if user_x["id"] == user["id"]:
                user_not_found = False;
        if user_not_found:
            users.append(user_x)

    return users

def GetUsersWithCertainSkills(skill_id,number_of_skills,position):
    users = []

    for instance in db.session.query(User).order_by(User.surname).join(UserSkill,Skill).filter(Skill.id == skill_id):
        user ={}
        proficiency_value = GetUserSkillProficiencyLevel(instance.id,skill_id)
        proficiency = DecodeProf(proficiency_value)

        if proficiency_value > 1:

            if number_of_skills == ONE_SKILL:
                user.update({'id': instance.id, 'firstname': instance.firstname,'surname': instance.surname.lstrip(), 'proficiency_a': proficiency})
                users.append(user)

            elif number_of_skills == TWO_SKILLS:

                if position == FIRST_POSITION:
                    user.update({'id': instance.id, 'firstname': instance.firstname,'surname': instance.surname.lstrip(), 'proficiency_a': proficiency, 'proficiency_b': DEFAULT_PROFICIENCY})
                else:
                    user.update({'id': instance.id, 'firstname': instance.firstname,'surname': instance.surname.lstrip(), 'proficiency_a': DEFAULT_PROFICIENCY, 'proficiency_b': proficiency})

                users.append(user)

            elif number_of_skills == THREE_SKILLS:

                if position == FIRST_POSITION:
                    user.update({'id': instance.id, 'firstname': instance.firstname,'surname': instance.surname.lstrip(), 'proficiency_a': proficiency, 'proficiency_b': DEFAULT_PROFICIENCY, 'proficiency_c': DEFAULT_PROFICIENCY})
                elif position == SECOND_POSITION:
                    user.update({'id': instance.id, 'firstname': instance.firstname,'surname': instance.surname.lstrip(), 'proficiency_a': DEFAULT_PROFICIENCY, 'proficiency_b': proficiency, 'proficiency_c': DEFAULT_PROFICIENCY})
                else:
                    user.update({'id': instance.id, 'firstname': instance.firstname,'surname': instance.surname.lstrip(), 'proficiency_a': DEFAULT_PROFICIENCY, 'proficiency_b': DEFAULT_PROFICIENCY, 'proficiency_c': proficiency})

                users.append(user)

    return users

def GetusersWithOneSkill(skill):
    users = []

    skill_id = ExtractSkillId(skill)

    users = GetUsersWithCertainSkills(skill_id,ONE_SKILL,FIRST_POSITION)

    #sort result by surname
    users = sorted(users, key=itemgetter('surname'))

    return users

def GetusersWithTwoSkills(skill1, skill2):
    users_a = []
    users_b = []
    users = []

    skill1_id  = ExtractSkillId(skill1)
    skill2_id  = ExtractSkillId(skill2)

    #get list of users with skill 1
    users_a = GetUsersWithCertainSkills(skill1_id,TWO_SKILLS,FIRST_POSITION)

    #get list of users with skill 2
    users_b = GetUsersWithCertainSkills(skill2_id,TWO_SKILLS,SECOND_POSITION)


    #if list a contains users in list b update that user item
    for user_a in users_a:
        for user_b in users_b:
            if user_a["id"] == user_b["id"]:
                user_a.update({'proficiency_b': user_b["proficiency_b"]})
                users.append(user_a)

    users = GetUsersInASingleList(users, users_a)
    users = GetUsersInASingleList(users, users_b)

    #sort result by surname
    users = sorted(users, key=itemgetter('surname'))

    return users

def GetusersWithThreeSkills(skill1, skill2, skill3):
    users_a = []
    users_b = []
    users_c = []
    users = []


    skill1_id  = ExtractSkillId(skill1)
    skill2_id  = ExtractSkillId(skill2)
    skill3_id  = ExtractSkillId(skill3)

    #get list of users with skill 1
    users_a = GetUsersWithCertainSkills(skill1_id,THREE_SKILLS,FIRST_POSITION)

    #get list of users with skill 2
    users_b = GetUsersWithCertainSkills(skill2_id,THREE_SKILLS,SECOND_POSITION)

    #get list of users with skill 3
    users_c = GetUsersWithCertainSkills(skill3_id,THREE_SKILLS,THIRD_POSITION)

    #for users in both a & b lists
    for user_a in users_a:
        for user_b in users_b:
            if user_a["id"] == user_b["id"]:
                user = {}
                user.update({'id': user_a['id'], 'firstname': user_a['firstname'],'surname': user_a['surname'], 'proficiency_a': user_a["proficiency_a"],'proficiency_b': user_b["proficiency_b"],'proficiency_c': DEFAULT_PROFICIENCY})
                users.append(user)

    #add any a only users
    users = GetUsersInASingleList(users, users_a)

    #add any b only users
    users = GetUsersInASingleList(users, users_b)

    #for users in both a&b and c
    for user in users:
        for user_c in users_c:
            if user["id"] == user_c["id"]:
                user.update({'proficiency_c': user_c["proficiency_c"]})

    #add any c only users
    users = GetUsersInASingleList(users, users_c)

    #sort result by surname
    users = sorted(users, key=itemgetter('surname'))

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


    print(str(userId) + ' ' + str(skillId) + " " + str(level))

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
