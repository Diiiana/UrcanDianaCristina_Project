from rest_framework import serializers
from .models import Weather


class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('time', 'latitude', 'longitude', 'airTemperature', 'cloudCover', 'gust', 'humidity', 'precipitation', 'pressure', 'swellDirection',
                  'swellHeight', 'swellPeriod', 'visibility', 'waterTemperature', 'waveDirection', 'waveHeight', 'windWaveDirection', 'windWaveHeight', 'windDirection', 'windSpeed')
