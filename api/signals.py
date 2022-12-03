from api.models import Event
from social_net.consts import GOT_ACHIEVEMENT, NOTE_CREATED


def achievements_changed(sender, **kwargs):
    user = kwargs.get('instance')
    achievement_pk_set = kwargs.get('pk_set')
    action = kwargs.get('action')
    if action == 'post_add' and achievement_pk_set is not None:
        for achievement_pk in achievement_pk_set:
            Event.objects.create(
                user=user,
                achievement_id=achievement_pk,
                type=GOT_ACHIEVEMENT
            )


def note_created(sender, **kwargs):
    note = kwargs.get('instance')
    created = kwargs.get('created')
    if created:
        Event.objects.create(
            user_id=note.creator_id,
            note=note,
            type=NOTE_CREATED
        )
