# configure client configration file

$file_path = '/etc/ssh/ssh_config'

file { $file_path:
  ensure  => 'required'
  content => 'PasswordAuthentication no
	      IdentityFile ~/.ssh/school'
}
