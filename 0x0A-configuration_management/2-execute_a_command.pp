# manifest that kills a process named killmenow

$process_name = 'killmenow'

exec { $process_name:
  command => '/usr/bin/pkill -f killmenow'
}
