from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.filters import EventFilter
from api.models import Event
from api.serializers import FeedSerializer


class EventsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод всех событий пользователя"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventFilter
    queryset = Event.objects.all()
    lookup_field = 'user_id'
    serializer_class = FeedSerializer

    def get_queryset(self, **kwargs):
        """Получени queryset с событиями для конкретного пользователя"""
        user_id = self.kwargs.get('user_id')
        events = Event.objects.filter(user_id=user_id)
        return events

    def filter_queryset(self, queryset):
        """Добавляем в отфильтрованный queryset объявления"""
        queryset = super().filter_queryset(queryset)
        return queryset.get_events_list_with_adv()
