from werkzeug.security import generate_password_hash, check_password_hash
import sys

with open('/home/vagrant/trill/database-setup/load/users.csv', 'r') as f:
    for line in f:
        print (line)
