"""
WSGI config for django_waitlist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django_waitlist.settings import PROJECT_ROOT

# import tcell_agent
# tcell_agent.init()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_waitlist.settings")

application = get_wsgi_application()

# try:
#     # Capture revision of running uwsgi
#     # Assumes you run chdir with uwsgi
#     if os.getenv('DOCKER_DEV'):
#         bhash = 'hash'
#     else:
#         from subprocess import check_output
#         bhash = check_output(['git','rev-parse','HEAD'])
#     rev = open(os.path.join( PROJECT_ROOT, 'revision.txt') ,'wb')
#     rev.write(bhash)
#     rev.close()
# 
#     # Drop file for healthy check
#     text = "This file exists only when uwsgi is healthy. Remove it to pool from LB pool"
#     health = open( os.path.join( PROJECT_ROOT, 'health.check' ) ,'wb')
#     health.write(text)
#     health.close()
# except:
#     import traceback
#     print traceback.format_exc()
