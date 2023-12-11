# File: nginx_setup.pp

# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Manage Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Configure Nginx site
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create a template for Nginx site configuration
file { '/etc/nginx/sites-available/default.erb':
  ensure => file,
  content => '# Nginx default site configuration template
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        return 200 "Hello, World!\n";
    }

    location /redirect_me {
        return 301 http://$host/;
    }
}',
  require => Package['nginx'],
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}
