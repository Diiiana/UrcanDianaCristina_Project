from django.db import models

# Create your models here.
class Weather(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    airTemperature = models.FloatField(default=0)
    cloudCover = models.FloatField(default=0)
    gust = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    precipitation = models.FloatField(default=0)
    pressure = models.FloatField(default=0)
    seaLevel = models.FloatField(default=0)
    swellDirection = models.FloatField(default=0)
    swellHeight = models.FloatField(default=0)
    swellPeriod = models.FloatField(default=0)
    visibility = models.FloatField(default=0)
    waterTemperature = models.FloatField(default=0)
    waveDirection = models.FloatField(default=0)
    waveHeight = models.FloatField(default=0)
    windWaveDirection = models.FloatField(default=0)
    windWaveHeight = models.FloatField(default=0)
    windDirection = models.FloatField(default=0)
    windSpeed = models.FloatField(default=0)

    def __str__(self):
      return "Weather"