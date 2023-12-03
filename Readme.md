To create a python virtual environment:
1 - check the python version:
1.1 - python3 -V (in my case is python 3.11)
1 - mkdir venv
2 - cd venv
3 - python3.11 -m venv .
4 - activate the venv:
4.1 - cd ..
4.2 - source ./venv/bin/activate

Install django:
1 - pip install django

Start django project:
1 - django-admin startproject projectname

Start an app within the project (one project can be composed by several apps):
1 - python manage.py startapp appname

Run django server:
1 - python manage.py runserver

Create migrations and migrate:
1 - python manage.py makemigrations
2 - python manage.py migrate

Extra tips:
1 - in osx you could have problems with mysqlclient installarion (pip install mysqlclient).
2 - To solve:
2.1 - bbrew install mysql-client pkg-config
2.2 - export PKG_CONFIG_PATH="/usr/local/opt/mysql-client/lib/pkgconfig"
2.3 - pip install mysqlclient
3 - Use django and bootstrap
3.1 - pip install django-bootstrap4
3.2 - add bootstrap4 in INSTALLED_APPS in settings.py
