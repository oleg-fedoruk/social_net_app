from django_filters import rest_framework as filters

from api.models import Event


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class EventFilter(filters.FilterSet):
    type = CharFilterInFilter(field_name='content_type__model', lookup_expr='in')
    header = filters.CharFilter(field_name='header', lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['header']
