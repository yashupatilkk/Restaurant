from django.apps import AppConfig

class BaseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Base_App'

    def ready(self):
        pass  # Remove any unnecessary imports like `import Base_App.signals`

