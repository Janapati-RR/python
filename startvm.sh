 #! /bin/bash
 apt-get update
 apt-get install apache2 -y
 a2ensite default-ssl
 a2enmod ssl
 gsutil -m cp -r gs://suntechno/* /var/www/html/
  systemctl restart apache2