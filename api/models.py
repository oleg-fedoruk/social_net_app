from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from social_net.consts import EVENT_TYPES, NOTE_CREATED, GOT_ACHIEVEMENT


class User(AbstractUser):
    objects = UserManager()

    achievements_received = models.ManyToManyField(
        'Achievement', related_name='users',
        verbose_name='Полученные достижения', blank=True, null=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Note(models.Model):
    header = models.CharField(max_length=64, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Тело')
    created_at = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, verbose_name="Создатель", on_delete=models.CASCADE, related_name='notes')

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
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Event(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    type = models.CharField(choices=EVENT_TYPES, verbose_name='Тип события', max_length=64)
    created_at = models.DateField(auto_now_add=True, verbose_name='Время события')

    achievement = models.ForeignKey(Achievement, verbose_name='Полученное достижение', on_delete=models.CASCADE, null=True, blank=True)
    note = models.ForeignKey(Note, verbose_name='Созданная заметка', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.type == NOTE_CREATED:
            return f'Пользователь {self.user.username} создал заметку {self.note.header}'
        elif self.type == GOT_ACHIEVEMENT:
            return f'Пользователь {self.user.username} получил достижение {self.achievement.name}'

    class Meta:
        ordering = ["created_at"]
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

