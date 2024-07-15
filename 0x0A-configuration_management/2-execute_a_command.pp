#Executes a bash command

exec { 'Terminate-Process':
	command => '/usr/bin/pkill -f killmenow'
}
