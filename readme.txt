pip list:{
    Django (1.10.4)
    flake8 (3.2.1)
    mccabe (0.5.3)
    pep8 (1.7.0)
    pip (9.0.1)
    pycodestyle (2.2.0)
    pyflakes (1.3.0)
    setuptools (31.0.1)
    wheel (0.29.0)
}

python{
    version: 3.5.2
    venv.dir: C:\Python\env\myenv\Scripts
}

django.superuser{
    user: admin
    mail: admin@admin.ru
    pass: User1377
}

django run server {
    source celeryenv/bin/activate
    gunicorn mysite.wsgi:application --bind 127.0.0.1:8000 -t 120 -w 2 # время ожидания 120 сек, 2 процесса
    celery -A mysite worker -l info
}

проект развернут на Amazon.
В папке ~/mysite - лежит проект
Разварачивание на Nginx and Gunicorn
Окружение python в папке ~/celeryenv
Настройки nginx в /etc/nginx/sites-available/default
Для запуска gunicorn, активировать окружение python3:
source ~/celeryenv/bin/activate
и собственно запустить:
cd mysite
gunicorn mysite.wsgi:application --bind 127.0.0.1:8000 -t 120 -w 2 # время ожидания 120 сек, 2 процесса

-------------- nginx setting ----------------------------

##
# You should look at the following URL's in order to grasp a solid understanding
# of Nginx configuration files in order to fully unleash the power of Nginx.
# http://wiki.nginx.org/Pitfalls
# http://wiki.nginx.org/QuickStart
# http://wiki.nginx.org/Configuration
#
# Generally, you will want to move this file somewhere, and start with a clean
# file but keep this around for reference. Or just disable in sites-enabled.
#
# Please see /usr/share/doc/nginx-doc/examples/ for more detailed examples.
##

#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
#server {
#	listen 80;
#	listen [::]:80;
#
#	server_name example.com;
#
#	root /var/www/example.com;
#	index index.html;
#
#	location / {
#		try_files $uri $uri/ =404;
#	}
#}


server {
    listen 80;
    server_name 0.0.0.0; #либо ip, либо доменное имя
    access_log  /var/log/nginx/example.log;

    location /static/ {
        root /home/ubuntu/mysite/;
        expires 30d;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  }

-------------- nginx setting end ------------------------