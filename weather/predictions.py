import random
import pandas as panda
import numpy as np

import sklearn
from sklearn import preprocessing
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeRegressor

from .models import Weather

first_location = (40.105106, -73.890797) # New Jersey Bight
second_location = (39.978344, -73.947308)
third_location = (39.886616, -74.016935)


def get_temperature_prediction(coordinates):
    weather_data = list(Weather.objects.all().order_by('time'))
    dict_weather = []
    for w in weather_data:
        if w.latitude == coordinates[0] and w.longitude == coordinates[1]:
            dict_weather.append(w.data_dict())
    data_frame = panda.DataFrame(dict_weather)
    data_frame = data_frame.drop(
        ['time', 'latitude', 'longitude', 'cloudCover', 'gust', 'seaLevel', 'swellDirection', 'swellHeight',
         'swellPeriod', 'visibility', 'waterTemperature', 'waveDirection', 'waveHeight', 'windWaveDirection',
         'windWaveHeight'], axis=1)

    temperature_x = data_frame.drop(['airTemperature'], axis=1)
    temperature_y = data_frame.pop('airTemperature')

    train_x, test_x, train_y, test_y = train_test_split(temperature_x, temperature_y, test_size=0.2, random_state=4)
    regression = DecisionTreeRegressor(random_state=0)
    regression.fit(train_x, train_y)
    prediction = regression.predict(test_x)

    error = np.mean((prediction - test_y) ** 2)

    print('             Air temperature')
    print(panda.DataFrame({
        'actual': test_y,
        'prediction': prediction,
        'error': (test_y - prediction)
    }))

    return data_frame


def get_precipitation_prediction(coordinates):
    weather_data = list(Weather.objects.all().order_by('time'))
    dict_weather = []
    for w in weather_data:
        if w.latitude == coordinates[0] and w.longitude == coordinates[1]:
            dict_weather.append(w.data_dict())
    data_frame = panda.DataFrame(dict_weather)
    data_frame = data_frame.drop(
        ['time', 'latitude', 'longitude', 'seaLevel', 'swellDirection', 'swellHeight',
         'swellPeriod', 'visibility', 'waterTemperature', 'waveDirection', 'waveHeight', 'windWaveDirection',
         'windWaveHeight', 'windDirection', 'windSpeed'], axis=1)

    precipitation_x = data_frame.drop(['precipitation'], axis=1)
    precipitation_y = data_frame.pop('precipitation')

    train_x, test_x, train_y, test_y = train_test_split(precipitation_x, precipitation_y, test_size=0.2, random_state=4)

    regression = DecisionTreeRegressor(random_state=0)

    regression.fit(train_x, train_y)

    prediction = regression.predict(test_x)

    error = np.mean((prediction - test_y) ** 2)

    print('             Precipitations')
    print(panda.DataFrame({
        'actual': test_y,
        'prediction': prediction,
        'error': (test_y - prediction)
    }))

    print("     ERROR: " + str(error) + "\n")
    return data_frame


def coordinate_prediction():
    print("First location - \n")
    get_temperature_prediction(first_location)
    print("Second location - \n")
    get_temperature_prediction(second_location)
    print("Third location - \n")
    get_temperature_prediction(third_location)
    get_precipitation_prediction(first_location)
