# automate creating of a custom HTTP header response
# using puppet

exec {'update':
  command => '/usr/bin/apt-get update -y',
}
-> package { 'nginx':
  ensure => 'present',
}
-> file_line { 'add_custom_header':
  path  => '/etc/nginx/sites-enabled/default',
  match => 'server_name _;',
  line  => "server_name _;\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
