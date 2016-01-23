Instructions
============

- Follow the instructions given in [here](https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial/)
- Copy and paste the below script in the **wsgi** file under the **Web tab** section. 
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
- Clone https://github.com/ananth95/saber_backend repository into your pythonanywhere account
 