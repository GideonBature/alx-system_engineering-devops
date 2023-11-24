# create a file in /tmp

$dir_path = '/tmp'
$file_path = '/tmp/school'

file { $dir_path:
  ensure => 'directory',
}

file { $file_path:
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}
