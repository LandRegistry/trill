# TRILL - Training & Skills

##Dependencies:
- Oracle Virtualbox
- Vagrant
- Postgres
- Python 3


##How to use it:

###Start the virtual machine.

```
vagrant up
```

```
vagrant ssh
```

###Run the dummy app:

```
python3 run.py
```

Hitting 'localhost:5000' on the browser should give you a page that says 'Everything is OK'.

###Run unit tests for the app:

```
source test.sh
```
