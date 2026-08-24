# _*_ mode: ruby -*-
# vi: set ft=ruby

Vagrant.configure("2") do |config|
    # Base VM OS Configuration
    config.vm.box = "generic/rocky9"
    config.ssh.insert_key = false
    config.vm.synced_folder ".", "/vagrant", disabled: true
    config.vm.provider :libvirt do |libvirt| # Using libvirt because my control node runs fedora and I personally use libvirt, qemu and KVM
        # Using QEMU system connection for better perfomance and feature support
        libvirt.qemu_use_session = false
        libvirt.memory = "1024"
        libvirt.cpus = 1
    end

    # VM1: HAProxy Load Balancer
    config.vm.define "lb" do |lb|
        lb.vm.hostname = "haxproxy"
        lb.vm.network "private_network", ip: "192.168.56.4"
    end

    # VM2: Webserver 1
    config.vm.define "web1" do |web1|
        web1.vm.hostname = "web1"
        web1.vm.network "private_network", ip: "192.168.56.5"
    end

    # VM3: Webserver 2
    config.vm.define "web2" do |web2|
        web2.vm.hostname = "web2"
        web2.vm.network "private_network", ip: "192.168.56.6"
    end

    # VM4: Database
    config.vm.define "db" do |db|
        db.vm.hostname = "db"
        db.vm.network "private_network", ip: "192.168.56.7"
    end
end