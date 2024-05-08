# Update the system
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

# Install nginx package
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

# Create index.html with "Hello World!" content
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Add a rewrite rule for the /redirect_me endpoint in the nginx configuration
exec { 'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/@naturethrillers/videos permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

# Ensure nginx service is running
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
