"""
WSGI config for django_waitlist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# import tcell_agent
# tcell_agent.init()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_waitlist.settings")

application = get_wsgi_application()
application.load_middleware()

# import newrelic.agent
# application = newrelic.agent.WSGIApplicationWrapper(application)

# os.environ['TCELL_AGENT_CONFIG'] = '/app/tcell_agent.config'
# os.environ['TCELL_AGENT_HOME'] = '/app/tcell'
