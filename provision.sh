#!/bin/bash

echo "Setting UK locale and timezone"
localectl set-locale LANG=en_GB.UTF-8
timedatectl set-timezone Europe/London

echo "Adding PATH for local components"
echo "export PATH=$PATH:/usr/local/bin" > /etc/profile.d/local_bin.sh
source /etc/profile.d/local_bin.sh

echo "Cleaning Yum Cache"
yum clean all

echo "Refreshing Yum Cache"
yum makecache

echo "Installing Development Tools"
yum install -y gcc openssl-devel libyaml-devel libffi-devel readline-devel zlib-devel gdbm-devel ncurses-devel ruby-devel rubygems httpd httpd-devel

echo "Installing Puppet Ruby Gems"
gem install --no-ri --no-rdoc puppet -v 3.7.5

echo "Installing Postgres Puppet Module"
puppet module install puppetlabs-postgresql

echo "Setting up TRILL database"
puppet apply /home/vagrant/trill/manifests/postgres.pp

echo "Adding PATH for PostgreSQL 9.3"
if [ -d /usr/pgsql-9.3/bin ]; then
  echo "export PATH=/usr/pgsql-9.3/bin:$PATH" > /etc/profile.d/pgsql-9.3.sh
  source /etc/profile.d/pgsql-9.3.sh
fi

echo "Checking to see if PhantomJS is installed ..."
PHANTOM_JS="phantomjs-1.9.7-linux-x86_64"
PHANTOM_JS_BIN="/usr/bin/phantomjs"
if [ ! -e $PHANTOM_JS_BIN ]
then
  echo "Installing PhantomJS"
  echo "Downloading PhantomJS source"
  wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 > /dev/null 2>&1
  echo "Setting up"
  mv $PHANTOM_JS.tar.bz2 /usr/local/share/
  cd /usr/local/share/
  tar xvjf $PHANTOM_JS.tar.bz2
  ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/share/phantomjs
  ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin/phantomjs
  ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/bin/phantomjs
  rm -f $PHANTOM_JS.tar.bz2
else
  echo "PhantomJS already installed.. moving on"
fi
