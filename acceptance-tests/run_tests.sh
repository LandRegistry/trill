#!/bin/bash

# Commented for the time being to prevent the entire shell session bombing out if
# any of the called scripts/programs fail (MG 01/05/15)
# set -e

rm -rf sshot*

source ../environment.sh

bundle install

if [ -z "$1" ]
  then
    cucumber --tags ~@wip
  else
    cucumber $@
fi
