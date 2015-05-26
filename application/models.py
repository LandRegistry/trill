from sqlalchemy import Column, Integer, String
from application import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    managerfirstname = db.Column(db.String(80))
    managersurname = db.Column(db.String(80))
    pwhash = db.Column(db.String(80))

    def __init__(self, firstname, surname, email, managerfirstname, managersurname, pwhash):
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.managerfirstname = managerfirstname
        self.managersurname = managersurname
        self.pwhash = pwhash

    def __repr__(self):
        return '<User %r>' % self.surname


class JobTitle(db.Model):
    __tablename__ = 'job_titles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    trill_role_group_id = db.Column(db.Integer, db.ForeignKey('trill_role_groups.id'))


    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Job_Title %r>' % self.title

class TrillRoleGroup(db.Model):
    __tablename__ = 'trill_role_groups'
    id = db.Column(db.Integer, primary_key=True)
    groupname = db.Column(db.String(80))

    def __init__(self, title):
        self.groupname = groupname

    def __repr__(self):
        return '<Trill_Role_Group %r>' % self.groupname

class SkillGroup(db.Model):
    __tablename__ = 'skill_groups'
    id = db.Column(db.Integer, primary_key=True)
    skillgroupname = db.Column(db.String(80), unique=True)
    skilltype = db.Column(db.Integer)

    def __init__(self, title):
        self.skillgroupname = skillgroupname
        self.skilltype = skilltype

    def __repr__(self):
        return '<Skill_Group %r>' % self.skillgroupname

class TrillRoleSkillGroup(db.Model):
    __tablename__ = 'trill_role_skill_groups'
    id = db.Column(db.Integer, primary_key=True)
    trill_role_group_id = db.Column(db.Integer, db.ForeignKey('trill_role_groups.id'))
    skill_group_id = db.Column(db.Integer, db.ForeignKey('skill_groups.id'))



class SkillTitle(db.Model):
    __tablename__ = 'skill_titles'
    id = db.Column(db.Integer, primary_key=True)
    skilltitlename = db.Column(db.String(80), unique=True)
    skill_group_id = db.Column(db.Integer, db.ForeignKey('skill_groups.id'))

    def __init__(self, title):
        self.skilltitlename = skilltitlename

    def __repr__(self):
        return '<Skill_Title %r>' % self.skilltitlename

class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    skillcode = db.Column(db.String(80), unique=True)
    skilldescription = db.Column(db.String)
    skill_title_id = db.Column(db.Integer, db.ForeignKey('skill_titles.id'))

    def __init__(self, title):
        self.skillcode = skillcode
        self.skilldescription = skilldescription

    def __repr__(self):
        return '<Skill %r>' % self.skillcode

class UserJob(db.Model):
    __tablename__ = 'user_jobs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    job_title_id = db.Column(db.Integer, db.ForeignKey('job_titles.id'))
    startdate = db.Column(db.Date)
    enddate = db.Column(db.Date)

    def __init__(self, title):
        self.startdate = startdate
        self.enddate = enddate

    def __repr__(self):
        return '<User_Job %r>' % self.startdate

class UserSkill(db.Model):
    __tablename__ = 'user_skills'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))
    proficiency = db.Column(db.Integer)
    confidence = db.Column(db.Integer)
    age = db.Column(db.Integer)



    def __init__(self, title):
        self.age = age

    def __repr__(self):
        return '<User_Skill %r>' % self.age
