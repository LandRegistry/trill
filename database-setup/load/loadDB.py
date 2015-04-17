#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import sys



con = None

try:

    #connect to Trill data base as a super user
    con = psycopg2.connect("dbname='trill' user='vagrant'")
    cur = con.cursor()

    usercsv = open('/home/vagrant/trill/database-setup/load/users.csv', 'r')
    cur.execute("DELETE FROM users")
    cur.copy_from(usercsv, 'users', sep=',')

    jobtitlescsv = open('/home/vagrant/trill/database-setup/load/jobtitles.csv', 'r')
    cur.execute("DELETE FROM job_titles")
    cur.copy_from(jobtitlescsv, 'job_titles', sep=',')

    #skillscsv = open('/home/vagrant/trill/skills.csv', 'r')
    #cur.execute("DELETE FROM skills")
    #cur.copy_from(skillscsv, 'skills', sep=',')

    con.commit()


except psycopg2.DatabaseError as e:

    if con:
        con.rollback()

    print("Error: {0}".format(e))
    sys.exit(1)

finally:

    if con:
        con.close()
