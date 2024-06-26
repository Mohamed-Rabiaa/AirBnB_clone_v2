#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

dirs_arr=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/"
            "/data/web_static/releases/test/")
for dir in "${dirs_arr[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir "$dir"
    fi
done

if [ ! -f "/data/web_static/releases/test/index.html" ]; then
    echo "<html>
  <head>
  </head>
  <body>
  Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
fi

if [ -L "/data/web_static/current" ]; then
    rm "/data/web_static/current"
fi
ln -s "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -R ubuntu:ubuntu /data/

if ! sudo grep -q "location /hbnb_static/" /etc/nginx/sites-available/default; then
    sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
fi
service nginx restart
