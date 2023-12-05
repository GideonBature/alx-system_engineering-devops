# automate creating of a custom HTTP header response
# using puppet

exec {'update':
  command => '/usr/bin/apt-get',
}
-> package { 'nginx':
  ensure => 'present',
}
-> file_line { 'add_custom_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
