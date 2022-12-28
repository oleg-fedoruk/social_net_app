import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_net.settings')
application = get_wsgi_application()

from django.core.management import call_command

app_name = 'api'
models_list = [
    'User',
    'Achievement',
    'Advertisement',
    'Note',
    'Event',
]


def load_fixtures(models_list: list):
    """Последовательно заполняет БД фикстурами"""
    for model in models_list:
        call_command('loaddata', f'{model}.json')


def create_fixtures(app_name: str, models_list: list):
    """ Создаёт/обновляет фикстуры из заполненной БД"""
    for model_name in models_list:
        call_command('dumpdata', '--natural-foreign', f'{app_name}.{model_name}', '-o', f'{model_name}.json')


if __name__ == '__main__':
    create_fixtures(app_name, models_list)
