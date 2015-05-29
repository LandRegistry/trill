#!/usr/bin/python3
# -*- coding: utf-8 -*-

from werkzeug.security import generate_password_hash
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

    cur.execute("DELETE FROM people_role_stage")

    ln = 0
    stmt = "INSERT INTO people_role_stage VALUES (%(firstname)s, %(surname)s, %(email)s, %(trill_role_group)s, %(managerfirstname)s, %(managersurname)s, %(job_title)s, %(encrypted_passwd)s)"
    with open(IMPORT_FILES_PATH + '/people_data_live.csv') as csvfile:
        r = csv.DictReader(csvfile, fieldnames=("firstname","surname","email","trill_role_group","managerfirstname","managersurname","job_title","encrypted_passwd"))
        for datarow in r:
            # Encrypt the password
            encrypted_passwd = generate_password_hash(datarow['encrypted_passwd'])
            datarow['encrypted_passwd'] = encrypted_passwd
            # Remove manager details as per requirements
            datarow['managerfirstname'] = ''
            datarow['managersurname'] = ''
            # Remove padding values if they exist in the file
            if None in datarow:
                datarow.pop(None)
            cur.execute(stmt, datarow)
            ln += 1

    con.commit()
    cur.execute("SELECT count(*) FROM people_role_stage;")
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
