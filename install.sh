#!/bin/bash

dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $dir

if [ -d /usr/pgsql-9.3/bin ]; then
  export PATH=$PATH:/usr/pgsql-9.3/bin
fi
sudo env "PATH=$PATH" pip3 install -r requirements.txt