#!/bin/bash

set -e

rm -rf sshot*

source ../environment.sh

bundle install

if [ -z "$1" ]
  then
    bundle exec cucumber --tags ~@wip
  else
    bundle exec cucumber $@
fi
