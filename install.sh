#!/bin/bash

dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $dir

echo "Installing Python Modules"
pip3 install -r requirements_base.txt
pip3 install -r requirements_deploy.txt
