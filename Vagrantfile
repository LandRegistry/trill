# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

$xtra_prov = <<SCRIPT
localectl set-locale LANG=en_GB.UTF-8
timedatectl set-timezone Europe/London
sudo -i -u vagrant source /home/vagrant/trill/install.sh
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
  config.vm.box = "landregistry/centos-beta"
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.synced_folder ".", "/home/vagrant/trill", create: true
  config.vm.provision :shell, :path => 'provision.sh'
  config.vm.provision :shell, :inline => $xtra_prov
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  
end
