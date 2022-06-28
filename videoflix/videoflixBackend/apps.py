from django.apps import AppConfig


class VideoflixbackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videoflixBackend'

    def ready(self): 
        from . import signals 
