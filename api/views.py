from rest_framework import viewsets


class EventsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод всех событий пользователя"""
    search_fields = ['username', 'email', 'profile__profession']

