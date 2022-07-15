from django.http import QueryDict
from rest_framework import serializers
from .models import Wine, Winemaker


class WinemakerSerializer(serializers.ModelSerializer):
    # wines = serializers.HyperlinkedRelatedField(
    #     view_name='wine_detail',
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        depth = 1
        model = Winemaker
        fields = ('id', 'name', 'location', 'description', 'wines')


class WineSerializer(serializers.HyperlinkedModelSerializer):
    # winemaker = serializers.HyperlinkedRelatedField(
    #     view_name='winemaker_detail',
    #     read_only=True
    # )
    winemaker = WinemakerSerializer()
    winemaker_id = serializers.PrimaryKeyRelatedField(
        queryset = Winemaker.objects.all(),
        source = 'winemaker'
    )

    class Meta:
        depth = 1
        model = Wine
        fields = ('id', 'name', 'type', 'grape', 'country',
                 'price', 'label', 'link', 'winemaker_id')