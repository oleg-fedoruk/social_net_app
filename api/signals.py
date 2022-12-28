from django.contrib.contenttypes.models import ContentType

from api.models import Event, Achievement


def achievements_changed(sender, **kwargs):
    user = kwargs.get('instance')
    achievement_pk_set = kwargs.get('pk_set')
    action = kwargs.get('action')
    if action == 'post_add' and achievement_pk_set is not None:
        for achievement_pk in achievement_pk_set:
            Event.objects.create(
                user=user,
                object_id=achievement_pk,
                content_type=ContentType.objects.get_for_model(Achievement)
            )


def note_created(sender, **kwargs):
    note = kwargs.get('instance')
    created = kwargs.get('created')
    if created:
        Event.objects.create(
            user_id=note.creator_id,
            content_object=note,
        )
