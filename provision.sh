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
