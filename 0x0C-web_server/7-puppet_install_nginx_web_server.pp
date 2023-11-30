# install nginx with puppet

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get -y update; sudo apt-get -y install nginx',
  provider => shell,
}

exec {'Hello World!':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'sudo sed -i "s/server_name _;/server_name _;\n\n\tlocation \/redirect_me {\n\t\t return 301 https:\/\/www.google.com;\n\t}" \
/etc/nginx/sites-enabled/default':
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
