from django.core.management.base import BaseCommand

from api.management.fixtures import load_fixtures


class Command(BaseCommand):

    models_list = [
        'Achievement',
        'User',
        'Advertisement',
        'Note',
        'Event',
    ]

    def handle(self, *args, **options):
        load_fixtures(self.models_list)
