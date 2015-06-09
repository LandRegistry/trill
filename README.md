# TRILL - Training & Skills

##Dependencies:
- Oracle Virtualbox
- Vagrant
- Postgres
- Python 3


##How to use it:

###Important note for Windows users

If you are using a Windows machine, set the following option for Git BEFORE you clone the repository.

```
git config --global core.autocrlf false
```

###Start the virtual machine.

```
vagrant up
```

```
vagrant ssh
```
###Setup database tables

```
source environment.sh
python3 manage.py db upgrade
```

###Load tables with test data

```
python3 /home/vagrant/trill/database-setup/load/loadDB.py
```
###Run the app:

```
source run_dev.sh
```

Hitting 'localhost:5000' on the browser should give you the GDS skills page.

###Run unit tests for the app:

```
source test.sh
```
