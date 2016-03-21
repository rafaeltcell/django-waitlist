from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "django_waitlist"

    def ready(self):
        import_module("django_waitlist.receivers")
