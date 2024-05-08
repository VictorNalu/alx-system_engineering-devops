# setting up my client config file

# Check if ssh config file exists and has the right permissions

file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "\
Host 54.236.25.139
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  ",
}
