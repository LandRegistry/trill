#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import sys
import os
import csv

APPLICATION_FILEPATH = os.getenv('TRILL_APPLICATION_FILEPATH','/home/vagrant/trill')
IMPORT_FILES_PATH = APPLICATION_FILEPATH + '/database-setup/conversion/data'

con = None

try:

    #connect to Trill data base as a super user
    con = psycopg2.connect("dbname='trill' user='vagrant'")
    cur = con.cursor()

    cur.execute("DELETE FROM skill_role_stage")

    ln = 0
    stmt = "INSERT INTO skill_role_stage VALUES (%(trill_role_group)s, %(skillgroup)s)"
    with open(IMPORT_FILES_PATH + '/role_group_live.csv', encoding='utf-8', errors='ignore') as csvfile:
        r = csv.DictReader(csvfile, dialect='excel', fieldnames=("trill_role_group","skillgroup"))
        for datarow in r:
            datarow['trill_role_group'] = datarow['trill_role_group'].strip()
            datarow['skillgroup'] = datarow['skillgroup'].replace('  ',' ').strip()
            cur.execute(stmt, datarow)
            ln += 1

    con.commit()
    cur.execute("SELECT count(*) FROM skill_role_stage;")
    c = cur.fetchone()


except psycopg2.DatabaseError as e:

    if con:
        con.rollback()

    print("Error: {0}".format(e))
    sys.exit(1)

finally:
    print(str(ln) + " rows processed from file")
    print(str(c[0]) + " rows fetched from database")
    if con:
        con.close()
