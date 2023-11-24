# create a file in /tmp

$dir_path = '/tmp'
$file_path = '/tmp/school'

file { $dir_path:
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0744'
}

file { $file_path:
  ensure  => 'file',
  content => 'I love Puppet'
}
