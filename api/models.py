from datetime import timedelta, datetime
from itertools import chain
from operator import attrgetter

from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from social_net.consts import TERM_OF_ADV


class EventsQuerySet(models.query.QuerySet):
    """Расширенный queryset для объектов Event"""

    def get_events_list_with_adv(self):
        advertisements = Advertisement.objects.filter(created_at__gte=(datetime.now() - timedelta(TERM_OF_ADV)))
        result_list = sorted(
            chain(self, advertisements),
            key=attrgetter('created_at'), reverse=True)
        return result_list


class EventsManager(models.Manager):
    """Обновлённый менеджер для модели Event"""

    def get_queryset(self):
        return EventsQuerySet(self.model, using=self._db)


class Event(models.Model):
    """События для ленты пользователей"""
    user = models.ForeignKey('User', verbose_name='Пользователь', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время события')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = EventsManager()

    @property
    def header(self):
        return self.__str__()

    def __str__(self):
        if self.content_type.model == 'note':
            return f'Пользователь {self.user.username} создал заметку {self.content_object.header}'
        elif self.content_type.model == 'achievement':
            return f'Пользователь {self.user.username} получил достижение {self.content_object.name}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class User(AbstractUser):
    objects = UserManager()

    achievements_received = models.ManyToManyField(
        'Achievement', related_name='users',
        verbose_name='Полученные достижения', blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Note(models.Model):
    header = models.CharField(max_length=64, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Тело')
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, verbose_name="Создатель", on_delete=models.CASCADE, related_name='notes')
    events = GenericRelation(Event, related_query_name='notes')

    def __str__(self):
        return self.header

    class Meta:
        ordering = ["created_at"]
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'


class Achievement(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название достижения')
    condition_for_obtaining = models.TextField(verbose_name='Условие получения')
    icon = models.ImageField('Иконка', upload_to='icons/')
    events = GenericRelation(Event, related_query_name='achievements')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class Advertisement(models.Model):
    header = models.CharField(max_length=64, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField('Изображение', upload_to='images/')
    link = models.URLField(verbose_name='Ссылка на рекламируемый ресурс')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
