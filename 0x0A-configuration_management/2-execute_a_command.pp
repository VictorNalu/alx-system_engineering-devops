# This Puppet manifest kills a process named "killmenow"

exec { 'kill':
command => 'pkill killmenow',
path    => '/usr/bin/',
}
