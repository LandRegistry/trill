from werkzeug.security import generate_password_hash
import csv

ofile = open('usershashed.csv', 'w')
usewriter = csv.writer(ofile,delimiter=',')

with open('users.csv', 'r') as ifile:
    userreader = csv.reader(ifile)
    for row in userreader:
        print(', '.join(row))
        pwHash = generate_password_hash(row.pop())
        row.append(pwHash)
        usewriter.writerow(row)

ifile.close()
ofile.close()
