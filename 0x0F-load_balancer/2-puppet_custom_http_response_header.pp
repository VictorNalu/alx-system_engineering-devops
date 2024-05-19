# This Puppet manifest installs and configures Nginx to add a custom HTTP response header

# Ensure the Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running and enabled to start at boot
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

# Manage the Nginx default site configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Create the Nginx module directory structure
file { '/etc/puppetlabs/code/environments/production/modules/nginx':
  ensure => directory,
}

file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates':
  ensure => directory,
}

# Create a template file for the Nginx configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => @("END"),
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    
    server_name _;
    
    location / {
        try_files \$uri \$uri/ =404;
    }
    
    add_header X-Served-By <%= @hostname %>;
}
| END
}

# Gather the hostname fact
$hostname = $facts['networking']['hostname']
