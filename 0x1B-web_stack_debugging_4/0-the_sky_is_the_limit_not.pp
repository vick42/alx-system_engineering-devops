# This increases nginx open file limit to 4096
exec { 'Change nginx limit':
  command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
  provider => shell,
}
