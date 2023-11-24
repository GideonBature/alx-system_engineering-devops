# install flask from pip3 using puppet

$pkg_name = 'flask'

package { $pkg_name:
  ensure   => '2.1.0',
  provider => 'pip3'
}
