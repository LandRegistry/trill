#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import sys
import os

APPLICATION_FILEPATH = os.getenv('TRILL_APPLICATION_FILEPATH','/home/vagrant/trill')
IMPORT_FILES_PATH = APPLICATION_FILEPATH + '/database-setup/load'

con = None

try:



    #connect to Trill data base as a super user
    con = psycopg2.connect("dbname='trill' user='vagrant'")
    cur = con.cursor()




    cur.execute("DELETE FROM user_skills")
    cur.execute("DELETE FROM user_jobs")
    cur.execute("DELETE FROM skills")
    cur.execute("DELETE FROM skill_titles")
    cur.execute("DELETE FROM trill_role_skill_groups")
    cur.execute("DELETE FROM skill_groups")
    cur.execute("DELETE FROM job_titles")
    cur.execute("DELETE FROM trill_role_groups")
    cur.execute("DELETE FROM users")


    usercsv = open(IMPORT_FILES_PATH + '/usershashed.csv', 'r')
    cur.copy_from(usercsv, 'users', sep=',')

    trillrolegroupscsv = open(IMPORT_FILES_PATH + '/TrillRoleGroups.csv', 'r')
    cur.copy_from(trillrolegroupscsv, 'trill_role_groups', sep=',')


    jobtitlescsv = open(IMPORT_FILES_PATH + '/jobtitles.csv', 'r')
    cur.copy_from(jobtitlescsv, 'job_titles', sep=',')


    skillgroupscsv = open(IMPORT_FILES_PATH + '/SkillGroups.csv', 'r')
    cur.copy_from(skillgroupscsv, 'skill_groups', sep=',')


    skilltitlescsv = open(IMPORT_FILES_PATH + '/SkillTitles.csv', 'r')
    cur.copy_from(skilltitlescsv, 'skill_titles', sep=',')

    skillscsv = open(IMPORT_FILES_PATH + '/Skill.csv', 'r')
    cur.copy_from(skillscsv, 'skills', sep=',')

    userjobscsv = open(IMPORT_FILES_PATH + '/UserJobs.csv', 'r')
    cur.copy_from(userjobscsv, 'user_jobs', sep=',')

    userskillscsv = open(IMPORT_FILES_PATH + '/UserSkills.csv', 'r')
    cur.copy_from(userskillscsv, 'user_skills', sep=',')

    trillroleskillgroupscsv = open(IMPORT_FILES_PATH + '/TrillRoleSkillGroups.csv', 'r')
    cur.copy_from(trillroleskillgroupscsv, 'trill_role_skill_groups', sep=',')

    con.commit()


except psycopg2.DatabaseError as e:

    if con:
        con.rollback()

    print("Error: {0}".format(e))
    sys.exit(1)

finally:

    if con:
        con.close()
