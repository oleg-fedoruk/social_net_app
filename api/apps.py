from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from django.db.models.signals import m2m_changed, post_save
        from api.models import User, Note
        from api.signals import achievements_changed, note_created
        m2m_changed.connect(achievements_changed, sender=User.achievements_received.through)
        post_save.connect(note_created, sender=Note)
