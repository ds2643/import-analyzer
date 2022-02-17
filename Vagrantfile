# Install required plugins
required_plugins = %w( vagrant-vbguest )
required_plugins.each do |plugin|
    exec "vagrant plugin install #{plugin};vagrant #{ARGV.join(" ")}" unless Vagrant.has_plugin? plugin || ARGV[0] == 'plugin'
end


Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-18.04"
  config.vm.box_version = "202112.19.0"

  config.vm.provider "virtualbox" do |v|
    v.name = "voltus"
    v.cpus = 2
    v.memory = 2048
  end

  # Git ssh configuration
  config.ssh.forward_agent = true

  config.vm.provision "shell", path: "bootstrap.sh", env: {
	"BASH_ENV" => "/home/vagrant/.bashrc",
	"DEBIAN_FRONTEND" => "noninteractive"
  }

  # Start at repository root when you ssh into the vm
  config.ssh.extra_args = ["-t", "cd /vagrant; bash "]

  config.vbguest.auto_update = false
  config.vbguest.no_remote = true

  # Port forwarding for externally visible ports
  APPLICATION_PORTS={
  }

  for port in APPLICATION_PORTS.map { |project,port| port }
  	config.vm.network :forwarded_port, guest: port, host: port
  end

end
