from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self) -> None:
            # Without this import, admin panel will not include this app
            from core import admin  # noqa: F401 (unused-import)