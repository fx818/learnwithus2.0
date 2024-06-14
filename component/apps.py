from django.apps import AppConfig


class ComponentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "component"


# myapp/apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'component'

    def ready(self):
        import component.signals
