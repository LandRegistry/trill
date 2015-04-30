#!/bin/bash

dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $dir

if [ ! -d ${HOME}/.rbenv ]
then
  echo "Installing Rbenv Ruby Environment Manager"
    git clone https://github.com/sstephenson/rbenv.git ${HOME}/.rbenv
    echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ${HOME}/.bash_profile
    echo 'eval "$(rbenv init -)"' >> ${HOME}/.bash_profile
    source ${HOME}/.bash_profile
  echo "Installing Ruby-Build Plugin"
    git clone https://github.com/sstephenson/ruby-build.git ${HOME}/.rbenv/plugins/ruby-build
  echo "Building Ruby 1.9.3 environment. This will take several minutes to complete ..."
    curl -fsSL "https://github.com/ruby/ruby/commit/0d58bb55985e787364b0235e5e69278d0f0ad4b0.patch" | \
    filterdiff -x a/ChangeLog | rbenv install --patch 1.9.3-p362
    rbenv rehash
fi

echo "Activating Ruby 1.9.3"
  rbenv global 1.9.3-p362
  rbenv rehash

echo "Installing Bundler"
  gem install  --no-ri --no-rdoc bundler
  rbenv rehash

echo "Installing Ruby Gems"
  bundle install
  rbenv rehash
