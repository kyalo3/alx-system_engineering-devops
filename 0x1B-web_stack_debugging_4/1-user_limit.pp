exec { 'increase-hard-file-limit-for-holberton-user':
  # modify the UNLIMIT value
  command => 'bash -c "sudo sed -i "/^holberton hard/s/4/50000/" /etc/security/limits.conf"',
  # specify the path for the sed command
  path    => '/usr/local/bin/:/bin',
}

# restart Nginx
exec { 'increase-soft-file-limit-for-holberton-user':
  # Restart Nginx service
  command => 'bash -c "sudo sed -i "/^holberton soft/s/5/50000/" /etc/security/limits.conf"',
  # specify the path for the init.d script
  path    => '/usr/local/bin/:/bin/',
}
