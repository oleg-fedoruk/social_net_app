from rest_framework.serializers import ModelSerializer

from api.models import Event, Advertisement


class EventSer(ModelSerializer):
    """Сериализатор событий"""

    class Meta:
        model = Event
        fields = (
            'header',
            'type',
            'created_at',
        )


class AdvertisementSer(ModelSerializer):

    class Meta:
        model = Advertisement
        fields = '__all__'
