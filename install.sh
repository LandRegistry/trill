#!/bin/bash

dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $dir

echo "Installing Python Modules"
sudo -i pip3 install -r $dir/requirements.txt
