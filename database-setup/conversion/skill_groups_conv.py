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

    cur.execute("DELETE FROM skill_mapping_stage")

    ln = 0
    stmt = "INSERT INTO skill_mapping_stage VALUES (%(skilltype)s, %(skillgroup)s, %(skilltitlename)s, %(skilldescription)s, %(skillcode)s)"
    with open(IMPORT_FILES_PATH + '/skill_data_live.csv', encoding='utf-8', errors='ignore') as csvfile:
        r = csv.DictReader(csvfile, dialect='excel', fieldnames=("skilltype","skillgroup","skilltitlename","skilldescription","skillcode"))
        for datarow in r:
            if datarow['skilltype'] == 'GDS':
                datarow['skilltype'] = 1
            elif datarow['skilltype'] == 'IS':
                datarow['skilltype'] = 2
            elif datarow['skilltype']  == 'ISK':
                datarow['skilltype'] = 3
            datarow['skillgroup'] = datarow['skillgroup'].replace('  ',' ').strip()
            datarow['skilltitlename'] = datarow['skilltitlename'].strip()
            datarow['skilldescription'] = datarow['skilldescription'].replace('  ',' ').strip()
            cur.execute(stmt, datarow)
            ln += 1

    con.commit()
    cur.execute("SELECT count(*) FROM skill_mapping_stage;")
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
