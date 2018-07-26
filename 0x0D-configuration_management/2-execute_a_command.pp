# create manifest to kill process "killmenow"
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
  returns => [0]
}