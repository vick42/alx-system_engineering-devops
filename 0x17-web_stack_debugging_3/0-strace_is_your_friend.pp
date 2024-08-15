#For this project I utilised strace followed by Puppet to automate th patch for 500 error on apache

exec { 'fix_typo':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  provider => 'shell'}
