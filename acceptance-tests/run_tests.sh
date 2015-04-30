#!/bin/bash

set -e

rm -rf sshot*

source ../environment.sh
source ../environment_test.sh

bundle install

if [ -z "$1" ]
  then
    cucumber --tags ~@wip
  else
    cucumber $@
fi
