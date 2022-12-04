from rest_framework import viewsets, filters
from rest_framework.response import Response

from api.models import Event, Advertisement
from api.serializers import EventSer, AdvertisementSer


class EventsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод всех событий пользователя"""
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'note__header', 'achievement__name', 'type']

    queryset = Event.objects.all()
    lookup_field = 'user_id'
    serializer_class = EventSer

    def get_queryset(self, **kwargs):
        """Получени queryset с событиями для конкретного пользователя"""
        user_id = self.kwargs.get('user_id')
        events = Event.objects.filter(user_id=user_id)
        return events

    def custom_serializing(self, queryset):
        """Кастомная сериализация queryset'а из объектов двух разных моделей"""
        results = list()
        for entry in queryset:
            item_type = entry.__class__.__name__.lower()
            if isinstance(entry, Event):
                serializer = EventSer(entry)
            if isinstance(entry, Advertisement):
                serializer = AdvertisementSer(entry)
            results.append({'item_type': item_type, 'data': serializer.data})
        return results

    def list(self, request, *args, **kwargs):
        """Переопределённый метод запроса списка"""
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.get_events_list_with_adv()
        page = self.paginate_queryset(queryset)
        if page is not None:
            data = self.custom_serializing(page)
            return self.get_paginated_response(data)
        data = self.custom_serializing(queryset=queryset)
        return Response(data)
