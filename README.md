Instructions
============

- To install Django in Pythonanywhere
	- Open Bash console and run 
```sh
mkvirtualenv django17 --python=/usr/bin/python3.4
pip install django
```
- Clone https://github.com/ananth95/saber_backend repository into your pythonanywhere account (`clone it in root folder /home/yourusername`)
	- Command to clone
```
git clone https://github.com/ananth95/saber_backend
```
- Copy and paste the below script in the link to edit **wsgi file configuration** under the **Web tab**. 
  Change `yourusername` in the script
```py
import os
import sys

path = '/home/yourusername/saber_backend'
if path not in sys.path:
	sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'saber_backend.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
- To Set up the virtual environment
	- Go to the *Virtualenv* section under the **Web tab** and set the path as
	  `/home/myusername/.virtualenvs/django17`
	  Change `myusername` in the above path
- Open Bash console in `saber_backend` folder and run 
```sh
python manage.py makemigrations
python manage.py migrate
```