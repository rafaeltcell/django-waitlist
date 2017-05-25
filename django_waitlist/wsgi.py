import os

from django.core.wsgi import get_wsgi_application
from django.test import RequestFactory
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_waitlist.settings")

application = get_wsgi_application()
application.load_middleware()

url = '/'
# request = RequestFactory().get(url, HTTP_HOST='127.0.0.1', SERVER_PORT='3000')
request = RequestFactory().get(url, HTTP_HOST='127.0.0.1')
print(request)

# for middleware_method in application._request_middleware:
    # print(middleware_method)
    # response = middleware_method(request)
    # if response:
        # break
