from rest_framework.serializers import ModelSerializer, Serializer

from api.models import Event, Advertisement


class EventSer(ModelSerializer):
    """Сериализатор событий"""

    class Meta:
        model = Event
        fields = (
            'header',
            'created_at',
        )


class AdvertisementSer(ModelSerializer):

    class Meta:
        model = Advertisement
        fields = '__all__'


class FeedSerializer(Serializer):

    def to_representation(self, instance):
        if isinstance(instance, Event):
            return EventSer().to_representation(instance)
        if isinstance(instance, Advertisement):
            return AdvertisementSer().to_representation(instance)
        raise NotImplementedError
