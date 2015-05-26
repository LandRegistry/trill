from werkzeug.security import generate_password_hash
import csv
import os

APPLICATION_FILEPATH = os.getenv('TRILL_APPLICATION_FILEPATH','/vagrant/home/trill')
IMPORT_FILES_PATH = APPLICATION_FILEPATH + '/database-setup/load'

ofile = open(IMPORT_FILES_PATH + '/usershashed.csv', 'w')
usewriter = csv.writer(ofile,delimiter=',')

with open(IMPORT_FILES_PATH + '/users.csv', 'r') as ifile:
    userreader = csv.reader(ifile)
    for row in userreader:
        print(', '.join(row))
        pwHash = generate_password_hash(row.pop())
        row.append(pwHash)
        usewriter.writerow(row)

ifile.close()
ofile.close()
