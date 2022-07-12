from rest_framework import serializers
from .models import Wine, Winemaker


class WinemakerSerializer(serializers.HyperlinkedModelSerializer):
    wines = serializers.HyperlinkedRelatedField(
        view_name='wine_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Winemaker
        fields = ('id', 'name', 'location', 'description', 'wines')


class WineSerializer(serializers.HyperlinkedModelSerializer):
    winemaker = serializers.HyperlinkedRelatedField(
        view_name='winemaker_detail',
        read_only=True
    )

    class Meta:
        model = Wine
        fields = ('id', 'name', 'type', 'grape', 'country',
                 'price', 'label', 'link', 'winemaker')