#!/bin/bash

localectl set-locale LANG=en_GB.UTF-8
timedatectl set-timezone Europe/London
sudo -i -u vagrant source /home/vagrant/trill/install.sh
