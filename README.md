# AIScrapy


**Activating source file in Linux and Mac**

```
virtualenv env
source env/bin/activate

source .env
python -m pip install -r requirement.txt
python manage.py runserver

```





**Configure Gunicorn Services with.Env**

```
sudo nano /etc/systemd/system/gunicorn.socket

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target




sudo nano /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/aiscrapy_website
EnvironmentFile=/home/ubuntu/aiscrapy_website/.env
ExecStart=/home/ubuntu/aiscrapy_website/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          website.wsgi:application
```



**Configure Ngix Services for gunicorn**
```
/etc/nginx/sites-available/aiscrapy

server {
    listen 80;
    server_name aiscrapy.com www.aiscrapy.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/aiscrapy_website;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```
**Obtaining an SSL Certificate And Server Deployment**
```
https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04
```
