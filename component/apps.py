from django.apps import AppConfig


class ComponentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "component"


class MyAppConfig(AppConfig):
    name = 'component'

    def ready(self):
        import component.signals



from django.apps import AppConfig
class componentConfig(AppConfig):
    name = 'component'
    def ready(self):
        import component.signals



# apps.py
from django.apps import AppConfig
class YourAppNameConfig(AppConfig):
    name = 'component'
    def ready(self):
        import component.signals

