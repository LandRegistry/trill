#!/bin/bash

echo "export PATH=$PATH:/usr/local/bin" > /etc/profile.d/local_bin.sh

source /etc/profile.d/local_bin.sh

echo "Cleaning Yum Cache"
yum clean all

echo "Refreshing Yum Cache"
yum makecache

echo "Installing Puppet Ruby Gems"
gem install --no-ri --no-rdoc puppet

echo "Installing Postgres Puppet Module"
puppet module install puppetlabs-postgresql

echo "Setting up TRILL database"
puppet apply /home/vagrant/trill/manifests/postgres.pp