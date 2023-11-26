# configure client configration file

$file_path = '/etc/ssh/ssh_config'

file { $file_path:
  ensure  => 'present',
  content => "
	# SSH Client Configuration
	host*
	PasswordAuthentication no
	IdentityFile ~/.ssh/school
	"
}
