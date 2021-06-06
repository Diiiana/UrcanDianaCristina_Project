import json
from datetime import datetime, timezone
from pprint import pprint

from .models import Weather

import requests

# default: (58.7984, 17.8081)
first_location = (40.105106, -73.890797) # New Jersey Bight
second_location = (39.978344, -73.947308)
third_location = (39.886616, -74.016935)

start = datetime.fromtimestamp(1591349494, tz=timezone.utc)
end = datetime.now(tz=timezone.utc)


def get_json(location):
    response = requests.get(
        'https://api.stormglass.io/v2/weather/point',
        params={
            'lat': location[0],
            'lng': location[1],
            'params': ','.join(['airTemperature', 'cloudCover', 'gust', 'humidity',
                                'precipitation', 'pressure', 'swellDirection', 'swellHeight', 'swellPeriod',
                                'visibility', 'waterTemperature', 'waveDirection', 'waveHeight', 'windWaveDirection',
                                'windWaveHeight', 'windDirection', 'windSpeed']),
            'start': start,
            'end': end,
            'source': 'noaa'
        },
        headers={
            'Authorization': '0318522a-c60f-11eb-80ed-0242ac130002-031852a2-c60f-11eb-80ed-0242ac130002'
        }
    )
    return response.json()


def insert_db(response):
    meta = response['meta']
    hours = response['hours']
    for data in hours:
        weather_data = Weather(
            time=data['time'],
            latitude=meta['lat'],
            longitude=meta['lng'],
            airTemperature=data['airTemperature']['noaa'],
            cloudCover=data['cloudCover']['noaa'],
            gust=data['gust']['noaa'],
            humidity=data['humidity']['noaa'],
            precipitation=data['precipitation']['noaa'],
            pressure=data['pressure']['noaa'],
            swellDirection=data['swellDirection']['noaa'],
            swellHeight=data['swellHeight']['noaa'],
            swellPeriod=data['swellPeriod']['noaa'],
            visibility=data['visibility']['noaa'],
            waterTemperature=data['waterTemperature']['noaa'],
            waveDirection=data['waveDirection']['noaa'],
            waveHeight=data['waveHeight']['noaa'],
            windWaveDirection=data['windWaveDirection']['noaa'],
            windWaveHeight=data['windWaveHeight']['noaa'],
            windDirection=data['windDirection']['noaa'],
            windSpeed=data['windSpeed']['noaa']
        )

        weather_data.save()


def get_parsed_data():
    for i in range(1, 4):
        if i == 1:
            result = get_json(first_location)
            insert_db(result)
        else:
            if i == 2:
                result = get_json(second_location)
                insert_db(result)
            else:
                if i == 3:
                    result = get_json(third_location)
                    insert_db(result)
    return Weather.objects.all()
