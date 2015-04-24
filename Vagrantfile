# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "landregistry/centos-beta"
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.synced_folder ".", "/home/vagrant/trill", create: true
  config.vm.provision "standard", type: "shell", :path => 'provision.sh'
  config.vm.provision "test_fwk", type: "shell", :path => 'test_fwk_provision.sh'
  config.vm.provision "extras", type: "shell", :path => 'extra_provision.sh'
  config.vm.network "forwarded_port", guest: 5000, host: 5000

end
