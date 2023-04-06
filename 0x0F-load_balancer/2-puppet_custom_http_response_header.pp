#!/usr/bin/env bash
# We automate the task of creating a custom HTTP header response, but with Puppet.

sudo apt-get update
sudo apt-get install puppet-agent

lass apache {
  package { 'apache2':
    ensure => installed,
  }

  service { 'apache2':
    ensure  => running,
    enable  => true,
    require => Package['apache2'],
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => "<html><head><title>Hello World</title></head><body><h1>Hello World!</h1></body></html>",
    require => Package['apache2'],
  }

  file { '/etc/apache2/sites-available/000-default.conf':
    ensure  => file,
    content => "# Custom Apache configuration\n<VirtualHost *:80>\n    ServerName example.com\n    ServerAdmin webmaster@localhost\n    DocumentRoot /var/www/html\n    ErrorLog ${APACHE_LOG_DIR}/error.log\n    CustomLog ${APACHE_LOG_DIR}/access.log combined\n</VirtualHost>\n",
    require => Package['apache2'],
    notify  => Service['apache2'],
  }
}

sudo puppet apply /etc/puppetlabs/code/environments/production/manifests/apache.pp


