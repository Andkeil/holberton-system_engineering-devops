# Puppet script to better handle many http requests on nginx
exec { 'mod-rlimits':
  path    => ['/bin/', '/usr/bin/'],
  command => "sudo sed -i 's/.*worker_processes.*/worker_processes 10;/' /etc/nginx/nginx.conf;
  sudo sed -i '/worker_processes 10;/a worker_rlimit_nofile 5000;' /etc/nginx/nginx.conf;
  sudo service nginx restart"
}